# Google Maps Lead Scraper

A Python-based Google Maps business scraper with a Streamlit web UI. Search for any type of business in any location and extract detailed lead information, ready to export as a CSV file.

Built using [Playwright](https://playwright.dev/python/) for browser automation and [Streamlit](https://streamlit.io/) for the user interface.

## Features

- **Search any business category, anywhere** — restaurants, gyms, grocery stores, salons, hospitals, and more, in any city or area.
- **Rich data extraction** for each business:
  - Name
  - Rating
  - Reviews count
  - Business category/type
  - Opening hours status
  - Price range (where available)
  - Address
  - Phone number
  - Website
- **Duplicate removal** — automatically removes repeated businesses based on name and address.
- **Optional filters**:
  - Only show businesses with no website (great for identifying potential leads)
  - Set a minimum rating threshold
- **Progress tracking** in the terminal via a live progress bar.
- **Simple web interface** built with Streamlit — no command-line knowledge required to use it.
- **CSV export** — download results directly from the web UI.

## Tech Stack

- Python 3
- [Playwright](https://playwright.dev/python/) — browser automation
- [Pandas](https://pandas.pydata.org/) — data handling and CSV export
- [Streamlit](https://streamlit.io/) — web interface
- [tqdm](https://github.com/tqdm/tqdm) — progress bars

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Armaan-11/google-maps-lead-scraper.git
   cd google-maps-lead-scraper
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

3. Install the required dependencies:
   ```
   pip install playwright pandas openpyxl streamlit tqdm
   playwright install chromium
   ```

## Usage

### Option 1: Web Interface (recommended)

Run the Streamlit app:
```
streamlit run app.py
```

This will open a browser tab with the interface. Enter a business category and location, optionally apply filters, click **Search**, and download the results as a CSV once scraping is complete.

### Option 2: Command Line

Run the scraper directly from the terminal:
```
python scraper.py --category "restaurants" --location "Delhi" --output "results.csv"
```

Optional flags:
- `--no_website` — only include businesses without a website
- `--min_rating 4.0` — only include businesses with a rating of 4.0 or higher

Example with filters:
```
python scraper.py --category "gyms" --location "Mumbai" --output "gyms_mumbai.csv" --no_website --min_rating 4.0
```

## How It Works

1. Opens Google Maps and performs a search based on the provided category and location.
2. Scrolls through the results panel to load all available listings.
3. Clicks into each listing to extract detailed information.
4. Cleans and structures the data using Pandas.
5. Removes duplicate entries.
6. Applies any selected filters.
7. Saves the final results to a CSV file.

## Notes

- The browser runs in visible (non-headless) mode by default so you can see the scraping process in action.
- Scraping speed depends on the number of listings and the breadth of the search (a city-level search will be much faster than a state or country-level search).
- This tool is intended for educational and personal lead-generation purposes. Please use responsibly and in accordance with Google's Terms of Service.

## Disclaimer

This project is for educational and research purposes only. The author is not responsible for any misuse of this tool. Users are responsible for ensuring their use of this software complies with applicable laws and terms of service.