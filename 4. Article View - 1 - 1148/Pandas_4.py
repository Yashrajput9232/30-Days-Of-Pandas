import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    authors_who_viewed = views[views['author_id'] == views['viewer_id']]
    
    result = authors_who_viewed[['author_id']].drop_duplicates().rename(columns={'author_id': 'id'}).sort_values(by='id')
    
    return result    