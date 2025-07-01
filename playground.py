from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import openai
import os
import phi
from phi.playground import Playground, serve_playground_app

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY") 
phi.api_key = os.environ.get("PHIDATA_API_KEY")

## Web Search Agent
websearch_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama3-70b-8192"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources in your answers."],
    show_tool_calls=True,
    markdown=True,
)

## Financial Agent
financial_agent = Agent(
    name="Financial Agent",
    role="Analyze financial data and provide insights",
    model=Groq(id="llama3-70b-8192"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        company_news=True,
    )],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

app = Playground(agents=[websearch_agent, financial_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)