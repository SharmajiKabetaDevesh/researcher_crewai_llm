from crewai import Task
from tools import tool
from agent import researcher,writer

research_task=Task(
    description=(
        """
   Identify the next big trend in {topic}.
   Focus on identifying pros and cons and the overall narrative.
   Your final reposrt should be clearly articulate the key points,
   its market oppportunities,and potential risk.
"""
    ),
    expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',

    tools=[tool],
    agent=researcher

)

write_task=Task(
    description=(
        """
     Compose an insightful rticle on {topic}.
     Focus on the latest trends and how it's impacting the industry.
     This acticle should be easy to understand, engaging ,and positive.
"""
    ),
    expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
    tool=[tool],
    agent=writer,
    async_exectution=False,
    output_dfile='blog.md'
)