from langchain.llms import OpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent

llm = OpenAI(temperature=0.9)
tools = load_tools(["serpapi"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
agent.run("tell me about Michael Wang, a student at University of Waterloo. Be sure to be specific and talk about all aspects of Michael Wang.")
