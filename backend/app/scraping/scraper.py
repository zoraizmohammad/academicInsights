import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract text, images, and multimedia elements
        text = soup.get_text()
        images = len(soup.find_all("img"))
        videos = len(soup.find_all("video"))
        audio = len(soup.find_all("audio"))
        
        return {
            "url": url,
            "text": text,
            "images": images,
            "videos": videos,
            "audio": audio
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
