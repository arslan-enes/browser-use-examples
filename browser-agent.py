from browser_use import Agent
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from pydantic import SecretStr

import os
import asyncio

load_dotenv()  # load environment variables from .env file

llm = AzureChatOpenAI(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT", ""),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", ""),
    api_key=SecretStr(os.getenv("AZURE_OPENAI_API_KEY", "")),
)


async def main():
    agent = Agent(
        task="Compare pricing informations for followed products: jira, linear, clickup",
        llm=llm,
        save_conversation_path="logs/conversations.json",
    )
    result = await agent.run()
    print(result)


asyncio.run(main())
