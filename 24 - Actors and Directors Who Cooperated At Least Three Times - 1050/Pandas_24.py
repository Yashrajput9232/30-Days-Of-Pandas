import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    result = (actor_director.groupby(['actor_id', 'director_id'])
              .size()  # Count each pair's occurrences
              .reset_index(name='count')
              .query('count >= 3')  # Filter pairs with count >= 3
              [['actor_id', 'director_id']])  # Select relevant columns

    return result
