from crewai import Crew,Process
from agent import researcher,writer
from tasks import research_task,write_task

crew=Crew(
    agents=[researcher,writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)
inputs = {'topic': 'AI in Finance'}
res=crew.kickoff(inputs=inputs)
print(res)