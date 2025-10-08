import langchain
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_openai import OpenAI,ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

class Person(BaseModel):
    name : str = Field(description="Name of the Person")
    age : int = Field(gt=18, description =  "Age of the Person")
    city: str = Field(description="Name of the city to which this person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate name,age,city of a {origin} person, \n {format_instruction}",
    input_variables=["origin"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template | model | parser
final_result = chain.invoke({"origin": "indian"})
print(final_result)