def add_duration_features(df: pd.DataFrame) -> pd.DataFrame:
    df['line_duration_min'] = (pd.to_datetime(df['End_Line']) - pd.to_datetime(df['Start_Line'])).dt.total_seconds()/60
    df['service_duration_min'] = (pd.to_datetime(df['Service_End']) - pd.to_datetime(df['Service_Start'])).dt.total_seconds()/60
    df['Total_Time'] = df['Line_Time'] + df['Service_Time']
    return df