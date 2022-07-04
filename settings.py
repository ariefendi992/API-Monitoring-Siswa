import os 
from dotenv import load_dotenv

load_dotenv()
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

class Config:
    # general configuration
    SECRET_KEY = str(os.getenv('secret_key'))

    # mysql configuration
    username = str(os.getenv('db_user'))
    password = str(os.getenv('db_pass'))
    host = str(os.getenv('db_host'))
    database = str(os.getenv('db_name'))

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+ username + ':' + password + '@' + host + '/' + database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # jwt secret key
    JWT_SECRET_KEY = str(os.getenv('jwt_secret_key'))
    # test configuration
    # print(SECRET_KEY)
    # print(username)
    # print(password)
    # print(host)
    # print(database)
