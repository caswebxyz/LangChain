import langchain
from langchain_core.tools import tool
from langchain_openai import OpenAI,ChatOpenAI
import requests
from dotenv import load_dotenv
load_dotenv()
@tool
def multipy(a:int, b:int) -> int:
    """tool mul"""
    return a * b

a = multipy.invoke({"a":11,"b":22})
print(a)

llm = ChatOpenAI()

llm_tools = llm.bind_tools([multipy])
print(llm_tools)
res = llm_tools.invoke("Hi ge how are u")
print("=======================================================================")
print("res===>>>>",res.content)