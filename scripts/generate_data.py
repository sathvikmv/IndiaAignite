import pandas as pd
import numpy as np
import random
import os

def generate_data():
    states = {
        "Karnataka": ["Bangalore", "Mysore", "Hubli", "Mangalore", "Belgaum"],
        "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad"],
        "Delhi": ["New Delhi", "North Delhi", "South Delhi", "East Delhi"],
        "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur"],
        "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Salem"]
    }
    
    years = list(range(2015, 2025))
    
    causes = {
        "Accidental": ["Road Accident", "Drowning", "Fire", "Fall", "Poisoning"],
        "Natural": ["Heart Attack", "Stroke", "Heat Stroke", "Epidemic"]
    }
    
    data = []
    
    for state, districts in states.items():
        for district in districts:
            for year in years:
                # Generate multiple entries per year per district with different causes
                # 3-5 records per district-year
                num_records = random.randint(3, 6)
                for _ in range(num_records):
                    death_type = random.choice(["Accidental", "Natural"])
                    cause = random.choice(causes[death_type])
                    
                    # Base count
                    count = random.randint(10, 100)
                    
                    # Trends
                    if state == "Karnataka" and cause == "Road Accident":
                        count += (year - 2015) * 15  # Increasing trend
                    
                    if state == "Delhi" and cause == "Heat Stroke":
                        count += (year - 2015) * 10 # Increasing trend due to climate?
                        
                    if state == "Kerala" and cause == "Epidemic":
                        if year in [2020, 2021]:
                            count += 200 # Covid spike simulation
                            
                    # Random noise
                    count = max(0, int(count + np.random.normal(0, 10)))
                    
                    data.append({
                        "State": state,
                        "District": district,
                        "Year": year,
                        "Type": death_type,
                        "Cause": cause,
                        "Deaths": count
                    })
                    
    df = pd.DataFrame(data)
    
    output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/dataset.csv"))
    df.to_csv(output_path, index=False)
    print(f"Dataset generated at {output_path} with {len(df)} records.")

if __name__ == "__main__":
    generate_data()
