from langchain.chat_models import init_chat_model
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

class Model:
    def __init__(self, model_name="Gemini", url = None, api = None):
        if model_name == "Gemini":
            self.llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0.2)
        else:
            self.llm = init_chat_model(model=model_name, temperature=0.2)

    def inference(self, prompt):
        try:
            text_ = self.llm.invoke(input=prompt).content[0]['text']
            return text_
        except Exception as e:
            print(e)
            return None