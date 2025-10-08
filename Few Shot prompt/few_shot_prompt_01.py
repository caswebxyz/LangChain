import langchain
from langchain_openai import OpenAI,ChatOpenAI
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from dotenv import load_dotenv

load_dotenv()

examples = [
    {    "text":"I love this mode","label": "Positive"   },
    {    "text":"This is the worst thing i have seen","label": "Negative"   },
    {    "text":"It was okay, not so great but not bad","label": "Neutral"   },
    
]

promt_tmp = PromptTemplate(
    template = "Review: {text}\n Sentiment : {label}",
    input_variables = ["text","label"]
)

few_shot_prompt = FewShotPromptTemplate(
    examples = examples,
    example_prompt = promt_tmp,
    prefix = "Act as a Sentiment Classification Assistant, based on example please clarify provided Inputs",
    suffix = "Review : {text}\n Sentiment",
    input_variables=["text"]
)

input_prompt = few_shot_prompt.format(text="This Product exceeds my expectations")
print(input_prompt)

llm = ChatOpenAI(model="gpt-4")
res= llm.invoke(input_prompt)
print(res)