import langchain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4")

template = PromptTemplate(
    template="Generate 2 lines about {topic}",
    input=["topic"]
)

parser = StrOutputParser()
chain = template | model | parser
result = chain.invoke({"topic: Diwali"})
print(result)

chain.get_graph().print_ascii()
