def convert_columns_to_datetime(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    df = df.copy()
    for col in columns:
        df[col] = pd.to_datetime(df[col], format="%H:%M:%S")
    return df