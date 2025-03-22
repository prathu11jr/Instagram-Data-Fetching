import instaloader
import os
import time

USERNAME = "bennonono10"
PASSWORD = "Ben12345678"
SESSION_FILE = f"{USERNAME}.session"

L = instaloader.Instaloader(max_connection_attempts=1, request_timeout=60)

# Attempt to load session; if it doesn't exist, login and save session.
try:
    if os.path.exists(SESSION_FILE):
        L.load_session_from_file(USERNAME, SESSION_FILE)
    else:
        L.login(USERNAME, PASSWORD)
        L.save_session_to_file(SESSION_FILE)
except Exception as e:
    print(f"Login error: {e}")
    exit(1)

# Wait to help prevent rate limiting
time.sleep(10)

try:
    profile = instaloader.Profile.from_username(L.context, "bbcnews")
    latest_post = next(profile.get_posts())
    print("Caption:", latest_post.caption)
    print("Image URL:", latest_post.url)
except Exception as e:
    print(f"Error fetching post: {e}")
