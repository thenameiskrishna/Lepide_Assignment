import os

class Config:
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
