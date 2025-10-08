import langchain
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from bs4 import BeautifulSoup
load_dotenv()

url = "https://www.flipkart.com/apple-macbook-air-m2-8-gb-512-gb-ssd-mac-os-monterey-mly43hn-a/p/itmdc5308fa78421?pid=COMGFB2GDBDYXF9D&lid=LSTCOMGFB2GDBDYXF9DPTKNCZ&marketplace=FLIPKART&q=apple+macbook+m2&store=6bo%2Fb5g&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_19_sc_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_19_sc_na_na&fm=organic&iid=fc1df87b-abc5-41cd-9790-11572da4407a.COMGFB2GDBDYXF9D.SEARCH&ppt=clp&ppn=dussehra-offers-store&ssid=2669wg4ibk0000001759666648896&qH=cb577c6dd09ac998"

loader = WebBaseLoader(url)
docs = loader.load()
print(docs[0])
# docs
print(docs)
# print(type(docs))
# print(len(docs))
llm = ChatOpenAI()

prompt = PromptTemplate(
    template="Answer the following question \n {question} from the text : \n {text}",
    input_variables=["question","text"]
)

parser = StrOutputParser()
chain = prompt | llm | parser

results = chain.invoke({
    "question": "what is the product",
    "text": docs[0]
    })
print("<<<<<<<<<<<<<<<<<<<<<<====================================================================================================>>>>>>>>>>>")
print(results)

