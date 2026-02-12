import pandas as pd
def add_duration_features(df: pd.DataFrame) -> pd.DataFrame:
    df['Line_Time'] = (pd.to_datetime(df['End_line']) - pd.to_datetime(df['Start_Line'])).dt.total_seconds()/60
    df['Service_Time'] = (pd.to_datetime(df['Service_End']) - pd.to_datetime(df['Service_Start'])).dt.total_seconds()/60
    df['Total_Time'] = df['Line_Time'] + df['Service_Time']
    return df