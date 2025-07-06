# 🤖 QA Agent – End-to-End Automated Frontend Testing for Recruter.ai

This project is an **AI-powered multi-tool QA Agent** that automates the entire frontend testing pipeline for [Recruter.ai](https://recruter.ai). It integrates **LLMs, RAG (Retrieval-Augmented Generation)**, and **Playwright** to generate, execute, and report test cases — based on natural language inputs and video demonstrations.

---

## 🚀 Features

- 🎯 **Test Case Generator (RAG + LLM)**
  - Parses "How-to" YouTube video of the app
  - Transcribes audio using OpenAI Whisper
  - Extracts relevant steps and converts them into JSON test cases

- 🧪 **Playwright Test Executor**
  - Converts LLM-generated JSON into Playwright scripts
  - Executes tests in headless Chromium environment

- 📊 **Report Generator**
  - Generates structured pass/fail reports for all steps
  - Logs errors and success messages

- 🎧 **Whisper-based Video Transcription**
  - Uses OpenAI’s Whisper model to understand app flow from videos

---

## 🧠 Tech Stack

| Tool/Library       | Purpose                                  |
|--------------------|-------------------------------------------|
| Python             | Core language                             |
| OpenAI Whisper     | Audio/video transcription                 |
| LangChain + LLMs   | Prompting and test generation             |
| Playwright (Python)| Frontend test automation                  |
| JSON               | Intermediate test step format             |
| GitHub             | Version control                           |

---

## 🗂️ Folder Structure

```

qa\_agent\_recruter/
├── agents/
│   └── llm\_agent.py              # Handles LLM prompt logic
├── data/
│   └── transcript.txt            # Transcribed video content
├── generated\_tests/
│   └── test\_case\_1.py           # Generated Playwright test
├── utils/
│   ├── whisper\_transcriber.py   # Whisper transcription logic
│   ├── test\_runner.py           # Runs Playwright tests
│   └── json\_to\_playwright.py    # Converts JSON to Playwright script
├── venv/                        # Virtual environment
├── main.py                      # Entry point
└── README.md

````

---

## ⚙️ Setup Instructions

1. **Clone the repo:**

```bash
git clone https://github.com/ArunMandava3030/qa_agent.git
cd qa_agent
````

2. **Create a virtual environment:**

```bash
python -m venv venv
```

3. **Activate the virtual environment:**

* On Windows:

  ```bash
  venv\Scripts\activate
  ```
* On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

4. **Install the requirements:**

```bash
pip install -r requirements.txt
```

> 📌 Note: Playwright dependencies may need to be installed manually:

```bash
playwright install
```

---

## ▶️ How to Run the Agent

```bash
python main.py
```

* This will:

  * Transcribe video content using Whisper
  * Generate test cases via LLM (LangChain)
  * Auto-convert and run tests using Playwright
  * Print a summary report of test results

---

## 📎 Sample Output

```bash
Device set to use cpu
Transcription complete.
LLM Response: 5 valid test cases extracted.
✅ Test 1: Passed
❌ Test 2: Element not found
✅ Test 3: Passed
...
```

---

## 🧪 Sample Test Case Format (JSON)

```json
{
  "test_name": "Login Test",
  "steps": [
    {"action": "goto", "url": "https://recruter.ai"},
    {"action": "click", "selector": "#login-button"},
    {"action": "fill", "selector": "#email", "value": "test@example.com"},
    {"action": "fill", "selector": "#password", "value": "secure123"},
    {"action": "click", "selector": "#submit"},
    {"action": "assert", "selector": "#dashboard", "text": "Welcome"}
  ]
}
```

---

## 🛠️ Troubleshooting

* **Push to GitHub Failing?**

  * Avoid pushing `venv/` or large files. Add to `.gitignore`.
  * GitHub has a 100MB file size limit.

* **Playwright not found?**

  * Run: `pip install playwright` and `playwright install`

* **Whisper not working on CPU?**

  * Warning is fine. It defaults to FP32 when GPU isn’t available.

---

## 📢 Contributing

Feel free to fork this project, submit pull requests, or suggest improvements via [issues](https://github.com/ArunMandava3030/qa_agent/issues).

---

## 👨‍💻 Author

**Arun Mandava**
📧 [arunmandava3030@gmail.com](mailto:arunmandava3030@gmail.com)
🔗 [LinkedIn](https://linkedin.com/in/arunmandava3030)
💻 [GitHub](https://github.com/ArunMandava3030)

---

## 📜 License

This project is open-source under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

* [OpenAI Whisper](https://github.com/openai/whisper)
* [LangChain](https://github.com/langchain-ai/langchain)
* [Microsoft Playwright](https://playwright.dev/python)


