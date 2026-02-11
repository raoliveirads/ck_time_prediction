def drop_unnecessary_columns(df: pd.DataFrame) -> pd.DataFrame:
    columns_to_drop = ['Date', 'Heavy_Flow', 'Continuous_Flows','line_type','end_time']
    return df.drop(columns=columns_to_drop, errors="ignore")