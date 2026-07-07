import argparse
import asyncio
import sys
import threading
from playwright.sync_api import sync_playwright
import pandas as pd
from tqdm import tqdm


def _scrape_worker(category, location, max_scrolls, result_holder):
    if sys.platform == "win32":
        asyncio.set_event_loop(asyncio.ProactorEventLoop())
    search_query = f"{category} in {location}"
    all_data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        url = f"https://www.google.com/maps/search/{search_query.replace(' ', '+')}"
        
        print("Opening Google Maps and loading search results...")
        page.goto(url)
        page.wait_for_timeout(5000)

        results_panel = page.locator("div[role='feed']")

        print("Scrolling to load all listings...")
        for i in tqdm(range(max_scrolls), desc="Scrolling"):
            results_panel.evaluate("(el) => el.scrollTop = el.scrollHeight")
            page.wait_for_timeout(1500)
        listings = page.locator("a.hfpxzc").all()
        total = len(listings)
        
    
        print(f"Extracting details from {total} listings...")
        for index in tqdm(range(total), desc="Scraping"):
            try:
                listings = page.locator("a.hfpxzc").all()
                listing = listings[index]

                listing.click()
                try:
                    page.wait_for_selector("h1.DUwDvf", timeout=8000)
                except:
                    page.wait_for_timeout(2000)

                try:
                    name = page.locator("h1.DUwDvf").inner_text()
                except:
                    name = "N/A"

                try:
                    rating = page.locator("div.F7nice span[aria-hidden='true']").first.inner_text()
                except:
                    rating = "N/A"
                
                try:
                    reviews_count = page.locator("div.F7nice span[aria-label*='reviews']").inner_text()
                    reviews_count = reviews_count.replace("(", "").replace(")", "").strip()
                except:
                    reviews_count = "N/A"
                    
                try:
                    business_type = page.locator("button.DkEaL").inner_text()
                except:
                    business_type = "N/A"
                    
                try:
                    hours_status = page.locator("div.o0Svhf span.ZDu9vd").inner_text()
                except:
                    hours_status = "N/A"
                    
                try:
                    price_range = page.locator("span[aria-label*='Price']").inner_text()
                except:
                    price_range = "N/A"

                try:
                    address = page.locator("button[data-item-id='address']").inner_text()
                    address = address.replace("\ue0c8", "").strip()
                except:
                    address = "N/A"

                try:
                    phone = page.locator("button[data-item-id^='phone']").inner_text()
                    phone = phone.replace("\ue0b0", "").strip()
                except:
                    phone = "N/A"

                try:
                    website = page.locator("a[data-item-id='authority']").inner_text()
                    website = website.replace("\ue0c8", "").strip()
                except:
                    website = "N/A"

                all_data.append({
                    "name": name,
                    "rating": rating,
                    "reviews_count": reviews_count,
                    "business_type": business_type,
                    "hours_status": hours_status,
                    "price_range": price_range,
                    "address": address,
                    "phone": phone,
                    "website": website
                })

            except Exception as e:
                print(f"Skipped index {index}, error: {e}")
                continue

        browser.close()

    result_holder["data"] = all_data


def scrape_google_maps(category, location, max_scrolls=5):
    result_holder = {}
    thread = threading.Thread(
        target=_scrape_worker,
        args=(category, location, max_scrolls, result_holder)
    )
    thread.start()
    thread.join()
    return result_holder.get("data", [])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--category", required=True)
    parser.add_argument("--location", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--no_website", action="store_true")
    parser.add_argument("--min_rating", type=float, default=None)
    args = parser.parse_args()

    data = scrape_google_maps(args.category, args.location, max_scrolls=5)
    df = pd.DataFrame(data)

    # Remove duplicates
    df = df.drop_duplicates(subset=["name", "address"], keep="first")

    # Optional filter: no website
    if args.no_website:
        df = df[df["website"] == "N/A"]

    # Optional filter: minimum rating
    if args.min_rating is not None:
        df["rating_numeric"] = pd.to_numeric(df["rating"], errors="coerce")
        df = df[df["rating_numeric"] >= args.min_rating]
        df = df.drop(columns=["rating_numeric"])

    df.to_csv(args.output, index=False)
    print(f"Saved {len(df)} results to {args.output}")