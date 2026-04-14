import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

BASE_BRANCH = os.getenv("BASE_BRANCH", "main")
MAX_FILES = int(os.getenv("MAX_FILES", "50"))
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", "20000"))
