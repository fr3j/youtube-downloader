import yt_dlp
import os

def download_videos(link_file, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the links from the file
    with open(link_file, 'r') as file:
        links = file.readlines()
    
    # Strip any extra whitespace characters from the links
    links = [link.strip() for link in links]

    # Define download options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Best video and audio quality
        'merge_output_format': 'mkv',  # Merge video and audio into mkv
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Save files in the specified folder
    }

    # Initialize the downloader
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download each video
        for link in links:
            if link:  # Check if the link is not empty
                print(f"Downloading {link}...")
                ydl.download([link])
                print(f"Downloaded {link}.")

if __name__ == "__main__":
    link_file = 'links.txt'  # Path to your file with YouTube links
    output_folder = 'downloaded_videos'  # Folder to save the downloaded files
    download_videos(link_file, output_folder)
