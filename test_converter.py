import json
import os

def convert_json_to_playwright(json_file_path, output_dir):
    with open(json_file_path, 'r') as f:
        test_cases = json.load(f)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    for i, test in enumerate(test_cases['tests']):
        filename = f"test_{i+1}_{test.get('name', test.get('testName', 'Unnamed')).replace(' ', '_')}.spec.ts"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w') as file:
            # Generate Playwright commands from steps
            playwright_commands = []
            for step in test['steps']:
                command = generate_playwright_command(step)
                if command:
                    playwright_commands.append(command)
            
            file.write(f"""import {{ test, expect }} from '@playwright/test';

test('{test.get('description', test.get('testName', 'Test'))}', async ({{ page }}) => {{
    {chr(10).join([f'    {cmd}' for cmd in playwright_commands])}
}});
""")

def generate_playwright_command(step):
    """Convert a step dictionary to a Playwright command"""
    action = step.get('action', step.get('command', ''))
    target = step.get('target', '')
    value = step.get('value', '')
    condition = step.get('condition', '')
    
    if action == 'navigate':
        return f"await page.goto('{target}');"
    
    elif action == 'fill':
        return f"await page.fill('{target}', '{value}');"
    
    elif action == 'click':
        return f"await page.click('{target}');"
    
    elif action == 'expect':
        if condition == 'toBeVisible':
            return f"await expect(page.locator('{target}')).toBeVisible();"
        elif condition == 'toHaveAttribute':
            return f"await expect(page.locator('{target}')).toHaveAttribute('{value}');"
        elif condition == 'toContainText':
            return f"await expect(page.locator('{target}')).toContainText('{value}');"
        else:
            return f"await expect(page.locator('{target}')).{condition}();"
    
    elif action == 'select':
        return f"await page.selectOption('{target}', '{value}');"
    
    elif action == 'checkA11y':
        return f"// Accessibility check - requires @axe-core/playwright\n    // await injectAxe(page);\n    // await checkA11y(page);"
    
    elif action == 'setViewportSize':
        width = step.get('width', 1920)
        height = step.get('height', 1080)
        return f"await page.setViewportSize({{ width: {width}, height: {height} }});"
    
    elif action == 'wait':
        timeout = step.get('timeout', 1000)
        return f"await page.waitForTimeout({timeout});"
    
    elif action == 'waitForSelector':
        return f"await page.waitForSelector('{target}');"
    
    elif action == 'type':
        return f"await page.type('{target}', '{value}');"
    
    elif action == 'press':
        return f"await page.press('{target}', '{value}');"
    
    elif action == 'hover':
        return f"await page.hover('{target}');"
    
    elif action == 'screenshot':
        return f"await page.screenshot({{ path: '{target}' }});"
    
    else:
        # Fallback for unknown actions
        return f"// Unknown action: {action} - {target}"

def main():
    # Example usage
    convert_json_to_playwright("json_tests/generated_tests.json", "playwright_tests")

if __name__ == "__main__":
    main()