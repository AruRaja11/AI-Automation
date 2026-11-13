from dotenv import load_dotenv
import os

load_dotenv()

class GetSettings:
    OPENAI_KEY : str = os.getenv("OPENAI_API_KEY")
    