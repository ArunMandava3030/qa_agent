import { test, expect } from '@playwright/test';

test('Test candidate search functionality', async ({ page }) => {
        await page.goto('https://recruiter.ai/search');
    await page.fill('#search-input', 'software engineer');
    await page.click('#search-button');
    await expect(page.locator('.search-results')).toBeVisible();
});
