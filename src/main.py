# main.py

from playlist_manager import PlaylistManager
from config import logger

def main():
    print("=== SoundCloud Playlist Duplicator ===\n")
    try:
        existing_playlist_input = input("Enter the ID or URL of the existing playlist you want to duplicate: ").strip()
        
        manager = PlaylistManager()
        
        if existing_playlist_input.startswith('http'):
            logger.info("Playlist input is a URL. Attempting to resolve playlist ID...")
            existing_playlist_id = manager.resolve_playlist_id(existing_playlist_input)
        else:
            existing_playlist_id = existing_playlist_input

        new_playlist_title = input("Enter a title for the new playlist: ").strip()
        if not new_playlist_title:
            raise ValueError("Playlist title cannot be empty.")

        new_playlist_url = manager.duplicate_playlist(existing_playlist_id, new_playlist_title)
        print(f"\nNew playlist created successfully! You can view it here: {new_playlist_url}")
    except NotImplementedError as nie:
        logger.error(nie)
        print(f"Error: {nie}")
    except Exception as e:
        logger.error(e)
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
