import os

class Config:
    '''
    General configuration parent class
    '''
   
    HEADLINES_API  = "https://newsapi.org/v2/top-headlines?country=us&country=gb&country=au&apiKey={}"
    SOURCES_API = "https://newsapi.org/v2/sources?language=en&category={}&apiKey={}"
    SOURCES_ARTICLE_API = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}"
    SEARCH_API = "https://newsapi.org/v2/everything?q={}&apiKey={}"
    API_BASE_URL = 'https://newsapi.org/v1/articles?source={}&apiKey={}'
    NEWS_ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    API_KEY = os.environ.get("API_KEY")
    SECRET_KEY = os.environ.get('SECRET_KEY')



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}