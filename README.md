# 📊 Poll Results Visualizer

## 📖 Overview
The **Poll Results Visualizer** is an end-to-end data analytics project that processes raw survey and poll data, performs automated data wrangling, and deploys an interactive web dashboard. It enables stakeholders to rapidly understand user preferences, satisfaction metrics, and qualitative feedback trends without manual spreadsheet analysis.

## ✨ Features
* **Automated Data Cleaning:** Uses Pandas to handle missing text, normalize dates, and standardize categorical variables.
* **Interactive Dashboard:** Built with Streamlit, allowing users to dynamically filter poll results by demographic inputs like Age and Region.
* **Visual Analytics:** Includes comparative bar charts for option preferences, histograms for satisfaction ratings, and time-series line charts for response tracking.
* **Text Mining:** Generates real-time Word Clouds from unstructured, open-ended survey feedback.
* **Synthetic Data Generation:** Includes a built-in Python script to generate thousands of rows of realistic poll data for testing and portfolio demonstration.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Manipulation:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn, WordCloud
* **Web Framework:** Streamlit

## 📂 Project Structure
```text
Poll-Results-Visualizer/
│
├── data/                  # Stores raw_poll_data.csv 
├── src/                   # Contains Python helper scripts
│   └── data_generator.py  # Script to create synthetic survey data
├── app.py                 # Main Streamlit dashboard script
├── requirements.txt       # List of installed libraries
└── README.md              # Project documentation

🚀 Installation & Setup

    Clone the repository:
    Bash

    git clone [https://github.com/YOUR_USERNAME/Poll-Results-Visualizer.git](https://github.com/YOUR_USERNAME/Poll-Results-Visualizer.git)
    cd Poll-Results-Visualizer

    Create and activate a virtual environment:

        Windows: python -m venv venv and venv\Scripts\activate

        Mac/Linux: python3 -m venv venv and source venv/bin/activate

    Install dependencies:
    Bash

    pip install -r requirements.txt

💻 Usage

    Generate the dataset: Run the data generator to create the synthetic poll responses.
    Bash

    python src/data_generator.py

    Launch the dashboard:
    Bash

    streamlit run app.py

    Open your browser to http://localhost:8501 to view the interactive application.
