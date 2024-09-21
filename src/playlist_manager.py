# playlist_manager.py

import requests
from soundcloud_api import SoundCloudAPI
from config import logger

class PlaylistManager:
    def __init__(self):
        self.api = SoundCloudAPI()
        self.API_BASE_URL = 'https://api.soundcloud.com'  # Ensure consistent usage
        logger.info("Initialized PlaylistManager.")

    def fetch_track_uris(self, playlist_id):
        logger.info(f"Fetching track URIs from playlist ID: {playlist_id}")
        playlist = self.api.get_playlist(playlist_id)
        tracks = playlist.get('tracks', [])
        if not tracks:
            logger.warning("No tracks found in the specified playlist.")
            return []
        track_uris = [track['uri'] for track in tracks]
        logger.info(f"Retrieved {len(track_uris)} track URIs.")
        return track_uris

    def duplicate_playlist(self, existing_playlist_id, new_playlist_title):
        logger.info(f"Starting duplication of playlist ID: {existing_playlist_id}")
        track_uris = self.fetch_track_uris(existing_playlist_id)
        if not track_uris:
            logger.error("Cannot duplicate an empty playlist.")
            raise Exception("Cannot duplicate an empty playlist.")
        logger.info(f"Creating new playlist titled '{new_playlist_title}' with {len(track_uris)} tracks.")
        new_playlist = self.api.create_playlist(new_playlist_title, track_uris)
        new_playlist_url = new_playlist.get('permalink_url')
        logger.info(f"New playlist created at: {new_playlist_url}")
        return new_playlist_url

    def resolve_playlist_id(self, playlist_url):
        """
        Resolves the numeric playlist ID from a SoundCloud playlist URL.
        """
        logger.info(f"Resolving playlist URL: {playlist_url}")
        resolve_endpoint = f"{self.API_BASE_URL}/resolve"
        params = {
            'url': playlist_url
        }
        response = requests.get(resolve_endpoint, headers=self.api.headers, params=params)
        if response.status_code != 200:
            logger.error(f"Failed to resolve playlist URL: {response.status_code} - {response.text}")
            raise Exception(f"Failed to resolve playlist URL: {response.status_code} - {response.text}")
        playlist = response.json()
        playlist_id = playlist.get('id')
        if not playlist_id:
            logger.error("Playlist ID could not be resolved from the provided URL.")
            raise Exception("Playlist ID could not be resolved from the provided URL.")
        logger.info(f"Resolved playlist ID: {playlist_id}")
        return playlist_id
