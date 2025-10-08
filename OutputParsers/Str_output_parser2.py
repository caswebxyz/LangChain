import langchain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

# Prompt1 for Task 1
prompt1 = PromptTemplate(
    template="Write a detailed template report on {topic} less than 15 lines",
    input_variables = ["topic"]
)

#Prompt2 for Task 2
prompt2 = PromptTemplate(
    template="Write a 5 lines summary  on text \n {text}",
    input_variables = ["text"]
)

parser = StrOutputParser()

Chain = prompt1 | model | parser | prompt2 | model | parser

res = Chain.invoke({"topic":"BlackHole"})
print(res)