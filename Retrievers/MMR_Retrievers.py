import langchain
from langchain_openai import OpenAI
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

documents = [
    Document (page_content= "Artificial Intelligence enables machines to mimic human intelligence"),
    Document (page_content="Deep learning uses neural network with many layers to process complex data"), 
    Document (page_content="Natural Language Processing helps computers to understand and generate human language"), 
    Document (page_content="Langchain helps developers build LLM applications easily."),
    Document (page_content="Chroma is a vector database optimized for LLM based search"),
    Document (page_content="Embedding converts the text into high dimensional vectors"), 
    Document (page_content="OpenAI provides powerful embedding models")
]

embedding_model = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(
    documents = documents,
    embedding=embedding_model
)

retriever=vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k":3, "lambda_mult":1}
    )

query = "what is a langchain?"

results = retriever.invoke(query)

print(results)