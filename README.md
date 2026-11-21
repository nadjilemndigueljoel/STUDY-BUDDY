Study Buddy-AI Study Assistant

1. Project Description

Study Buddy is an AI-powered study assistant designedto help students learn more effectively.

It uses Google Gemini to answer questions, explain lessons, and support students during their studies.

2. Main Features

. Answers students questions.
. Explains lessons in simple words.
. Remembers previous conversations.
. Saves conversation history in a JSON file.
. Suggests follow-up questions.

3. Technologies Used

. Python
. Google Gemini API
. JSON
. python-dotenv

4. Project Structure

. main.py-Main project entry point.
. chat.py-Chat interface.
. assistant.py-AI assistant logic.
. memory.py-Conversations memory.
. prompts.py-AI instructions.
. config.py-API configuration.
. memory.json-Saved conversations.
. .env-API key configuration.
. requirements.txt-Project dependencies.

5. Installation
Install the dependencies.

- pip install -r requirements.txt
Configure our Gemini API key in the .env file.

6. How to Run
Start the application:

- python chat.py
Type exit to end the session.

7. Conclusion

Study Buddy demonstrates how artificial intelligence and Python can be used to build ahelpful educational assistant.
