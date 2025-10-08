import langchain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

from dotenv import load_dotenv

load_dotenv()

model1 = ChatOpenAI()
model2 = ChatOpenAI(model="gpt-4")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text: \n {text}",
    input=["text"]
)

prompt2 = PromptTemplate(
    template="Generate 5 short questions and Answers from the following text \n {text}",
    input=["text"]
)

prompt3 = PromptTemplate(
    template="Merge provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}",
    input=["notes","quiz"]
)

parallel_chain = RunnableParallel(
    {
        "notes" : prompt1 | model1 | parser,
        "quiz" : prompt2 | model1 | parser
    }
)


merge_chain = prompt3 | model1 | parser 

chain = parallel_chain | merge_chain 

text = """A test about Generative AI (GenAI) could refer to evaluating a GenAI model's performance using metrics like accuracy and relevance, or it could be a knowledge-based quiz testing understanding of GenAI concepts and tools, as seen with the ISTQB® CT-GenAI certification. Testing GenAI focuses on quality, ethics, and reliability, addressing challenges like bias and hallucinations through prompt-based testing and continuous monitoring. 
1. For a GenAI Model:Purpose: To assess the quality, reliability, and safety of the AI model's output and behavior. 
Methods:
Prompt-Based Testing: Using targeted prompts to evaluate the model's response to various inputs. 
Evaluation Metrics: Measuring accuracy, relevance, coherence, diversity, and ethical considerations of the generated content. 
Tools: Platforms like Promptfoo, OpenAI Eval, and DeepChecks can help. 
Continuous Monitoring: Implementing pipelines to detect and resolve issues in real-time after deployment to improve reliability and user trust. 
2. A Quiz or Certification:
Purpose: To test an individual's knowledge and understanding of GenAI concepts and their application in testing. 
Example: The ISTQB® CT-GenAI certification is a formal exam testing professionals on applying GenAI, LLMs, and AI testing tools. 
Topics Covered: Core concepts, prompt engineering, common use cases, and potential risks like hallucinations and bias. 
Key Considerations for GenAI Testing:
Ethical Implications: A significant focus is placed on identifying and mitigating bias, harmful content, and data privacy risks. 
Challenges: Hallucinations (AI-generated fabrications), non-transparent models, and data protection are major hurdles in GenAI testing. 
Integration: Tools and techniques are evolving to automate testing through API access and integrate with existing CI/CD processes for better efficiency. "
"""

result = chain.invoke({"text":text})
print(result)