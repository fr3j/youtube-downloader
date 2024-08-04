import requests
from bs4 import BeautifulSoup
import os

# List of podcast URLs
podcast_urls = [
    "https://eagleman.com/podcast/why-do-brains-love-conspiracy-theories/",
    # Add more podcast URLs here
]

# Directory to save the downloaded podcasts
save_dir = "podcasts"
os.makedirs(save_dir, exist_ok=True)

def download_podcast(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the audio file link in the webpage
    audio_tag = soup.find('audio')
    if not audio_tag:
        print(f"No audio tag found on {url}")
        return
    
    audio_src = audio_tag.get('src')
    if not audio_src:
        print(f"No src attribute found in audio tag on {url}")
        return
    
    # Get the audio file name from the URL
    file_name = os.path.basename(audio_src)
    file_path = os.path.join(save_dir, file_name)
    
    # Download the audio file
    audio_response = requests.get(audio_src, stream=True)
    if audio_response.status_code == 200:
        with open(file_path, 'wb') as f:
            for chunk in audio_response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded {file_name} from {url}")
    else:
        print(f"Failed to download audio from {audio_src}")

# Download each podcast
for url in podcast_urls:
    download_podcast(url)
