SQLALCHEMY_DATABASE_URI = "postgresql://postgres:12345678@localhost:5432/late_show_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

class Config(object):
    """Base config class"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'thisisasecretkey'


class ProductionConfig(Config):
    """Production config class"""
    pass


class DevelopmentConfig(Config):
    """Development config class"""
    DEBUG = True


class TestingConfig(Config):
    """Testing config class"""
    TESTING = True
