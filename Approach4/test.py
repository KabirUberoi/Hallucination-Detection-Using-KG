from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Create an instance of ChatOllama
ollama = ChatOllama(model="codegemma")

# Define your system prompt
system_prompt = "You will be given a query and your task is to generate a list of wikipedia queries which are necessary and sufficient to answer the query. The output should be in a JSON format only. Do not give any text/explanation/filler information, only and only return a JSON."

# Set the system prompt

# Example query
query = "What are the benefits of data visualization?"

# Get the response
response = ollama.ask(query)

# Print or process the response
print(response)