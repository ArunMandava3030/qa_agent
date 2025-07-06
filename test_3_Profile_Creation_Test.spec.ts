import { test, expect } from '@playwright/test';

test('Test user profile creation', async ({ page }) => {
        await page.goto('https://recruiter.ai/profile');
    await page.fill('#company-name', 'Test Company');
    await page.fill('#position', 'HR Manager');
    await page.click('#save-profile');
    await expect(page.locator('.success-message')).toBeVisible();
});
