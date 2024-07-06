import spacy
import requests
import json
import ast
import re
from bs4 import BeautifulSoup
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

class SemanticPhraseGenerator:
    def __init__(self,model_name="codegemma"):
        """
        Initialize the SemanticPhraseGenerator with a specified model.
        
        Parameters:
        model_name (str): The name of the model to use.
        """
        self.llm = ChatOllama(model=model_name)
        
        self.prompt = ChatPromptTemplate.from_template("Given this query, your task is to generate the top {top_k} wikipedia queries which are necessary and sufficient to answer the query only using the context in the input query. Do not make assumptions about time. Cover each and every detail of the given query. The output should be in the python list format and the entries in the list should not contain ' or \" at all. Do not give any text/explanation/filler information, only and only return a list of entitis. QUERY : {query}")

    def generate_semantic_phrases(self, query, top_k=5):
        """
        Generate semantic phrases using the provided query.
        
        Parameters:
        query (str): The query to generate semantic phrases for.
        
        Returns:
        list: A list of semantic phrases.
        """
        input_data = {"query": query, "top_k": top_k}
        chain = self.prompt | self.llm | StrOutputParser()
        response = chain.invoke(input_data)
        # print(response)
        
        pattern = r'["\'](.*?)["\']'
        list_of_queries = re.findall(pattern, response)
        print(f"The List Of Queries: {list_of_queries}")
        return list_of_queries
    
        # lines = response.splitlines()
        # if len(lines) > 2:
        #     response = '\n'.join(lines[1:-1])
        # else:
        #     response =  ""
        
        # response.strip()
        
        # try:
        #     semantic_phrases = json.loads(response)
        # except json.JSONDecodeError as e:
        #     print(f"Error decoding JSON response: {e}")
        #     semantic_phrases = []
        # return semantic_phrases

if __name__ == "__main__":
    # Example usage
    parser = SemanticPhraseGenerator()
    user_query = "Who was on the latest world cup winning squad for India?"
    temp = (parser.generate_semantic_phrases(user_query,4))