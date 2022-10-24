class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    #Elephantsql
    SQLALCHEMY_DATABASE_URI = 'postgresql://vtaifebm:n7H7mbTD6J2w1lxFdbKwBHY206tmvCAe@peanut.db.elephantsql.com:5432/vtaifebm'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/posts'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
}
