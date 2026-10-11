from dotenv import load_dotenv
from importlib.metadata import version

load_dotenv()

core_version = version("langchain-core")
lg_version = version("langgraph")
from langchain_google_genai import ChatGoogleGenerativeAI


print(f"langchain-core version: {core_version}")
print(f"langgraph version: {lg_version}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", temperature=0)
    response = llm.invoke("Say 'setup complete!' in one word")
    print(f"Response from ChatGoogleGenerativeAI: {response}")

    print("Setup complete!")
