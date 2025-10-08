import langchain
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
load_dotenv()

text = """
Space exploration is the physical investigation of outer space by uncrewed robotic space probes and through human spaceflight.[1]

While the observation of objects in space, known as astronomy, predates reliable recorded history, it was the development of large and relatively efficient rockets during the mid-twentieth century that allowed physical space exploration to become a reality. Common rationales for exploring space include advancing scientific research, national prestige, uniting different nations, ensuring the future survival of humanity, and developing military and strategic advantages against other countries.[2]

The early era of space exploration was driven by a "Space Race" in which the Soviet Union and the United States vied to demonstrate their technological superiority. Landmarks of this era include the launch of the first human-made object to orbit Earth, the Soviet Union's Sputnik 1, on 4 October 1957, and the first Moon landing by the American Apollo 11 mission on 20 July 1969. The Soviet space program achieved many of the first milestones, including the first living being in orbit in 1957, the first human spaceflight (Yuri Gagarin aboard Vostok 1) in 1961, the first spacewalk (by Alexei Leonov) on 18 March 1965, the first automatic landing on another celestial body in 1966, and the launch of the first space station (Salyut 1) in 1971.
"""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=""
)

result = splitter.split_text(text)
print(result)

# Character Splitter with Chunk Overlap


splitter1 = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10,
    separator=""
)

result1 = splitter1.split_text(text)
print(result1)
