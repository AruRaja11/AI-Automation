from langchain_openai import ChatOpenAI
from core.config import GetSettings
import os 


class AIServices:
    def __init__(self):
        self.model = "gpt-5-nano"

        self.llm = ChatOpenAI(
            model=self.model,
            api_key=GetSettings.OPENAI_KEY,
            max_completion_tokens=500,
            max_retries=1,
            timeout=30
        )


    def ai_response(self, query:str):
        try:
            response = self.llm.invoke(query)

            return {
                'response': response
            }

        except Exception as e:
            return {
                "response": "something went wrong"
            }