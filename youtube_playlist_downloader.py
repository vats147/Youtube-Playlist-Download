

from pytube import Playlist

# Define the URL of the YouTube playlist
playlist_url = "https://www.youtube.com/watch?v=7Dh73z3icd8&list=PLu0W_9lII9aiXlHcLx-mDH1Qul38wD3aR"


# Create a Playlist object
playlist = Playlist(playlist_url)

# Iterate over each video in the playlist
for video in playlist.videos:
    # Print the video title
    print("Downloading:", video.title)

    # Download the video
    video.streams.get_highest_resolution().download(output_path="path/to/save/videos")

print("Download complete!")
