from sklearn.metrics.pairwise import cosine_similarity

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
