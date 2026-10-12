import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# --- CONFIGURATION ---
st.set_page_config(page_title="Poll Results Visualizer", layout="wide")
st.title("📊 Tech Survey Data Dashboard")
st.markdown("Analyze preferred data tools, satisfaction ratings, and user feedback from synthetic poll data.")

# --- DATA LOADING & CLEANING ---
@st.cache_data
def load_and_clean_data():
    try:
        df = pd.read_csv('data/raw_poll_data.csv')
    except FileNotFoundError:
        st.error("Data not found. Please run `python src/data_generator.py` first.")
        return pd.DataFrame()

    # Data Cleaning Phase
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Date'] = df['Timestamp'].dt.date
    df['Preferred_Tool'] = df['Preferred_Tool'].str.strip().str.title()
    df['Feedback'] = df['Feedback'].fillna("No Comment") # Handle missing text
    return df

df = load_and_clean_data()

if not df.empty:
    # --- SIDEBAR FILTERS ---
    st.sidebar.header("Filter Results")
    selected_regions = st.sidebar.multiselect("Select Region", df['Region'].unique(), default=df['Region'].unique())
    selected_age = st.sidebar.multiselect("Select Age Group", df['Age_Group'].unique(), default=df['Age_Group'].unique())

    # Apply Filters
    filtered_df = df[(df['Region'].isin(selected_regions)) & (df['Age_Group'].isin(selected_age))]

    # --- TOP METRICS ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Responses", len(filtered_df))
    col2.metric("Average Satisfaction", round(filtered_df['Satisfaction_1_to_5'].mean(), 2))
    top_tool = filtered_df['Preferred_Tool'].mode()[0] if not filtered_df.empty else "N/A"
    col3.metric("Most Popular Tool", top_tool)

    st.divider()

    # --- VISUALIZATIONS ---
    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.subheader("🏆 Preferred Tools Distribution")
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        sns.countplot(y='Preferred_Tool', data=filtered_df, order=filtered_df['Preferred_Tool'].value_counts().index, palette='viridis', ax=ax1)
        ax1.set_xlabel("Number of Votes")
        ax1.set_ylabel("Tool")
        st.pyplot(fig1)

    with col_chart2:
        st.subheader("⭐ Satisfaction Ratings")
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        sns.histplot(filtered_df['Satisfaction_1_to_5'], bins=5, kde=False, color='coral', ax=ax2)
        ax2.set_xlabel("Rating (1-5)")
        ax2.set_ylabel("Frequency")
        ax2.set_xticks([1, 2, 3, 4, 5])
        st.pyplot(fig2)

    st.divider()
    
    col_chart3, col_chart4 = st.columns(2)
    
    with col_chart3:
        st.subheader("📈 Responses Over Time")
        daily_counts = filtered_df.groupby('Date').size().reset_index(name='Counts')
        st.line_chart(daily_counts.set_index('Date'))

    with col_chart4:
        st.subheader("💬 Feedback Word Cloud")
        # Filter out "No Comment" for wordcloud
        text_data = ' '.join(filtered_df[filtered_df['Feedback'] != 'No Comment']['Feedback'].tolist())
        if text_data.strip():
            wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='magma').generate(text_data)
            fig3, ax3 = plt.subplots(figsize=(8, 4))
            ax3.imshow(wordcloud, interpolation='bilinear')
            ax3.axis('off')
            st.pyplot(fig3)
        else:
            st.info("No text feedback available for current filters.")

    # --- DATA PREVIEW ---
    with st.expander("Preview Cleaned Dataset"):
        st.dataframe(filtered_df.head(50))