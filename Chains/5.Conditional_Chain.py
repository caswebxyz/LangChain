import langchain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda

from dotenv import load_dotenv

load_dotenv()

model1 = ChatOpenAI()
model2 = ChatOpenAI(model="gpt-4")

parser = StrOutputParser()


prompt1 = PromptTemplate(
    template="Classify the sentiment into positive or negative feedback \n {feedback}",
    input=["feedback"]
)

chain = prompt1 | model1 | parser
result = chain.invoke({"feedback":"Asus not a good model"})
print(result)
