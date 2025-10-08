import langchain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()
parser = JsonOutputParser()

template1 = PromptTemplate(
    template = "Give me 5 facts about {topic} \n {format_instrution}",
    input_variables=["topic"],
    partial_variables = {"format_instrution" : parser.get_format_instructions()}
)

Chain = template1 | model | parser
res = Chain.invoke({"topic" : "Challagulla Srinivasa Kumar"})
print(res)