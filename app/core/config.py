from app.core.logging import logger

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    try:
        # env
        POSTGRES_USER = os.environ["POSTGRES_USER"]
        POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
        POSTGRES_DB = os.environ["POSTGRES_DB"]
        DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}"
        
        # Local AD
        SERVER_NAME = os.environ["SERVER_NAME"]
        USER = os.environ["USER"]
        PASSWORD = os.environ["PASSWORD"]


        # no env
        LEN_PASS = 8
    except Exception as e:
        logger.critical(f"Змінні оточення {e} не отримано, перевірте файл .env")