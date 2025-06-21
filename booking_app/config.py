import os
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = 'HS256'
ACCESS_TOKEN_LIFETIME = 30
REFRESH_TOKEN_LIFETIME = 3


class Social:
    GITHUB_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID')
    GITHUB_KEY = os.getenv('GITHUB_KEY')
    GITHUB_URL = os.getenv('GITHUB_URL')
    GOOGLE_URL = os.getenv('GOOGLE_URL')
    GOOGLE_KEY = os.getenv('GOOGLE_KEY')
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')

social = Social()