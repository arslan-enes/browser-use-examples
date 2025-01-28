from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from pydantic import SecretStr

import os
import asyncio

load_dotenv()  # load environment variables from .env file

browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path="/usr/bin/google-chrome"
        # For MacOS, '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    )
)

llm = AzureChatOpenAI(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT", ""),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", ""),
    api_key=SecretStr(os.getenv("AZURE_OPENAI_API_KEY", "")),
)


async def main():
    agent = Agent(
        task="Create a Google Form that aims get name and email of the user. Name it 'Let's meet with Actins!' and publish. Return a link to the published form",
        llm=llm,
        browser=browser,
        save_conversation_path="logs/conversations.json",
    )
    result = await agent.run()
    print(result)


asyncio.run(main())
