class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    ARTICLE_NEWS_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    DEBUG = True