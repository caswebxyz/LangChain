import langchain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate,FewShotPromptTemplate
#from langchain.prompts import PromptTemplate,ChatPromptTemplate,FewShotPromptTemplate
#- This is also alternative way to do

load_dotenv()
#Creating Prompt Template
#PromptTemplate.from_template - This is also alternative way to do

whichlang = input("Enter to which language it should translate to")
msg = input("Enter Text to translate from English")

prompt = PromptTemplate(
    template="Translate following Sentence to {language_to_translate} \n: {sentence}",
    input_variables=["sentence","language_to_translate"]
)



input_prompt = prompt.format(sentence=msg,
                             language_to_translate=whichlang)
print(input_prompt)

model = ChatOpenAI(model="gpt-4")
res = model.invoke(input_prompt)
print(res.content) #मस्ते दोस्तों, आप कैसे हैं'