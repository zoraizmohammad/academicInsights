import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "your_secret_key"
    FIREBASE_ADMIN_KEY = "firebase-admin-key.json"
    FIREBASE_PROJECT_ID = "your-firebase-project-id"
