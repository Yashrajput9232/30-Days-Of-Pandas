import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    condition_filter = patients['conditions'].str.contains(r'\bDIAB1', na=False)
    
    result_df = patients[condition_filter]
    return result_df