# Assuming you have merged user_data and music_data into the user_item_matrix DataFrame

# Convert the user-item matrix to a pivot table
pivot_table = user_item_matrix.pivot_table(values='play_count', index='user_id', columns='track_id', fill_value=0)
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Assuming you have the pivot_table representing the user-item matrix

# Calculate the similarity matrix using cosine similarity
similarity_matrix = cosine_similarity(pivot_table)

def get_similar_users(user_id, k):
    user_index = pivot_table.index.get_loc(user_id)
    similar_users_indices = np.argsort(similarity_matrix[user_index])[::-1][1:k+1]
    similar_users = pivot_table.iloc[similar_users_indices].index
    return similar_users

def recommend_music_collaborative(user_id, k):
    similar_users = get_similar_users(user_id, k)
    user_tracks = pivot_table.loc[user_id]
    
    recommended_tracks = []
    for track_id in user_tracks.index:
        if user_tracks[track_id] == 0:
            for user in similar_users:
                if pivot_table.loc[user, track_id] > 0:
                    recommended_tracks.append(track_id)
                    break
    
    return recommended_tracks
