import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    never_ordered = customers[~customers['id'].isin(orders['customerId'])]
    customers = never_ordered[['name']].rename(columns={'name': 'Customers'})
    return customers
