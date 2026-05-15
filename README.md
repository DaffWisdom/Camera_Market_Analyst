# Used Camera Market Analysis (Canon R50)
## Project Overview
This is an end-to-end data analysis project focused on the resale market of the **Canon R50** camera. The project covers the entire data pipeline: from automated web scraping and data cleaning to feature engineering and exploratory data analysis (EDA).

## 🚀 Key Features
- **Automated Ingestion**: Scraped 100+ listings from a major e-commerce platform using Python (BeautifulSoup/Requests) with pagination and anti-bot mechanisms.
- **Data Wrangling**: Cleaned messy currency strings and transformed raw text into structured numerical data using Pandas.
- **Feature Engineering**: Used Regular Expressions (Regex) to extract hidden attributes like "Includes Kit Lens" and "Fullbox Status" from product titles.
- **Insightful EDA**: Visualized price distributions and market segments using Seaborn and Matplotlib.

## 🧠 The "Behavioral Data Bias" Discovery
A core finding of this project was the overlap in median prices between "Body Only" and "Fullbox" listings. 
- **The Observation**: Initial analysis showed that "Body Only" cameras were priced similarly to "Fullbox" kits.
- **The Insight**: Through domain knowledge, I deduced that sellers of entry-level cameras like the Canon R50 often sell the full kit but fail to explicitly state "Kit" or "Lens" in the short title.
- **The Solution**: I implemented a more robust Regex filter and acknowledged the limitation of title-only extraction, suggesting that future iterations should mine the product description field for higher accuracy.

## 🛠️ Tech Stack
- **Languages**: Python
- **Libraries**: BeautifulSoup4, Requests, Pandas, Matplotlib, Seaborn, Regex
- **Tools**: VS Code, Git

## 📈 Visualizations
(Plots are saved in the `outputs/` folder)
- **Histogram**: Shows a concentration of prices around 16.5M VND.
- **Boxplots**: Highlight market consistency and outliers in the Fullbox segment.

## How to Run
1. Clone the repository.
2. Run `pip install -r requirements.txt`.
3. Execute `python test_scraper.py` to get raw data.
4. Execute `python data_cleaning.py` to process features.
5. Execute `python eda_visualization.py` for insights.
