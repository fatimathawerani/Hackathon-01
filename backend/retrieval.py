import cohere
from qdrant_client import QdrantClient
from agents import function_tool 
import os 
from dotenv import load_dotenv

load_dotenv()

cohere_api_key = os.getenv("COHERE_API_KEY")
qdrant_url = os.getenv("QDRANT_URL")
qdrant_api_key = os.getenv("QDRANT_API_KEY")
qdrant_collection_name = os.getenv("ai-interactive-textbook")

cohere_client = cohere.Client(cohere_api_key)
qdrant = QdrantClient(url=qdrant_url, api_key=qdrant_api_key)



def get_embedding(text):
    """Get embedding vector from Cohere Embed v3"""
    response = cohere_client.embed(
        model="embed-english-v3.0",
        input_type="search_query",  # Use search_query for queries
        texts=[text],
    )
    return response.embeddings[0]  # Return the first embedding


@function_tool
def retrieve(query):
    embedding = get_embedding(query)
    result = qdrant.query_points(
        collection_name=qdrant_collection_name,
        query=embedding,
        limit=5
    )
    return [point.payload["text"] for point in result.points]