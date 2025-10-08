import langchain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

class Feedback(BaseModel):
    sentiment : Literal["positive","negative"] = Field(description="Give the Sentiment of the Feedback")

# Parser to classify sentiment
parser2 = PydanticOutputParser(pydantic_object=Feedback)

# Sentiment classification prompt
prompt1 = PromptTemplate(
    template="Classify the sentiment into positive or negative feedback \n{feedback}\n{format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser2.get_format_instructions()}
)

# Positive feedback response prompt
prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback:\n{feedback}",
    input_variables=["feedback"]
)

# Negative feedback response prompt
prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback:\n{feedback}",
    input_variables=["feedback"]
)

# LLMs
model1 = ChatOpenAI()
model2 = ChatOpenAI(model="gpt-4")

# For response generation, use string parser
response_parser = StrOutputParser()

# Chain to classify sentiment
classifier_chain = prompt1 | model1 | parser2

# Conditional chain based on sentiment
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model2 | response_parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model1 | response_parser),
    RunnableLambda(lambda x: "Could not determine sentiment.")
)

# Final composed chain
chain = classifier_chain | branch_chain

# Example input
result = chain.invoke({"feedback": "Asus not a good model"})

print(result)
