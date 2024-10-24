import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['event_date'] = pd.to_datetime(activity['event_date'])   
    result = activity.groupby('player_id')['event_date'].min().reset_index()
    result.columns = ['player_id', 'first_login']
    
    return result
