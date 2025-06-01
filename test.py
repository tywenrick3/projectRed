import logging, time
from playwright.sync_api import Playwright, sync_playwright, expect

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def search_bestbuy_nintendo_switch():
    logging.info("Starting Playwright session")
    with sync_playwright() as p:
        logging.info("Launching Chromium browser")
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        logging.info("Navigating to BestBuy homepage")
        page.goto("https://www.bestbuy.com/")

        logging.info("Locating search box")
        search_field = page.get_by_role("textbox", name="Search Best Buy")

        logging.info("Filling search field with 'Nintendo Switch'")
        search_field.fill("Nintendo Switch")

        logging.info("Pressing Enter to search")
        search_field.press("Enter")

        logging.info("Waiting 5 seconds for results to load")
        page.wait_for_timeout(5000)

        logging.info("Closing browser")
        browser.close()

    logging.info("Playwright session completed")

if __name__ == "__main__":
    search_bestbuy_nintendo_switch()