from data_loader import load_data
from pipeline import run_cleaning_pipeline

if __name__ == "__main__":
    
    df = load_data("../data/raw/checkin_queue_synthetic_2019_2025v2.csv")
    df_clean = run_cleaning_pipeline(df)
    
    df_clean.to_csv("../data/processed/checkin_queue_cleaned.csv", index=False)