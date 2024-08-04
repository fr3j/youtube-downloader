import yt_dlp
import os

def download_videos(link_file, output_base_folder):
    # Ensure the base output folder exists
    if not os.path.exists(output_base_folder):
        os.makedirs(output_base_folder)

    # Read the links from the file
    with open(link_file, 'r') as file:
        links = file.readlines()
    
    # Strip any extra whitespace characters from the links
    links = [link.strip() for link in links]

    # Define download options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Best video and audio quality
        'merge_output_format': 'mkv',  # Merge video and audio into mkv
        'outtmpl': os.path.join(output_base_folder, '%(playlist_title)s/%(title)s.%(ext)s'),  # Save files in the specified folder with playlist subfolders
        'noplaylist': False,  # Ensure that playlists are downloaded
    }

    # Initialize the downloader
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download each video or playlist
        for link in links:
            if link:  # Check if the link is not empty
                print(f"Downloading {link}...")
                ydl.download([link])
                print(f"Downloaded {link}.")

if __name__ == "__main__":
    link_file = 'playlist.txt'  # Path to your file with YouTube links
    output_base_folder = 'downloaded_videos'  # Base folder to save the downloaded files
    download_videos(link_file, output_base_folder)
