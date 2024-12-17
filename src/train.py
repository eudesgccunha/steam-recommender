import pickle
import numpy as np
from utils import get_ratings, get_steam_data, ItemBasedRecommender

# get data
df = get_steam_data('../data/steam_200k.csv')

# get implicit ratings
df_ratings = get_ratings(df)

# instantiate recommender class
recommender = ItemBasedRecommender(
    data=df_ratings,
    item_col='item_id',
    user_col='user_id',
    score_col='rating',
    aggfunc=np.sum
)

# train recommender
recommender.fit()

# Export model.pkl
with open('models/recommender.pkl', 'wb') as model_file:
    pickle.dump(recommender, model_file)