from playwright.sync_api import Playwright, sync_playwright, expect
import time

def search_bestbuy_nintendo_switch():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.bestbuy.com/")

        search_field = page.get_by_role("textbox", name="Search Best Buy")
        search_field.fill("Nintendo Switch")
        search_field.press("Enter")

        page.wait_for_timeout(5000) 
        browser.close()

if __name__ == "__main__":
    search_bestbuy_nintendo_switch()