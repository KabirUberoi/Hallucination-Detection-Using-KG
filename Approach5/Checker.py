import spacy
import requests
import json
import re
import html2text
import os
import markdownify
import networkx as nx
import matplotlib.pyplot as plt
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import networkx as nx
import matplotlib.pyplot as plt
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer, util
import numpy as np

class PhraseExtractor:
    def __init__(self, model_name="en_core_web_trf"):
        """
        Initialize the PhraseExtractor with a spaCy model.
        
        Parameters:
        model_name (str): The name of the spaCy model to load.
        """
        self.nlp = spacy.load(model_name)

    def extract_phrases(self, sentence):
        """
        Extract noun phrases from a sentence.
        
        Parameters:
        sentence (str): The sentence from which to extract phrases.
        
        Returns:
        list: A list of extracted noun phrases.
        """
        doc = self.nlp(sentence)
        phrases = [chunk.text for chunk in doc.noun_chunks if len(chunk) > 1]
        return phrases

class WikipediaSearcher:
    @staticmethod
    def get_wikipedia_titles(phrase):
        """
        Fetch Wikipedia article titles relevant to a given phrase.
        
        Parameters:
        phrase (str): The phrase to search for.

        Returns:
        list: A list of Wikipedia article titles relevant to the phrase.
        """
        search_url = "https://en.wikipedia.org/w/api.php"
        params = {
            'action': 'query',
            'list': 'search',
            'srsearch': phrase,
            'format': 'json'
        }
        try:
            response = requests.get(search_url, params=params)
            response.raise_for_status()
            data = response.json()
            titles = [result['title'] for result in data['query']['search']]
            return titles
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
            return []

class WikidataSearcher:
    @staticmethod
    def get_wikidata_entities(title):
        """
        Fetch Wikidata entities relevant to a given Wikipedia article title.
        
        Parameters:
        title (str): The Wikipedia article title.

        Returns:
        list: A list of Wikidata entities relevant to the title.
        """
        search_url = "https://www.wikidata.org/w/api.php"
        params = {
            'action': 'query',
            'list': 'search',
            'srsearch': title,
            'format': 'json'
        }
        try:
            response = requests.get(search_url, params=params)
            response.raise_for_status()
            data = response.json()
            entities = [result['title'] for result in data['query']['search']]
            return entities
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
            return []

class WikidataContentFetcher:
    @staticmethod
    def fetch_content(title):
        """
        Fetch content from Wikidata for a given title.
        
        Parameters:
        title (str): The title to fetch content for.

        Returns:
        dict: The content fetched from Wikidata.
        """
        S = requests.Session()
        URL = "https://en.wikipedia.org/w/api.php"
        PARAMS = {
            "action": "parse",
            "page": title,
            "format": "json"
        }
        try:
            R = S.get(url=URL, params=PARAMS)
            R.raise_for_status()
            DATA = R.json()
            return DATA
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
            return {}

    @staticmethod
    def extract_content(data):
        """
        Extract content from the provided JSON data.
        
        Parameters:
        data (dict): The JSON data containing the parsed content.

        Returns:
        str: The plain text content extracted from the HTML.
        """
        content = data.get('parse', {}).get('text', {}).get('*', '')
        
        # Convert HTML to plain text
        text_maker = html2text.HTML2Text()
        text_maker.ignore_links = False  # Set to False if you want to keep links in the text
        plain_text = text_maker.handle(content)
        
        return plain_text

    @staticmethod
    def extract_links(content):
        """
        Extract links from the provided HTML content.
        
        Parameters:
        content (str): The HTML content to extract links from.

        Returns:
        list: A list of extracted links.
        """
        links = re.findall(r'href=["\'](.*?)["\']', content)
        return links

class MarkdownProcessor:
    def __init__(self, temp_dir, output_dir):
        self.temp_dir = temp_dir
        self.output_dir = output_dir
        self.global_idx=0
        os.makedirs(self.output_dir, exist_ok=True)

    def convert_to_markdown(self, content):
        return markdownify.markdownify(content)

    def save_markdown(self, markdown_content):
        markdown_file_path = os.path.join(self.temp_dir, 'content.md')
        mode = 'a' if os.path.exists(markdown_file_path) else 'w'
        with open(markdown_file_path,mode, encoding='utf-8') as md_file:
            md_file.write(markdown_content)
        return markdown_file_path

    def split_markdown_into_chunks(self, markdown_text):
        lines = markdown_text.split('\n')
        chunks = []
        current_chunk = []

        for line in lines:
            if line.startswith('#'):
                if current_chunk:
                    chunks.append('\n'.join(current_chunk))
                    current_chunk = []
            current_chunk.append(line)

        if current_chunk:
            chunks.append('\n'.join(current_chunk))

        return chunks

    def save_chunks(self, chunks):
        """
        Save the chunks to the output directory. If the directory doesn't exist, create it. 
        Use a global index to ensure file names do not conflict.
        
        Parameters:
        chunks (list): The list of markdown chunks to save.
        """
        # Ensure output directory exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        for chunk in chunks:
            chunk_path = os.path.join(self.output_dir, f'chunk_{self.global_idx + 1}.md')
            with open(chunk_path, 'w', encoding='utf-8') as chunk_file:
                chunk_file.write(chunk)
            self.global_idx += 1

    def process(self, content):
        markdown_content = self.convert_to_markdown(content)
        self.save_markdown(markdown_content)
        chunks = self.split_markdown_into_chunks(markdown_content)
        self.save_chunks(chunks)
        return [chunk.split('\n')[0] for chunk in chunks if chunk.split('\n')[0].startswith('#')]

