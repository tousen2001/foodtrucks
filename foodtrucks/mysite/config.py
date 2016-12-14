class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_POOL_RECYCLE = 250
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass

    def __init__(self):
        pass


class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1:3306/mydb?charset=utf8'


class LocalConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1:3306/mydb?charset=utf8'


config = {
    'production': ProductionConfig,
    'local' : LocalConfig
}
