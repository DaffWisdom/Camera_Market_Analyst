# Canon R50 Used Market Analysis 📸

This project is an end-to-end data pipeline designed to scrape, clean, and analyze the used market prices of the **Canon R50** camera on a Vietnamese e-commerce platform.

## 🚀 Project Overview
- **Data Ingestion**: Scrapes listings from Chotot using `requests` and `BeautifulSoup`, featuring robust session management and anti-bot measures.
- **Data Cleaning**: Leverages `Pandas` and advanced `Regex` to extract camera conditions and lens configurations from Vietnamese listing titles.
- **EDA & Visualization**: Analyzes price distributions and configuration impacts using `Seaborn` and `Matplotlib`.

## 🔍 Key Data Insight: Behavioral Data Bias
Analysis of the Canon R50 used market reveals a significant **Behavioral Data Bias** in seller listing habits. Despite expected price variance between "Body Only" and "Kit" configurations, the median prices across these categories remained nearly identical. 

This phenomenon suggests that sellers of entry-level gear—who are often hobbyists rather than professional resellers—frequently include the standard kit lens (18-45mm) by default but omit explicit keywords like "Kit" or "Lens" from their titles, assuming it is the "standard" offering. Consequently, classification models based solely on title keywords likely suffer from high false-negative rates for kit inclusions.

## 🛠️ Tech Stack
- **Python 3.12**
- **Pandas** (Data Manipulation)
- **BeautifulSoup4** (Web Scraping)
- **Seaborn/Matplotlib** (Visualization)
- **Regex** (Feature Engineering)

## 📂 File Structure
- `test_scraper.py`: Scraper script with session persistence.
- `data_cleaning.py`: Cleans raw data and extracts features.
- `eda_visualization.py`: Generates price distribution plots.
- `used_camera_canon_r50_cleaned.csv`: The processed dataset.

---
*Developed as part of a Data Science Portfolio.*
