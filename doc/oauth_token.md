# Obtaining the OAuth Token

**Disclaimer:** Extracting the OAuth token via network inspection is not the standard or recommended method. Ensure you have explicit permission from SoundCloud and comply with their [Terms of Service](https://soundcloud.com/terms-of-use).

## Steps to Extract OAuth Token via Browser's Developer Tools

1. **Log In to SoundCloud:**

   Navigate to [SoundCloud](https://soundcloud.com/) and log in to your account.

2. **Open Developer Tools:**

   - **Google Chrome:** Press `Ctrl + Shift + I` (Windows/Linux) or `Cmd + Option + I` (Mac), or right-click anywhere on the page and select **"Inspect"**.
   - **Mozilla Firefox:** Press `Ctrl + Shift + I` (Windows/Linux) or `Cmd + Option + I` (Mac), or right-click and select **"Inspect Element"**.
   - **Microsoft Edge:** Similar to Chrome, press `Ctrl + Shift + I` or right-click and choose **"Inspect"**.

3. **Navigate to the Network Tab:**

   Within Developer Tools, click on the **"Network"** tab to monitor all network requests.

4. **Filter Requests:**

   Use the filter box to search for terms like `oauth`, `access_token`, or `authorization`.

5. **Identify OAuth Token:**

   - Look for requests made to endpoints like `https://api.soundcloud.com/...`.
   - Inspect request headers for entries like `Authorization: Bearer YOUR_OAUTH_TOKEN`.
   - Alternatively, check response bodies of relevant API calls for token information.

6. **Copy the OAuth Token:**

   Once located, carefully copy the entire OAuth token string.

7. **Store Securely:**

   Paste the token into the `.env` file as instructed in the [Configuration](#configuration) section.

---

## Security Considerations

- **Protect Your OAuth Token:**
  - **Never** share your OAuth token publicly.
  - **Do not** commit the `.env` file to version control.
  - Use environment variables or secret managers to store sensitive information.

- **Compliance:**
  - Ensure that extracting and using the OAuth token complies with SoundCloud's [Terms of Service](https://soundcloud.com/terms-of-use).
  - Unauthorized extraction or misuse of credentials can lead to account suspension or legal consequences.

- **Token Scope and Expiration:**
  - Be aware of the permissions granted by your OAuth token.
  - Monitor token validity and renew if necessary.
