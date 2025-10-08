import langchain
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

schema = [
    ResponseSchema(name="fact_1",description="Fact 1 about Topic"),
    ResponseSchema(name="fact_2",description="Fact 2 about Topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)


template = PromptTemplate(
    template="Give 3 facts about {topic}, \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

prompt = template.invoke({"topic":"Indian Ocean"})

res = model.invoke(prompt)

final_result = parser.parse(res.content)

print(final_result)