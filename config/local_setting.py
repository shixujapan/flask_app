# ローカル環境
from config.base_setting import *
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI="mysql://{user}:{password}@{host}/flask".format(**{
    'user': 'root',
    'password': '',
    'host':'localhost'
})
SECRET_KEY="678910"