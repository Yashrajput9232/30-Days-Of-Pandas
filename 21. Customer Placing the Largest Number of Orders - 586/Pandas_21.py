import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    order_counts = orders.groupby('customer_number').size().reset_index(name='order_count')
    
    max_customer = order_counts.loc[order_counts['order_count'].idxmax()]
    
    return pd.DataFrame({'customer_number': [max_customer['customer_number']]})