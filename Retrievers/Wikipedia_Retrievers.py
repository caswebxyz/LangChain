import langchain
from langchain_openai import OpenAI
from langchain_community.retrievers import WikipediaRetriever

wkretriever = WikipediaRetriever(
    top_k_results=2,
    lang="en"
)

query = "Analyze history of world war II and role of India in it"

docs = wkretriever.invoke(query)

print(docs)
