import langchain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4")


template = PromptTemplate(
    template="Generate 10 lines about {topic}",
    input=["topic"]
)

template2 = PromptTemplate(
    template="Generate 4 lines summpary from the following text \n {text}",
    input=["text"]
)


parser = StrOutputParser()
chain = template | model | parser | template2| model | parser 
result = chain.invoke({"topic: Pollution in India"})
print(result)

chain.get_graph().print_ascii()
