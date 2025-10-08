import langchain
from langchain_openai import OpenAIEmbeddings
#from langchain.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain.schema import Document
from dotenv import load_dotenv

load_dotenv()

doc1 = Document(
    page_content="MS Dhoni, famously known as captain Cool, has led Chennai Super kings to muliple IPL Trophies, he is the best wicket keeper and best finisher",
    metadata={"team":"Chennai Super Kings"}
)


doc2 = Document(
    page_content="Rohit Sharma is one of the most successful players in IPL history>>, winning six titles, including one with Deccan Chargers and five as captain of the Mumbai Indians. A prolific batsman, he holds several IPL records and is known for his powerful hitting and astute leadership",
    metadata={"team":"Mumbai Indians"}
)

doc3 = Document(
    page_content="Virat Kohli, the former captain of Royal Challengers Bangalore, is the highest run-scorer in IPL history. Known for his passion and consistency, he is a modern-day batting great who thrives under pressure.",
    metadata={"team": "Royal Challengers Bangalore"}
)

doc4 = Document(
    page_content="Jasprit Bumrah is one of the most feared bowlers in the IPL. Representing Mumbai Indians, he is known for his deadly yorkers, calm temperament, and ability to deliver in crucial moments.",
    metadata={"team": "Mumbai Indians"}
)

doc5 = Document(
    page_content="Ravindra Jadeja, a key all-rounder for Chennai Super Kings, contributes with the bat, ball, and in the field. His quick left-arm spin and electric fielding make him an invaluable asset to the team.",
    metadata={"team": "Chennai Super Kings"}
)

docs = [doc1,doc2,doc3,doc4,doc5]

vector_store=Chroma(
    embedding_function = OpenAIEmbeddings(),
    persist_directory = "my_chroma_db",
    collection_name = "emp"
    )


#store_info = vector_store.add_documents(docs)

bowler_info = vector_store.similarity_search(
    query = "who is the bowler?",
    k=1
)

print("<<<<<<<<<<<<<<<===========================================================>>>>>>>>>>>>>>>>>>>>>>>>>")
print(bowler_info)

bowler_info = vector_store.similarity_search(
    query = "who is the bowler?",
    k=2
)



bowler_info = vector_store.similarity_search_with_score(
    query = "who is the bowler?",
    k=2
)


doc3_update = Document(
    page_content="Jasprit Bumrahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh",
    metadata={'team': 'Mumbai Indians'}
)

vector_store.update_document("7d918c53-e944-442d-a666-275352d62e4d",doc3_update)

print("<*****************************************>>>>>>>>")
print(vector_store.get(include=["documents"]))

vector_store.delete(ids=["7d918c53-e944-442d-a666-275352d62e4d"])

print("<*****************************************>>>>>>>>")
print(vector_store.get(include=["documents"]))