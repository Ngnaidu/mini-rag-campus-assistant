# import os
# from dotenv import load_dotenv

# load_dotenv()

# class Settings:
#     LLM_API_KEY = os.getenv("LLM_API_KEY")
#     EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
#     CHAT_MODEL = "gpt-4o-mini"
#     VECTOR_STORE_DIR = "data/vector_store"
#     TOP_K = 3

# settings = Settings()
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    LLM_API_KEY = os.getenv("LLM_API_KEY")
    CHAT_MODEL = "gpt-4o-mini"

settings = Settings()

print("Loaded API KEY:", settings.LLM_API_KEY)