from .common import *

STATICFILES_STORAGE = 'orly.storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'orly.storages.MediaStorage'

AZURE_ACCOUNT_NAME = os.environ['AZURE_ACCOUNT_NAME']   # 환경변수에서 읽어 옴
AZURE_ACCOUNT_KEY = os.environ['AZURE_ACCOUNT_KEY']     # 환경변수에서 읽어 옴
AZURE_SSL = True
