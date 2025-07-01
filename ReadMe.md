# Financial AI Agent

A multi-agent AI system built with Phidata that combines web search capabilities with financial data analysis. The system uses Groq's LLaMA models to provide comprehensive financial insights and market research.

## Features

- **Web Search Agent**: Searches the web for general information using DuckDuckGo
- **Financial Agent**: Analyzes financial data using Yahoo Finance
- **Multi-Agent Coordination**: Combines both agents for comprehensive analysis
- **Interactive Playground**: Web-based interface for agent interaction
- **Real-time Data**: Live stock prices, analyst recommendations, and company news

## Architecture

The system consists of two specialized agents:

1. **Web Search Agent**
   - Model: Groq LLaMA3-70B
   - Tool: DuckDuckGo search
   - Role: General web information retrieval

2. **Financial Agent**
   - Model: Groq LLaMA3-70B
   - Tools: Yahoo Finance (stock prices, analyst recommendations, company news)
   - Role: Financial data analysis and insights

## Prerequisites

- Python 3.8+
- OpenAI API key
- Phidata API key
- Groq API access

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd financial-ai-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key_here
PHIDATA_API_KEY=your_phidata_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

### Command Line Interface

Run the financial agent directly:
```bash
python financial_agent.py
```

This will execute a sample query about company stocks, providing:
- Latest news summary
- Current stock price
- Analyst recommendations

### Web Playground

Launch the interactive web interface:
```bash
python playground.py
```

Then open your browser and navigate to the provided URL (typically ` URL: https://phidata.app/playground?endpoint=localhost%3A7777`) to interact with the agents through a web interface.

## Project Structure

```
financial-ai-agent/
├── financial_agent.py    # Main agent implementation
├── playground.py         # Web interface setup
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables (create this)
└── README.md           # This file
```

## Configuration

### Agent Customization

You can modify agent behavior by updating their instructions:

```python
financial_agent = Agent(
    name="Financial Agent",
    role="Analyze financial data and provide insights",
    model=Groq(id="llama3-70b-8192"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        company_news=True,
        stock_fundamentals=True,  # Add more tools as needed
    )],
    instructions=["Use tables to display the data", "Include risk analysis"],
    show_tool_calls=True,
    markdown=True,
)
```

### Available YFinance Tools

- `stock_price`: Current and historical stock prices
- `analyst_recommendations`: Analyst ratings and price targets
- `company_news`: Latest company-specific news
- `stock_fundamentals`: Financial statements and ratios
- `technical_indicators`: Technical analysis indicators

## Example Queries

- "What's the current stock price of Tesla and recent news?"
- "Compare Apple and Microsoft stock performance"
- "Analyze the financial health of Amazon"
- "What are analysts saying about Google's future prospects?"

## API Keys Setup

### Groq API Key
1. Visit [Groq Console](https://console.groq.com/)
2. Create an account and generate an API key
3. Add to your `.env` file

### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Create an account and generate an API key
3. Add to your `.env` file

### Phidata API Key
1. Visit [Phidata](https://phidata.com/)
2. Create an account and generate an API key
3. Add to your `.env` file

## Dependencies

- **phidata**: Agent framework and orchestration
- **python-dotenv**: Environment variable management
- **yfinance**: Yahoo Finance data access
- **duckduckgo-search**: Web search capabilities
- **fastapi**: Web framework for playground
- **uvicorn**: ASGI server
- **groq**: Groq API client
- **openai**: OpenAI API client

## Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure all API keys are correctly set in the `.env` file
2. **Import Errors**: Verify all dependencies are installed via `pip install -r requirements.txt`
3. **Network Issues**: Check internet connection for API calls and data fetching