import os

from dotenv import load_dotenv

load_dotenv()
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_URL = os.environ.get('DB_URL')
TEST_DB_NAME = os.environ.get('TEST_DB_NAME')
DJANGO_KEY = os.environ.get('DJANGO_KEY')
