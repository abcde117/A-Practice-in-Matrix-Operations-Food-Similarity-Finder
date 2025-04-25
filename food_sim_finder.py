import pandas as pd
import numpy as np
from scipy.spatial import distance

# Cosine similarity function
def cosine_similarity(x, y):
    return np.dot(x.T, y)[0][0] / (np.linalg.norm(x) * np.linalg.norm(y))

# Convert a row to column vector
def to_column_vector(row):
    return row.values.reshape(-1, 1)

# Function to get similarity ranking by cosine similarity
def get_cosine_similarity_ranking(df, query_item):
    input_vector = to_column_vector(df.loc[query_item])
    similarities = []
    for item_name in df.index:
        if item_name == query_item:
            similarities.append(0)
        else:
            vector = to_column_vector(df.loc[item_name])
            sim = cosine_similarity(input_vector, vector)
            similarities.append(sim)
    ranking = pd.DataFrame(similarities, index=df.index, columns=["cosine_similarity"])
    return ranking.sort_values("cosine_similarity", ascending=False)

# Function to get similarity ranking by Euclidean distance
def get_euclidean_distance_ranking(df, query_item):
    input_vector = to_column_vector(df.loc[query_item])
    distances = []
    for item_name in df.index:
        if item_name == query_item:
            distances.append(np.inf)
        else:
            vector = to_column_vector(df.loc[item_name])
            dist = distance.euclidean(input_vector, vector)
            distances.append(dist)
    ranking = pd.DataFrame(distances, index=df.index, columns=["euclidean_distance"])
    return ranking.sort_values("euclidean_distance")

# Example loading and usage (replace with your actual file path)
df = pd.read_csv('your_food_data.csv')
df = df.iloc[:, 1:]  # Skip the first unnamed column if needed
df = df.set_index('料理名')

# Example query
query_item = 'バター（小さじ1）'
print(get_cosine_similarity_ranking(df, query_item).head())
print(get_euclidean_distance_ranking(df, query_item).head())
