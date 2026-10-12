import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

def generate_synthetic_data(num_records=500):
    np.random.seed(42)
    
    # Options
    tools = ['Python', 'R', 'Excel', 'Tableau', 'Power BI', 'SQL']
    age_groups = ['18-24', '25-34', '35-44', '45+']
    regions = ['North America', 'Europe', 'Asia', 'Remote']
    feedbacks = [
        "Great tool, very useful", "Needs improvement", "Super helpful!",
        "A bit hard to learn", "Best for data cleaning", "I use it daily",
        "Could be faster", "Excellent community support", "", "Steep learning curve"
    ]
    
    data = []
    start_date = datetime.now() - timedelta(days=30)
    
    for i in range(num_records):
        timestamp = start_date + timedelta(days=random.randint(0, 30), minutes=random.randint(0, 1440))
        tool = random.choice(tools)
        
        # Bias satisfaction based on tool to create interesting data
        if tool in ['Python', 'SQL']:
            satisfaction = np.random.choice([4, 5, 5, 3, 4])
        else:
            satisfaction = np.random.choice([1, 2, 3, 4, 5])
            
        record = {
            'Timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'Respondent_ID': f'RESP_{1000+i}',
            'Age_Group': np.random.choice(age_groups, p=[0.4, 0.4, 0.15, 0.05]),
            'Region': random.choice(regions),
            'Preferred_Tool': tool,
            'Satisfaction_1_to_5': satisfaction,
            'Feedback': random.choice(feedbacks) if random.random() > 0.2 else np.nan # 20% missing feedback
        }
        data.append(record)
        
    df = pd.DataFrame(data)
    
    # Ensure data folder exists
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/raw_poll_data.csv', index=False)
    print(f"✅ Generated {num_records} synthetic survey records in 'data/raw_poll_data.csv'")

if __name__ == "__main__":
    generate_synthetic_data(800)