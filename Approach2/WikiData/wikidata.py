import spacy
import requests
import pandas as pd
from openpyxl import Workbook

# Load spaCy model
import subprocess
subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])

nlp = spacy.load("en_core_web_sm")

# Function to link entities to Wikidata/Wikipedia
def link_entity(entity):
    url = f"https://www.wikidata.org/w/api.php?action=wbsearchentities&search={entity}&language=en&format=json"
    response = requests.get(url)
    data = response.json()
    if data['search']:
        return data['search'][0]['id'], data['search'][0]['description']
    return None, None

# Function to verify direct links in Wikidata
def verify_link(entity1, entity2):
    url = f"https://query.wikidata.org/sparql?query=SELECT ?item WHERE {{ wd:{entity1} ?p wd:{entity2} }}&format=json"
    response = requests.get(url)
    data = response.json()
    return bool(data['results']['bindings'])

# Function to extract sections from the text
def extract_section(text, section_header):
    start_idx = text.find(section_header)
    if start_idx == -1:
        return ""
    start_idx += len(section_header)
    end_idx = text.find("#############", start_idx)
    if end_idx == -1:
        end_idx = len(text)
    return text[start_idx:end_idx].strip()

# Function to analyze text
def analyze_text(text):
    doc = nlp(text)
    entities = {ent.text: link_entity(ent.text) for ent in doc.ents}
    links = []
    direct_links = 0
    sentences = list(doc.sents)
    for sent in sentences:
        sent_entities = [ent.text for ent in sent.ents]
        for i in range(len(sent_entities)):
            for j in range(i + 1, len(sent_entities)):
                entity1 = entities[sent_entities[i]]
                entity2 = entities[sent_entities[j]]
                if entity1 and entity2:
                    links.append((entity1, entity2))
                    if verify_link(entity1[0], entity2[0]):
                        direct_links += 1
    ratio = direct_links / len(links) if links else 0
    return {"links": links, "direct_links": direct_links, "ratio": ratio}

# Extracting text and performing analysis
results = []

for file in extracted_files:
    if file.endswith(".txt"):
        file_path = os.path.join(extract_dir, file)
        with open(file_path, 'r') as f:
            content = f.read()

        # Extract coref resolved sentences and ground truth
        coref_resolved_text = extract_section(content, "coref resolved in sentences")
        ground_truth_text = extract_section(content, "ground truth")

        # Analyze coref resolved sentences
        coref_resolved_results = analyze_text(coref_resolved_text)
        ground_truth_results = analyze_text(ground_truth_text)

        # Compile results
        results.append({
            "file": file,
            "text_type": "Coref Resolved",
            "text": coref_resolved_text,
            "links_made": len(coref_resolved_results["links"]),
            "direct_links": coref_resolved_results["direct_links"],
            "ratio": coref_resolved_results["ratio"]
        })

        results.append({
            "file": file,
            "text_type": "Ground Truth",
            "text": ground_truth_text,
            "links_made": len(ground_truth_results["links"]),
            "direct_links": ground_truth_results["direct_links"],
            "ratio": ground_truth_results["ratio"]
        })

# Convert results to DataFrame and save as Excel
results_df = pd.DataFrame(results)
output_file = "entity_linking_analysis.xlsx"
results_df.to_excel(output_file, index=False)

output_file