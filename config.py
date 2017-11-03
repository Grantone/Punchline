import os


class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://granton:granton@localhost/categories'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    # 'test':TestConfig
}
