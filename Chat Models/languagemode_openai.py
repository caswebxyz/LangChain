from langchain_openai import ChatOpenAI, OpenAI
from dotenv import load_dotenv
load_dotenv()
print("11111")

model = OpenAI(model = "gpt-3.5-turbo-instruct")

result = model.invoke("Explain India Flag Colurs")

print(result)

