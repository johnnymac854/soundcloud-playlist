# SoundCloud Playlist Duplicator

![SoundCloud Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/SoundCloud_logo.svg/512px-SoundCloud_logo.svg.png)

**SoundCloud Playlist Duplicator** is a Python-based tool designed to duplicate existing SoundCloud playlists. By leveraging the SoundCloud API, this application allows users to effortlessly create a new playlist containing all tracks from a specified existing playlist.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Obtaining the OAuth Token](#obtaining-the-oauth-token)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Operating System:** Windows, macOS, or Linux.
- **Python:** Python 3.6 or higher installed on your machine.
- **SoundCloud Account:** An active SoundCloud account with access to the playlists you wish to duplicate.
- **OAuth Token:** A valid SoundCloud OAuth token with the necessary permissions.

---

## Installation

For detailed installation instructions, please refer to the [Installation Guide](doc/installation.md).

---

## Configuration

For detailed configuration instructions, please refer to the [Configuration Guide](doc/configuration.md).

---

## Usage

Once installation and configuration are complete, you can use the application to duplicate SoundCloud playlists.

### Running the Application

Execute the `main.py` script using Python:

```bash
python main.py
```

### Step-by-Step Guide

1. **Start the Application:**

   ```bash
   python main.py
   ```

2. **Enter Playlist ID or URL:**

   When prompted, input the **ID** or **URL** of the existing SoundCloud playlist you wish to duplicate.

   - **Example ID:** `123456789`
   - **Example URL:** `https://soundcloud.com/user/sets/playlist-name`

3. **Enter New Playlist Title:**

   Provide a desired name for the new duplicated playlist.

4. **Completion:**

   Upon successful execution, the application will display the URL of the newly created playlist.

   ```
   === SoundCloud Playlist Duplicator ===

   Enter the ID or URL of the existing playlist you want to duplicate: https://soundcloud.com/user/sets/playlist-name
   Resolving playlist URL to obtain ID...
   Fetching tracks from playlist ID: 123456789
   Found 25 tracks. Creating new playlist titled 'My Duplicated Playlist'...

   New playlist created successfully! You can view it here: https://soundcloud.com/user/sets/my-duplicated-playlist
   ```
---

## Obtaining the OAuth Token

For detailed instructions on obtaining your OAuth Token, please refer to the [OAuth Token doc](doc/oauth_token.md).

---

## Troubleshooting

### Common Issues and Solutions

1. **OAuth Token Not Found:**

   - **Error Message:** `ValueError: OAuth token not found. Please set SOUNDCLOUD_OAUTH_TOKEN in your .env file.`
   - **Solution:** Ensure that the `.env` file exists in the project root and contains the `SOUNDCLOUD_OAUTH_TOKEN` variable with a valid token.

2. **Invalid Playlist ID or URL:**

   - **Error Message:** `Exception: Failed to resolve playlist URL: 404 - Not Found`
   - **Solution:** Verify that the playlist ID or URL entered is correct and that the playlist exists.

3. **API Rate Limits Exceeded:**

   - **Error Message:** `Exception: Failed to fetch playlist: 429 - Too Many Requests`
   - **Solution:** Wait for a while before retrying. Implement exponential backoff in the script for handling rate limits.

4. **Failed to Create Playlist:**

   - **Error Message:** `Exception: Failed to create playlist: 403 - Forbidden`
   - **Solution:** Check if the OAuth token has the necessary permissions. Ensure that the new playlist title is valid and doesn't violate SoundCloud's policies.

5. **Network Issues:**

   - **Error Message:** `requests.exceptions.ConnectionError: ...`
   - **Solution:** Verify your internet connection and ensure that SoundCloud's API is reachable.

### Logging

Check the `app.log` file (if logging to a file is configured) for detailed error messages and stack traces to assist in debugging.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- **SoundCloud API:** For providing the necessary endpoints to interact with playlists.
- **Python Community:** For the extensive libraries and tools that make projects like this possible.
- **OpenAI:** For assisting in the development and structuring of this project.

---

**Disclaimer:** This tool is intended for personal use. Ensure that you have the right to duplicate any playlists and that your actions comply with SoundCloud's [Terms of Service](https://soundcloud.com/terms-of-use) and [Developer Guidelines](https://developers.soundcloud.com/docs/api/guide).

---

*Happy playlist duplicating! 🎶*

---