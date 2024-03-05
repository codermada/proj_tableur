class Config:
    DEBUG = True
    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    SECRET_KEY = 'dbwlifgwelblirev2134431@#$@##'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'

config = {
    'devConf': DevConfig,
    'default': Config
}