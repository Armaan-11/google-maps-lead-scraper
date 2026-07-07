import streamlit as st
import pandas as pd
import subprocess
import sys
import os

st.set_page_config(page_title="Lead Scraper", layout="centered")

st.title("Google Maps Lead Scraper")
st.write("Search any type of business in any location and get contact details instantly.")

category = st.text_input("What do you want to search? (e.g. restaurants, gyms, grocery stores)")
location = st.text_input("Location / City (e.g. Delhi, Mumbai)")

st.write("Optional filters:")
col1, col2 = st.columns(2)
with col1:
    no_website = st.checkbox("Only show businesses with NO website")
with col2:
    use_min_rating = st.checkbox("Set minimum rating")
    min_rating_value = None
    if use_min_rating:
        min_rating_value = st.number_input("Minimum rating", min_value=0.0, max_value=5.0, value=4.0, step=0.1)

search_button = st.button("Search")

if search_button:
    if not category or not location:
        st.error("Please fill in both the category and location fields.")
    else:
        output_file = "streamlit_results.csv"

        # Remove old output file if it exists
        if os.path.exists(output_file):
            os.remove(output_file)

        command = [
            sys.executable,
            "scraper.py",
            "--category", category,
            "--location", location,
            "--output", output_file
        ]

        if no_website:
            command.append("--no_website")

        if use_min_rating:
            command.extend(["--min_rating", str(min_rating_value)])

        with st.spinner("Scraping in progress... this may take a few minutes. A browser window will open."):
            result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode != 0:
            st.error("An error occurred while scraping.")
            st.code(result.stderr)
        elif not os.path.exists(output_file):
            st.warning("No results file was created. Something went wrong.")
        else:
            df = pd.read_csv(output_file)

            if len(df) == 0:
                st.warning("No results found. Try a different search.")
            else:
                st.success(f"Found {len(df)} results!")
                st.dataframe(df)

                csv_data = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="Download CSV",
                    data=csv_data,
                    file_name=f"{category}_{location}.csv",
                    mime="text/csv"
                )