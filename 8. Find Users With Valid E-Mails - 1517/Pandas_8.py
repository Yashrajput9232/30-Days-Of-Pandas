import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid_email_pattern = r'^[a-zA-Z][\w\.-]*@leetcode\.com$'
    
    users['valid'] = users['mail'].apply(lambda x: bool(re.match(valid_email_pattern, x)))
    valid_users = users[users['valid'] == True].drop(columns=['valid'])
    
    return valid_users   