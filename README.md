# 📊 Poll Results Visualizer

## 📖 Overview
The Poll Results Visualizer is an end-to-end data analytics project that ingests raw survey data, performs data cleaning, and deploys an interactive Streamlit dashboard. It helps stakeholders rapidly understand user preferences, satisfaction metrics, and qualitative feedback trends.

## 🎯 Problem Statement
Raw survey data (spreadsheets) is difficult to interpret at scale. Organizations need automated pipelines to transform rows of text and numbers into actionable insights, demographic trends, and visual summaries.

## 💡 Solution
This project utilizes Python and Pandas to clean demographic and polling data, calculating statistical distributions automatically. It then serves these insights through an interactive UI, featuring dynamic filtering, temporal analysis, and text-mining (Word Clouds).

## ✨ Features
*   **Automated Data Cleaning:** Handles missing text, normalizes dates, and standardizes categorical variables.
*   **Interactive Dashboard:** Built with Streamlit, allowing users to filter by demographic inputs (Age, Region).
*   **Visual Analytics:** Includes comparative bar charts, satisfaction histograms, and time-series line charts.
*   **Text Analysis:** Generates real-time Word Clouds from open-ended survey feedback.

## 🛠️ Tech Stack
*   **Language:** Python 3.x
*   **Data Manipulation:** Pandas, NumPy
*   **Visualization:** Matplotlib, Seaborn, WordCloud
*   **Web Framework:** Streamlit

## 🚀 How to Run Locally

1. Clone the repository:
   `git clone https://github.com/YOUR_USERNAME/Poll-Results-Visualizer.git`
2. Install dependencies:
   `pip install -r requirements.txt`
3. Generate the synthetic survey dataset:
   `python src/data_generator.py`
4. Launch the dashboard:
   `streamlit run app.py`

## 📸 Screenshots
*(Add your dashboard screenshots here once you run the project)*