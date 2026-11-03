from dotenv import load_dotenv
from importlib.metadata import version
load_dotenv()

core_version = version("langchain-core")
lg_version = version("langgraph")
from langchain_anthropic import ChatAnthropic

print(f"langchain-core version: {core_version}")
print(f"langgraph version: {lg_version}")

def main():

    llm_ant=ChatAnthropic(model_name="claude-haiku-5-5")
    response_ant=llm_ant.invoke(" say 'setup complete in one word'")
    print(response_ant)
if __name__ == "__main__":
    main()