class KnowledgeGraph:
    def __init__(self, chunk_titles, output_dir):
        self.chunk_titles = chunk_titles
        self.graph = nx.DiGraph()
        self.output_dir = output_dir

    def build_graph(self):
        for i, title in enumerate(self.chunk_titles):
            if i < len(self.chunk_titles) - 1:
                self.graph.add_edge(title, self.chunk_titles[i + 1])

    def visualize_graph(self):
        plt.figure(figsize=(20, 15))
        pos = nx.spring_layout(self.graph, k=2)  # Increase k to increase the distance between nodes
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=3000, edge_color='gray', linewidths=1, font_size=8, font_weight='bold')  # Reduce font_size for smaller text
        plt.title("Knowledge Graph of Linked Entities")
        image_path = os.path.join(self.output_dir, 'knowledge_graph.png')
        plt.savefig(image_path)
        plt.show()
        print(f"Knowledge graph image saved to: {image_path}")

class WikipediaScraper:
    def __init__(self, output_file, output_content_file, output_links_file, temp_dir, chunk_output_dir):
        self.phrase_extractor = PhraseExtractor()
        self.wikipedia_searcher = WikipediaSearcher()
        self.wikidata_searcher = WikidataSearcher()
        self.wikidata_content_fetcher = WikidataContentFetcher()
        self.output_file = output_file
        self.output_content_file = output_content_file
        self.output_links_file = output_links_file
        self.temp_dir = temp_dir
        self.chunk_output_dir = chunk_output_dir
        self.markdown_processor = MarkdownProcessor(self.temp_dir, self.chunk_output_dir)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def process_query(self, query, k=10):
        phrases = self.phrase_extractor.extract_phrases(query)
        print(f"Extracted phrases: {phrases}")

        results = {}
        content_results = {}
        links_results = {}
        all_chunks = []

        for phrase in phrases:
            titles = self.wikipedia_searcher.get_wikipedia_titles(phrase)
            print(f"Wikipedia titles for '{phrase}': {titles}")
            results[phrase] = {
                "wikipedia_titles": titles,
                "wikidata_entities": [],
                "content": {}
            }
            content_results[phrase] = {}
            links_results[phrase] = {}

            for title in titles:
                entities = self.wikidata_searcher.get_wikidata_entities(title)
                content_data = self.wikidata_content_fetcher.fetch_content(title)
                plain_text = self.wikidata_content_fetcher.extract_content(content_data)
                links = self.wikidata_content_fetcher.extract_links(content_data.get('parse', {}).get('text', {}).get('*', ''))

                chunk_titles = self.markdown_processor.process(plain_text)
                all_chunks.extend(chunk_titles)

                results[phrase]["wikidata_entities"].extend(entities)
                results[phrase]["content"][title] = plain_text
                content_results[phrase][title] = plain_text
                links_results[phrase][title] = links

        # Extract top k chunks
        top_chunks = self.get_top_chunks(query, all_chunks, k)
        print("\nTop chunks: \n", top_chunks)

        # Save results to output files
        try:
            with open(self.output_file, 'w', encoding='utf-8') as file:
                json.dump(results, file, ensure_ascii=False, indent=4)
            with open(self.output_content_file, 'w', encoding='utf-8') as content_file:
                json.dump(content_results, content_file, ensure_ascii=False, indent=4)
            with open(self.output_links_file, 'w', encoding='utf-8') as links_file:
                json.dump(links_results, links_file, ensure_ascii=False, indent=4)
            print(f"Results saved to {self.output_file}, {self.output_content_file}, and {self.output_links_file}")
        except IOError as e:
            print(f"Error saving results: {e}")

    def get_top_chunks(self, query, chunks, k):
        # BM25 step
        bm25 = BM25Okapi([chunk.split() for chunk in chunks])
        query_tokens = query.split()
        bm25_scores = bm25.get_scores(query_tokens)
        top_100_idx = np.argsort(bm25_scores)[::-1][:100]

        top_100_chunks = [chunks[i] for i in top_100_idx]

        # Sentence embeddings step
        query_embedding = self.model.encode(query)
        chunk_embeddings = self.model.encode(top_100_chunks)

        cosine_scores = util.cos_sim(query_embedding, chunk_embeddings).cpu().numpy().flatten()
        top_k_idx = np.argsort(cosine_scores)[::-1][:k]

        top_k_chunks = [top_100_chunks[i] for i in top_k_idx]
        return top_k_chunks

if __name__ == "__main__":
    temp_dir = ""
    chunk_output_dir = "output_chunks"
    scraper = WikipediaScraper(output_file="output.json", output_content_file="extracted_content.json", output_links_file="extracted_links.json", temp_dir=temp_dir, chunk_output_dir=chunk_output_dir)
    user_query = "Explain the theory of relativity and its implications in modern physics."
    scraper.process_query(user_query)