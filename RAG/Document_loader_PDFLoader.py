import langchain
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv()


loader = PyPDFLoader("C:/Users/srini/Downloads/uncharter.pdf")
docs = loader.load()
print(docs[0])
# docs
print(docs)
# print(type(docs))
# print(len(docs))
# llm = ChatOpenAI()

# prompt = PromptTemplate(
#     template="Write a summary for the following poem : \n {poem}",
#     input_variables=["poem"]
# )

# parser = StrOutputParser()
# chain = prompt | llm | parser

# results = chain.invoke({"poem": docs[0].page_content})

# print(results)

