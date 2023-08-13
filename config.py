import os
from dotenv import load_dotenv

baseDir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(baseDir, '.env'))

class Config(object):
    OPEN_AI_KEY = 'some_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", '') or \
        'sqlite:///' + os.path.join(baseDir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = 'some_path'
    LANGUAGES = ['en', 'fr']
    REQUESTS_PER_PAGE = 25
