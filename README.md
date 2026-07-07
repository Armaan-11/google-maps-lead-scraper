# Google Maps Lead Scraper

A Python-based Google Maps business scraper with a simple Streamlit web interface. Search for any type of business in any location and extract publicly available business information, then export the results as a CSV file.

Built using **Playwright** for browser automation, **Pandas** for data handling, and **Streamlit** for the user interface.

---

## Features

* 🔍 Search any business category (restaurants, gyms, salons, hospitals, grocery stores, etc.)
* 📍 Search businesses in any city or location
* 📊 Extract business details including:

  * Business Name
  * Rating
  * Address
  * Phone Number
  * Website
* 💻 Simple Streamlit web interface
* 📁 Download results as a CSV file
* ⚡ Automated browser interaction using Playwright

---

## Tech Stack

* Python 3
* Playwright
* Streamlit
* Pandas

---

## Project Structure

```text
google-maps-lead-scraper/
│
├── app.py              # Streamlit application
├── scraper.py          # Google Maps scraping logic
├── requirements.txt    # Project dependencies
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Armaan-11/google-maps-lead-scraper.git
cd google-maps-lead-scraper
```

### 2. Create a virtual environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browser

```bash
playwright install
```

---

## Requirements

The project uses the following Python packages:

```text
streamlit>=1.36.0
pandas>=2.2.2
playwright>=1.53.0
```

These are already included in the `requirements.txt` file.

---

## Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

1. Enter a business category.
2. Enter a city or location.
3. Select the fields you want to include.
4. Click **Search**.
5. Download the results as a CSV file.

---

## Output

The scraper extracts publicly available business information such as:

* Name
* Rating
* Address
* Phone Number
* Website

The results are displayed inside the Streamlit application and can be exported as a CSV file.

---

## Notes

* The browser runs in **non-headless mode** by default so the scraping process is visible.
* Large searches may take several minutes depending on the number of businesses available.
* Google Maps may occasionally display CAPTCHA or rate-limit automated requests.

---

## Disclaimer

This project is intended for **educational and research purposes only**.

Users are responsible for ensuring that their use of this software complies with applicable laws and Google's Terms of Service.
