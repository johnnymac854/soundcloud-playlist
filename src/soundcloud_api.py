# soundcloud_api.py

import requests
import json
from config import get_oauth_token, logger

API_BASE_URL = 'https://api.soundcloud.com'

class SoundCloudAPI:
    def __init__(self):
        self.oauth_token = get_oauth_token()
        self.headers = {
            'Authorization': f'OAuth {self.oauth_token}',
            'Content-Type': 'application/json'
        }
        logger.info("Initialized SoundCloudAPI with provided OAuth token.")

    def get_playlist(self, playlist_id):
        logger.info(f"Fetching playlist with ID: {playlist_id}")
        url = f"{API_BASE_URL}/playlists/{playlist_id}"
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            logger.error(f"Failed to fetch playlist: {response.status_code} - {response.text}")
            raise Exception(f"Failed to fetch playlist: {response.status_code} - {response.text}")
        logger.info("Playlist fetched successfully.")
        return response.json()

    def create_playlist(self, title, track_uris):
        logger.info(f"Creating new playlist titled: {title}")
        url = f"{API_BASE_URL}/playlists"
        data = {
            'playlist': {
                'title': title,
                'tracks': [{'uri': uri} for uri in track_uris]
            }
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(data))
        if response.status_code not in [200, 201]:
            logger.error(f"Failed to create playlist: {response.status_code} - {response.text}")
            raise Exception(f"Failed to create playlist: {response.status_code} - {response.text}")
        logger.info("Playlist created successfully.")
        return response.json()
