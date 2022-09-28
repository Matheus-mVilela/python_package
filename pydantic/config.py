from os import environ
from pydantic import BaseSettings, Field, BaseModel
from typing import Literal, Union
import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())

class ConfigTest(BaseSettings):
    mongo_url: str = Field(env='mongo_url')

class ConfigTest(BaseSettings):
    mongo_url: str

    class Config:
        env_prefix = 'TEST_'

class ConfigDev(BaseSettings):
    mongo_url: str

    class Config:
        env_prefix = 'DEV_'

class ConfigProd(BaseSettings):
    mongo_url: str

    class Config:
        env_prefix = 'PROD_'


class ConfigTest(BaseSettings):
    env: Literal['test']    
    mongo_url: str = 'http//testmongourl'


class ConfigDev(BaseSettings):
    env: Literal['dev']    
    mongo_url: str = 'http//devmongourl'

class ConfigProd(BaseSettings):
    env: Literal['prod']    
    mongo_url: str = 'http//prodmongourl' 


class Config(BaseModel):
    config: Union[ConfigTest, ConfigDev, ConfigProd]
