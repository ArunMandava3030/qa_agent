from utils.transcription import transcribe_video
from utils.rag_generator import generate_test_cases_from_transcript
from utils.test_converter import convert_json_to_playwright
from utils.test_runner import run_playwright_tests

transcript = transcribe_video("video.mp4", "data/transcript.txt")

test_json = generate_test_cases_from_transcript("data/transcript.txt")
with open("json_tests/generated_tests.json", "w") as f:
    f.write(test_json)

convert_json_to_playwright("json_tests/generated_tests.json", "playwright_tests")

run_playwright_tests()