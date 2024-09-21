# Configuration

Proper configuration is essential for the application to function correctly.

### 1. Obtain Your OAuth Token

**Important:** The OAuth token grants access to your SoundCloud account's resources. Handle it securely and never share it publicly.

- **Note:** Due to recent changes, SoundCloud may no longer support traditional developer registration. If you've obtained your OAuth token through alternative means (e.g., network inspection as advised by SoundCloud support), ensure you comply with SoundCloud's [Terms of Service](https://soundcloud.com/terms-of-use) and [Developer Guidelines](https://developers.soundcloud.com/docs/api/guide).

### 2. Set Up Environment Variables

Create a `.env` file in the project root directory to store your OAuth token securely.

```bash
touch .env
```

Open the `.env` file in a text editor and add your OAuth token:

```dotenv
SOUNDCLOUD_OAUTH_TOKEN=your_extracted_oauth_token_here
```

**⚠️ Security Notice:**

- **Never** commit the `.env` file to version control. Ensure it's listed in `.gitignore`:

  ```bash
  echo ".env" >> .gitignore
  ```

- **Protect Your OAuth Token:** Treat the `.env` file with the same confidentiality as your passwords.

---