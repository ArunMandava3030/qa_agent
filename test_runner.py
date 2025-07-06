import subprocess
import json
import os

def run_playwright_tests():
    # Run using shell=True so it uses your system PATH
    result = subprocess.run(
        "npx playwright test --reporter=json",
        shell=True,  # Important for Windows
        capture_output=True,
        text=True
    )

    # Ensure 'reports' directory exists
    os.makedirs("reports", exist_ok=True)

    # Attempt to parse and save the JSON
    try:
        json_output = json.loads(result.stdout)
        with open("reports/report.json", "w", encoding="utf-8") as f:
            json.dump(json_output, f, indent=2)
        print("✅ Test report saved to 'reports/report.json'")
    except json.JSONDecodeError:
        print("❌ Failed to parse Playwright output as JSON.")
        print("Raw Output:\n", result.stdout)

    return result.stdout
