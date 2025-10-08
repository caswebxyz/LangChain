import langchain
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()
parser = JsonOutputParser()
template = PromptTemplate(
    template="Create a Json Character for a {role} in a {genre} story, \n {format_instruction}",
    input_variables=["role","genre"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template | model | parser
res = chain.invoke({"role":"detective","genre":"mystery"})
print(res)