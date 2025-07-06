import { test, expect } from '@playwright/test';

test('Test user login functionality', async ({ page }) => {
        await page.goto('https://recruiter.ai/login');
    await page.fill('#email', 'test@example.com');
    await page.fill('#password', 'password123');
    await page.click('#login-button');
    await expect(page.locator('.dashboard')).toBeVisible();
});
