import pandas as pd
from cleaning.convert_columns_to_datetime import convert_columns_to_datetime
from cleaning.drop_columns import drop_columns
from cleaning.drop_unnecessary_columns import drop_unnecessary_columns
from cleaning.handle_outliers_iqr import handle_outliers_iqr
from cleaning.remove_outliers_iqr import remove_outliers_iqr
from cleaning.remove_duplicates import remove_duplicates

from features.add_duration_features import add_duration_features
from features.add_period_of_day import add_period_of_day
from features.add_total_checked_bags import add_total_checked_bags
from features.encode_binary_columns import encode_binary_columns

def run_cleaning_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    
    df = drop_unnecessary_columns(df)
    df = remove_duplicates(df)
    
    df = encode_binary_columns(df, [
        'Queue_Agent', 
        'PAX_Left', 
        'Flight_Cancelled',
        'Carousel_Stoped'
    ])
    
    df = convert_columns_to_datetime(df, [
        'Start_Time', 
        'Start_Line', 
        'End_line', 
        'Service_Start', 
        'Service_End'
    ])
    
    df = add_period_of_day(df, 'Start_Time')
    df = drop_columns(df, ['Start_Time'])
    
    df = add_duration_features(df)
    df = add_total_checked_bags(df)
    
    df = drop_columns(df, [
        'Start_Line',
        'End_line',
        'Service_Start',
        'Service_End',
        'Luggage_In',
        'Luggage_Out',
        'Line_Time',
        'Service_Time',
        'Year',
        'End_Time'
    ])
    
    df = remove_outliers_iqr(df, ['Total_Time'])
    
    df = remove_duplicates(df)
    
    return df