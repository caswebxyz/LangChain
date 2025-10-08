import langchain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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

res1 = prompt1.invoke({"topic":"Black hole"})
print(res1)
result = model.invoke(res1)
print(result.content)

resp2 = prompt2.invoke({"text":result.content})

result2 = model.invoke(resp2)
print(result2)