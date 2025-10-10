import langchain
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain.retrievers.multi_query import MultiQueryRetriever
from dotenv import load_dotenv

load_dotenv()

documents = [
    Document (page_content= "Artificial Intelligence enables machines to mimic human intelligence",metadata={"source":"H1"}),
    Document (page_content="Deep learning uses neural network with many layers to process complex data",metadata={"source":"H2"}),
    Document (page_content="Natural Language Processing helps computers to understand and generate human language",metadata={"source":"H3"}),
    Document (page_content="Langchain helps developers build LLM applications easily.",metadata={"source":"H4"}),
    Document (page_content="Chroma is a vector database optimized for LLM based search",metadata={"source":"H5"}),
    Document (page_content="Embedding converts the text into high dimensional vectors",metadata={"source":"H6"}),
    Document (page_content="OpenAI provides powerful embedding models",metadata={"source":"H7"}),
]

embedding_model = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(
    documents = documents,
    embedding=embedding_model
)

similarity_results = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k":3})
query = "what is a langchain?"
results1 = similarity_results.invoke(query)

for doc in results1:
    print(f"Source: {doc.metadata['source']}")
    print(f"Content: {doc.page_content}\n")

print("********************************************************************")

multiquery=MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(search_kwargs={"k":3}),
    llm=ChatOpenAI(model_name="gpt-5")
)   

results2 = multiquery.invoke(query)

for doc in results2:
    print(f"Source: {doc.metadata['source']}")
    print(f"Content: {doc.page_content}\n")