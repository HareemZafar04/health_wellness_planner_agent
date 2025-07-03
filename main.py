import asyncio
import warnings
import sys
import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from context import UserSessionContext
from agent import PlannerAgent
from utils.streaming import stream_response
import google.generativeai as genai  # Correct import

warnings.filterwarnings("ignore", category=DeprecationWarning, module="pydantic")

async def main():
    # Load environment variables
    load_dotenv()
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY is not set in .env file. Please add it and retry.")

    # Configure the API key
    genai.configure(api_key=gemini_api_key)
    
    # Initialize context and agent
    ctx = UserSessionContext(name="Guest", uid=1)
    agent = PlannerAgent()
    wrapper = None

    print(">>> Health & Wellness Agent (type 'quit' to exit)")
    while True:
        user = input("\nYou: ").strip()
        if user.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break
        model = genai.GenerativeModel('gemini-1.5-flash')  # Use correct model name
        response = model.generate_content(user)
        print(response.text)

if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())