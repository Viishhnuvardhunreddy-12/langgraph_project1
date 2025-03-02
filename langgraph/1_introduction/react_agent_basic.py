from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent,tool
from langchain_community.tools import TavilySearchResults
from dotenv import load_dotenv
import datetime

load_dotenv()

#tool initialization
search_tool=TavilySearchResults(search_depth="basic")

@tool
def get_system_time(format:str="%Y-%M-%D %H:%M:%S"):
    """Return the current date and time in the specific format given."""
    current_time=datetime.datetime.now()
    formatted_time=current_time.strftime(format)
    return formatted_time

tools=[search_tool,get_system_time]

llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")

agent=initialize_agent(tools=tools, llm=llm, agent="zero-shot-react-description", verbose=True)
agent.invoke("what is weather in hyderabad.")


