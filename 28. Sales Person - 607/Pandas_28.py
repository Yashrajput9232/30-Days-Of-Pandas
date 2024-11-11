import pandas as pd

def sales_person(salesperson: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_com_id = company[company['name'] == 'RED']['com_id'].values[0]
    salespersons_with_red_orders = orders[orders['com_id'] == red_com_id]['sales_id'].unique()
    result = salesperson[~salesperson['sales_id'].isin(salespersons_with_red_orders)][['name']]
    return result