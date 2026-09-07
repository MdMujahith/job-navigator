from typing import Annotated, Sequence, TypedDict
from dotenv import load_dotenv  
from langchain_core.messages import BaseMessage,HumanMessage # The foundational class for all message types in LangGraph
from langchain_core.messages import ToolMessage # Passes data back to LLM after it calls a tool such as the content and the tool_call_id
from langchain_core.messages import SystemMessage # Message for providing instructions to the LLM
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
import requests
import os
from datetime import date
from pathlib import Path
from tools.job_tools import list_jobs, create_job, update_job, delete_job
from tools.company_tools import list_companies, create_company, update_company, delete_company
from tools.interview_tools import list_interviews, create_interview, update_interview, delete_interview


load_dotenv()

tools = [
    list_jobs, create_job, update_job, delete_job,
    list_companies, create_company, update_company, delete_company,
    list_interviews, create_interview, update_interview, delete_interview,
]
model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite").bind_tools(tools)

prompt_path = Path(__file__).parent / "handler.Agent.md"

with open(prompt_path, "r", encoding="utf-8") as file:
    content = file.read()

system_prompt = SystemMessage(content=content)

class AgentState(TypedDict):
    messages:Annotated[Sequence[BaseMessage], add_messages]

def jobgetter(state:AgentState)->AgentState:
    """ Getting all the Job Form the Database"""
    messages = [system_prompt] + list(state["messages"])
    response = model.invoke(messages)
    return {"messages":response}

def should_continue(state: AgentState): 
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls: 
        return "end"
    else:
        return "continue"
    

graph = StateGraph(AgentState)
graph.add_node("our_agent",jobgetter)


tool_node = ToolNode(tools=tools)
graph.add_node("tools", tool_node)

graph.set_entry_point("our_agent")

graph.add_conditional_edges(
    "our_agent",
    should_continue,
    {
        "continue": "tools",
        "end": END,
    },
)

graph.add_edge("tools", "our_agent")

app = graph.compile()
user_input=input("You: ")
while user_input != "Exit".lower():
    user_input=input("You: ")
    result = app.invoke({
    "messages": [
        HumanMessage(content=user_input)]
})

    final_message = result["messages"][-1]

    print(final_message.content[0]["text"])