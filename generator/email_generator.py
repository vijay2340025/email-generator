from langchain.chat_models import init_chat_model
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

class Model:
    def __init__(self, model_name="Gemini", base_url=None, api_key=None):
        self.model_name = model_name
        if model_name == "Gemini":
            self.llm = ChatGoogleGenerativeAI(
                model="gemini-3.1-flash-lite",
                temperature=0.2,
            )
        else:
            print(f"{base_url}: {model_name} | {api_key}")
            self.llm = init_chat_model(
                model=model_name,
                temperature=0.2,
                base_url=base_url,
                max_tokens=4096,
                api_key=api_key,
            )

    def inference(self, prompt):
        try:
            if self.model_name == "Gemini":
                text_ = self.llm.invoke(input=prompt).content[0]['text']
                return text_
            else:
                text_ = self.llm.invoke(input=prompt)
                print(text_)
                return text_.content
        except Exception as e:
            print(e)
            return None