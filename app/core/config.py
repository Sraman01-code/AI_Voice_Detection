from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
MODEL_VERSION = os.getenv("MODEL_VERSION", "v1.0")

