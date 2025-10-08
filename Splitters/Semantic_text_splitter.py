import langchain
#from langchain.text_splitter import SemanticTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

text = """
Farmers are the backbone of our food supply, working tirelessly to grow crops and raise animals.
They use knowledge, tools, and nature to produce fruits, vegetables, grains, and more.
Farming is often a family tradition, passed down through generations.
Farmers face challenges like weather, pests, and market prices, yet continue to persevere.
Their hard work helps feed communities and support the global economy.

Cricketers are professional athletes who play the game of cricket with skill and strategy.
They train rigorously to improve their batting, bowling, and fielding abilities.
Cricketers often represent their clubs, states, or countries in competitive matches.
They inspire fans with their performances, teamwork, and sportsmanship on the field.
Many cricketers become national heroes and role models for aspiring young players.
"""

splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

docs = splitter.create_documents([text])
print(docs)
