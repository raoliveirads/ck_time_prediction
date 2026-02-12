import pandas as pd
def encode_binary_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    for col in columns:
        df[col] = df[col].apply(lambda x: 1 if x == 'X' else 0)
    return df