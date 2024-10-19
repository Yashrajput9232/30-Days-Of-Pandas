import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    bins = [-float('inf'), 20000, 50000, float('inf')]
    labels = ['Low Salary', 'Average Salary', 'High Salary']
    
    accounts['category'] = pd.cut(accounts['income'], bins=bins, labels=labels)
    
    result = accounts.groupby('category').size().reset_index(name='accounts_count')
    
    result = result.set_index('category').reindex(labels, fill_value=0).reset_index()
    
    return result
