import pandas as pd
def add_total_checked_bags(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Total_Checked_Bags"] = df["Luggage_In"] - df["Luggage_Out"]
    return df