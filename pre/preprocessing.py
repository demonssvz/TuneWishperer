import pandas as pd

# Assuming you have retrieved user data and music metadata from your data sources

# Create user_data DataFrame
user_data = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5],
    'track_id': [101, 102, 103, 104, 105],
    'play_count': [5, 3, 7, 2, 4],
    'genre': ['Rock', 'Pop', 'Electronic', 'Hip Hop', 'Jazz'],
    'artist': ['Led Zeppelin', 'Taylor Swift', 'Daft Punk', 'Kendrick Lamar', 'Miles Davis']
})

# Create music_data DataFrame
music_data = pd.DataFrame({
    'track_id': [101, 102, 103, 104, 105],
    'genre': ['Rock', 'Pop', 'Electronic', 'Hip Hop', 'Jazz'],
    'artist': ['Led Zeppelin', 'Taylor Swift', 'Daft Punk', 'Kendrick Lamar', 'Miles Davis'],
    'album': ['Led Zeppelin IV', '1989', 'Random Access Memories', 'To Pimp a Butterfly', 'Kind of Blue']
})
