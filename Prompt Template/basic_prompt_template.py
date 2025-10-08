import langchain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate,FewShotPromptTemplate
#from langchain.prompts import PromptTemplate,ChatPromptTemplate,FewShotPromptTemplate
#- This is also alternative way to do

load_dotenv()
#Creating Prompt Template
#PromptTemplate.from_template - This is also alternative way to do

prompt = PromptTemplate(
    template="Translate following Sentence to Hindi \n: {sentence}",
    input_variables=["sentence"]
)

input_prompt = prompt.format(sentence="Hello Friends, How are you")
print(input_prompt)

model = ChatOpenAI(model="gpt-4")
res = model.invoke(input_prompt)
print(res.content) #मस्ते दोस्तों, आप कैसे हैं'