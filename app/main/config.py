import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'key_ultra_secure')
    DEBUG = False


class DevelopmentConfig(Config):
    #SQLALCHEMY_DATABASE_URI = postgtes_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'basilisk.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'basilisk_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = False


class ProductionConfig(Config):
    DEBUG = False
    #SQLALCHEMY_DATABASE_URI = postgtes_local_base


config_by_name = dict (
    dev = DevelopmentConfig, 
    test = TestingConfig,
    prod = ProductionConfig
)

key = Config.SECRET_KEY