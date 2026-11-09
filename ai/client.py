import os
from openai import AsyncOpenAI

from ai.prompt import create_system_prompt

client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

async def generate_response(history):
    response = await client.responses.create(
        model=os.getenv("OPENAI_MODEL"),
        instructions=create_system_prompt(),
        input=history
    )

    return response.output_text