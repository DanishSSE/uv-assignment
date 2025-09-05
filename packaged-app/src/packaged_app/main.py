import os
from dotenv import load_dotenv
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_default_openai_client,
    set_tracing_disabled,
    OpenAIChatCompletionsModel,
)

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing. Please set it in your .env file.")

external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

set_default_openai_client(external_client)
set_tracing_disabled(True)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", openai_client=external_client
)

agent = Agent(
    name="GreetingAgent",
    instructions="You are a friendly assistant that greets users.",
    model=model,
)


def run_agent():
    result = Runner.run_sync(
        agent, "Greet me in Islamic way in one line and asking about my well-being."
    )
    print(result.final_output)
