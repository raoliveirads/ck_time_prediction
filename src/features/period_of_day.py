def add_period_of_day(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df = df.copy()
    
    hours = df[column].dt.hour
    
    conditions = [
        (hours >= 5) & (hours < 12),
        (hours >= 12) & (hours < 17),
        (hours >= 17) & (hours < 21),
    ]
    
    choices = ["Morning", "Afternoon", "Evening"]
    
    df["Period_of_Day"] = np.select(conditions, choices, default="Night")
    
    return df