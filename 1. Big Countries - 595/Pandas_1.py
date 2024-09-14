import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Filter based on the conditions: area >= 3000000 or population >= 25000000
    big_countries = world.loc[
        (world['area'] >= 3000000) | (world['population'] >= 25000000),
        ['name', 'population', 'area']
    ]
    
    return big_countries
