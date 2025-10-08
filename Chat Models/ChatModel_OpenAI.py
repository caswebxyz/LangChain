from langchain_openai import ChatOpenAI, OpenAI
from dotenv import load_dotenv
load_dotenv()
print("222")

chatmodel = ChatOpenAI(model = "gpt-4-turbo")

result = chatmodel.invoke("What is Speed of Earth")

print(result)

