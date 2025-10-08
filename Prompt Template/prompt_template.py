import langchain
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4")

res = llm.invoke("Translate following sentence into Telugu Language \n Hi All How are You")
print(res)
#హాయ్ అందరికీ, మీరు ఎలా ఉన్నారు?