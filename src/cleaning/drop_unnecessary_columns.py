import pandas as pd
def drop_unnecessary_columns(df: pd.DataFrame) -> pd.DataFrame:
    columns_to_drop = ['Date', 'Heavy_Flow', 'Continuous_Flow','Line_Type','End_time','Year']
    return df.drop(columns=columns_to_drop, errors="ignore")