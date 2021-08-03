import os


class Settings():
    is_test = False
    connectionstring: str = os.environ.get('DATABASE_CONNECTIONSTRING', '')
    #os.environ['DATABASE_CONNECTIONSTRING']    

settings = Settings()