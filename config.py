import os


class Config:
  '''
  General configuration parent class
  '''
  NEWS_API_BASE_URL = ''
  ARTICLES_API_BASE_URL = ''
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  SECRET_KEY = os.environ.get('SECRET_KEY')

class DevConfig(Config):
  '''
  Development configuration child class
  
  Args:
    Config: The Parent configuration class with general config settings
  '''
  DEBUG = True


class ProdConfig(Config):
  '''
  Production configuration child class

  Args:
    Config: The Parent configuration class with general config settings
  '''
  pass


config_options = {
'development':DevConfig,
'production':ProdConfig
}