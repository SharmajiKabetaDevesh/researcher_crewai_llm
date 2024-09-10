This code demonstrates a creative approach to using AI for automated research and content creation. By combining an LLM with specialized agents, the application aims to streamline the process of generating informative and engaging content on various technological advancements.


Components:

Agents: The application creates two AI agents:
Researcher: This agent acts like a scientist, tasked with researching a specific topic (e.g., AI in Finance) and identifying trends, pros, cons, and potential risks. It can access tools (currently unspecified) to aid research.
Writer: This agent plays the role of a journalist, taking the information gathered by the researcher and crafting an engaging and informative blog post about the topic.
Large Language Model (LLM): This is a powerful AI for generating text. The code uses a specific model called "gemini-1.5-flash" from Google AI.
Tasks:

Research Task: This task instructs the researcher agent to investigate the chosen topic and produce a concise report summarizing key points, market opportunities, and potential risks. (The report format is expected to be three paragraphs long.)
Write Task: This task instructs the writer agent to use the research findings to create a well-written, four-paragraph blog post formatted in markdown (a text formatting language). The post should focus on the latest trends and their impact on the industry, presented in a clear, engaging, and positive way. The final output is saved as a file named "blog.md".
Execution:

The application runs these tasks sequentially. First, the researcher gathers information. Then, the writer uses that information to write the blog post.
You can provide the desired topic through an "inputs" dictionary. For example, setting inputs={'topic': 'AI in Finance'} would instruct the agents to research and write about advancements in AI related to finance.
The application runs the tasks and prints the results (presumably containing the generated blog post content).

Steps to use this app:

1) Create a virtual environment using "python -m venv venv"
2) Activate venv using "venv/Scripts/activate
3) You need to clone this app now.
4) Install all packages using "python install -r requirements.txt"
5) Create an ".env" file and place your google api key.
6) Go to terminal and hit "python app.py" you are ready.

   ![Screenshot (341)](https://github.com/user-attachments/assets/f82c5fe9-0b9b-41ee-8742-56fb7a1afd41)
![Screenshot (342)](https://github.com/user-attachments/assets/9a416e07-9f71-47ee-a504-dd071a9e3dd7)
![Screenshot (343)](https://github.com/user-attachments/assets/84ee00e5-aafa-4994-b4c0-c8e125c2d6db)
![Screenshot (344)](https://github.com/user-attachments/assets/4f2e5994-d54b-4946-86ff-59cd3a5eaa7a)
![Screenshot (340)](https://github.com/user-attachments/assets/35d47e09-74e7-48be-8232-615e1ce9ffa2)
