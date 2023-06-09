from sklearn.cluster import KMeans

# Assuming you have the pivot_table representing the user-item matrix

# Perform k-means clustering on the tracks
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(pivot_table.T)  # Transpose the pivot_table for track clustering

# Assign cluster labels to each track
cluster_labels = kmeans.labels_
pivot_table['cluster_label'] = cluster_labels
def generate_playlist(user_id, num_tracks_per_cluster):
    user_tracks = pivot_table.loc[user_id]
    user_cluster_labels = user_tracks['cluster_label'].unique()
    
    playlist = []
    for cluster_label in user_cluster_labels:
        cluster_tracks = pivot_table[pivot_table['cluster_label'] == cluster_label]
        cluster_tracks_sorted = cluster_tracks.sort_values(by=user_id, ascending=False)
        top_tracks = cluster_tracks_sorted.index[:num_tracks_per_cluster].tolist()
        playlist.extend(top_tracks)
    
    return playlist
