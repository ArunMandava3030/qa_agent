from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.vectorstores import FAISS 
from langchain_community.document_loaders import TextLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain.chains import RetrievalQA 
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
import os 
import json

def generate_test_cases_from_transcript(transcript_path): 
    with open(transcript_path, 'r') as file: 
        transcript_text = file.read() 
 
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100) 
    docs = text_splitter.create_documents([transcript_text]) 
     
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") 
    vectorstore = FAISS.from_documents(docs, embeddings) 
    retriever = vectorstore.as_retriever() 
     
    # Use local pipeline instead of endpoint
    try:
        # Create a local text generation pipeline
        pipe = pipeline(
            "text-generation",
            model="microsoft/DialoGPT-small",  # Smaller model for local use
            max_new_tokens=256,
            temperature=0.5,
            return_full_text=False
        )
        
        # Create HuggingFace pipeline LLM
        llm = HuggingFacePipeline(pipeline=pipe)
        
    except Exception as e:
        print(f"Error loading local model: {e}")
        # Fallback to a simple text generation approach
        return generate_simple_test_cases(transcript_text)
 
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever) 
     
    prompt = ( 
        "Generate Playwright test cases in JSON format for the frontend user flow of Recruter.ai, " 
        "including edge cases and accessibility checks." 
    ) 
     
    # Use invoke instead of deprecated run method
    try:
        result = qa_chain.invoke({"query": prompt})
        response_text = result["result"]
        
        # Try to parse the response as JSON
        try:
            # If it's already a valid JSON string, return it
            json.loads(response_text)
            return response_text
        except json.JSONDecodeError:
            # If not valid JSON, fall back to simple test cases
            print("LLM response is not valid JSON, using fallback")
            return generate_simple_test_cases(transcript_text)
            
    except Exception as e:
        print(f"Error during chain execution: {e}")
        return generate_simple_test_cases(transcript_text)

def generate_simple_test_cases(transcript_text):
    """Fallback function to generate basic test cases without LLM"""
    
    # Simple template-based test case generation
    test_cases = {
        "testSuite": "Recruiter.ai Frontend Tests",
        "tests": [
            {
                "testName": "Login Flow Test",
                "description": "Test user login functionality",
                "steps": [
                    {"action": "navigate", "target": "https://recruiter.ai/login"},
                    {"action": "fill", "target": "#email", "value": "test@example.com"},
                    {"action": "fill", "target": "#password", "value": "password123"},
                    {"action": "click", "target": "#login-button"},
                    {"action": "expect", "target": ".dashboard", "condition": "toBeVisible"}
                ]
            },
            {
                "testName": "Search Functionality Test",
                "description": "Test candidate search functionality",
                "steps": [
                    {"action": "navigate", "target": "https://recruiter.ai/search"},
                    {"action": "fill", "target": "#search-input", "value": "software engineer"},
                    {"action": "click", "target": "#search-button"},
                    {"action": "expect", "target": ".search-results", "condition": "toBeVisible"}
                ]
            },
            {
                "testName": "Profile Creation Test",
                "description": "Test user profile creation",
                "steps": [
                    {"action": "navigate", "target": "https://recruiter.ai/profile"},
                    {"action": "fill", "target": "#company-name", "value": "Test Company"},
                    {"action": "fill", "target": "#position", "value": "HR Manager"},
                    {"action": "click", "target": "#save-profile"},
                    {"action": "expect", "target": ".success-message", "condition": "toBeVisible"}
                ]
            },
            {
                "testName": "Candidate Filtering Test",
                "description": "Test candidate filtering functionality",
                "steps": [
                    {"action": "navigate", "target": "https://recruiter.ai/candidates"},
                    {"action": "click", "target": "#filter-dropdown"},
                    {"action": "select", "target": "#experience-filter", "value": "3-5 years"},
                    {"action": "click", "target": "#apply-filter"},
                    {"action": "expect", "target": ".filtered-results", "condition": "toBeVisible"}
                ]
            },
            {
                "testName": "Accessibility Test",
                "description": "Test accessibility features",
                "steps": [
                    {"action": "navigate", "target": "https://recruiter.ai"},
                    {"action": "checkA11y", "target": "page"},
                    {"action": "expect", "target": "h1", "condition": "toHaveAttribute", "value": "aria-label"}
                ]
            },
            {
                "testName": "Mobile Responsive Test",
                "description": "Test mobile responsiveness",
                "steps": [
                    {"action": "setViewportSize", "width": 375, "height": 667},
                    {"action": "navigate", "target": "https://recruiter.ai"},
                    {"action": "expect", "target": ".mobile-menu", "condition": "toBeVisible"},
                    {"action": "click", "target": ".mobile-menu-toggle"},
                    {"action": "expect", "target": ".mobile-nav", "condition": "toBeVisible"}
                ]
            }
        ]
    }
    
    # Return as JSON string
    return json.dumps(test_cases, indent=2)