import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")