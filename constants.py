import os
from dotenv import load_dotenv
load_dotenv()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
DB_HOST = os.getenv('HOST')
DATABASE = os.getenv('DB')
EMPLOYEE = os.getenv('EMPLOYEE')
ORGANISATION = os.getenv('ORGANISATION')
ROLES = os.getenv('ROLES')
PRIVATE_KEY = os.getenv('SECRET_KEY')