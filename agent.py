from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import tool

google_api =os.getenv("GOOGLE_API_KEY")
llm=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=google_api
)


#creating my agent 

researcher=Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        """Driven by curiosity, you're at the forefront of
        innnovation,eager to explore and share knowledge that could change the world .
"""
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

#creating a writer agent with custom tools responsible in writing news blog

writer=Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        """
     With a flair for simplifying comlpex topics, you craft 
    engaging narratives  that captivate and educate bringing new
    discoveries to ligh in an accessible manner.
"""
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)

