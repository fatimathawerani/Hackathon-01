from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
from agents import set_tracing_disabled, function_tool
import os
from dotenv import load_dotenv
from agents import enable_verbose_stdout_logging

enable_verbose_stdout_logging()

load_dotenv()
set_tracing_disabled(disabled=True)

openrouter_key = os.getenv("OPENROUTER_API_KEY")

if not openrouter_key:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables")

openrouter_client = AsyncOpenAI(
    api_key=openrouter_key,
    base_url="https://openrouter.ai/api/v1",
)

openrouter_model = OpenAIChatCompletionsModel(
    # model="meta-llama/llama-3.3-70b-instruct:free",  # Better free model
    model="openai/gpt-oss-20b:free",  # Better free model
    openai_client=openrouter_client
)

import cohere
from qdrant_client import QdrantClient

# Initialize Cohere client
cohere_client = cohere.Client("a4xSXF4KL1ZseodFka4U69s6tIpD1VzWxvJ4ZFLa")
# Connect to Qdrant
qdrant = QdrantClient(
    url="https://7e7592e4-c1ca-4843-bf9b-87d9f9c7d57c.europe-west3-0.gcp.cloud.qdrant.io:6333",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.Pw2E54mv2FbsSdHQE7_hyt0lwNVtF21Wn99XsvdhgjY",
)



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
        collection_name="ai-interactive-textbook",
        query=embedding,
        limit=5
    )
    return [point.payload["text"] for point in result.points]



agent = Agent(
    name="Assistant",
    instructions=""" 
    You are an AI tutor for the Physical AI & Humanoid Robotics textbook.
    To answer the user question, first call the tool `retrieve` with the user query.
    Use ONLY the returned content from `retrieve` to answer.
    If the answer is not in the retrieved content, say "I don't know".
    """,

    model=openrouter_model,
    tools=[retrieve]
)


result = Runner.run_sync(
    agent,
    input="what is ROS?",
)

print(result.final_output)