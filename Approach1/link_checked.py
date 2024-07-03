import spacy
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('dbpedia_spotlight', config={'confidence': 0.35})
from fastcoref import FCoref
model = FCoref()
from SPARQLWrapper import SPARQLWrapper, JSON, POST
from datasets import load_dataset
dataset = load_dataset("potsawee/wiki_bio_gpt3_hallucination")
import os
from tqdm import tqdm

def get_cluster_spans(doc, clusters):
    fast_clusters = []
    for cluster in clusters:
        new_group = []
        for start, end in cluster:
            span = doc.char_span(start, end)
            if span is not None:
                new_group.append([span.start, span.end - 1])
        fast_clusters.append(new_group)
    return fast_clusters

def get_clusters(doc, text):
    preds = model.predict(texts=[text])
    clusters = preds[0].get_clusters(as_strings=False)
    cluster_spans = get_cluster_spans(doc, clusters)
    return cluster_spans

def get_span_noun_indices(doc, cluster):    
    spans = [doc[start:end+1] for start, end in cluster]

    spans_pos = []
    for span in spans:
        pos_tags = [token.pos_ for token in span]
        spans_pos.append(pos_tags)

    noun_indices = []
    for i, pos_list in enumerate(spans_pos):
        if 'NOUN' in pos_list or 'PROPN' in pos_list:
            noun_indices.append(i)
    return noun_indices

def get_cluster_head(doc, cluster, noun_indices):
    head_idx = noun_indices[0]
    head_start, head_end = cluster[head_idx]
    head_span = doc[head_start:head_end+1]
    return head_span, [head_start, head_end]

def is_containing_other_spans(span, all_spans):
    for s in all_spans:
        if s[0] >= span[0] and s[1] <= span[1] and s != span:
            return True  
    return False

def replacement(coref, resolved, mention_span):
    start, end = coref
    mention_text = mention_span.text_with_ws 
    resolved[start] = mention_text
    for i in range(start + 1, end + 1):
        resolved[i] = ""
    return resolved

def replace_corefs(document, clusters):
    resolved = [token.text_with_ws for token in document]
    all_spans = [span for cluster in clusters for span in cluster]

    for cluster in clusters:
        noun_indices = get_span_noun_indices(document, cluster)

        if noun_indices:
            mention_span, mention = get_cluster_head(document, cluster, noun_indices)
        else:
            start, end = cluster[0]
            mention_span = document[start:end+1]
            mention = cluster[0]
            
        for coref in cluster:
            if coref != mention and not is_containing_other_spans(coref, all_spans):
                replacement(coref, resolved, mention_span)

    return "".join(resolved)

def coreference_resolution(text):
    doc = nlp(text) 
    clusters = get_clusters(doc, text) 
    return replace_corefs(doc, clusters) 

def get_sentence_based_links(text):
    final_text = coreference_resolution(text)
    doc = nlp(final_text)
    sentence_forms = []
    for sent in doc.sents:
        # sentence_local = []
        # for ent in sent.ents:
        #     if ent.kb_id_!="":
        #         sentence_local.append((ent.text, ent.kb_id_, ent._.dbpedia_raw_result['@similarityScore']))
        # sentence_forms.append(sentence_local)        
        sentence_forms.append([ent.kb_id_ for ent in sent.ents if ent.kb_id_ != ""])
    pairs = []
    count = 0
    for entities in sentence_forms:
        if len(entities)>1:
            for i in range(len(entities)):
                for j in range(i+1,len(entities)):
                    pairs.append([entities[i],entities[j]])
                    pairs.append([entities[j],entities[i]])
                    count+=2
    print(f"The number of pairs is: {count}\n")
    return pairs

def check_direct_link(source, target):
    sparql = SPARQLWrapper("https://dbpedia.org/sparql")
    
    query = f"""
    ASK WHERE {{
      <{source}> ?predicate <{target}> .
    }}
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    
    results = sparql.query().convert()
    return results['boolean']

# test =  ["John Russell Reynolds (1820–1876) was an English lawyer, judge, and author.", "He was born in London, the son of a barrister, and was educated at Eton College and Trinity College, Cambridge.", "He was called to the bar in 1845, and became a Queen's Counsel in 1859.", "He was appointed a judge of the Court of Common Pleas in 1867, and was knighted in 1871.", "Reynolds was a prolific author, writing on a wide range of topics.", "He wrote several books on legal topics, including The Law of Libel and Slander (1863), The Law of Copyright (1865), and The Law of Patents for Inventions (1868).", "He also wrote on a variety of other topics, including history, biography, and literature.", "He was a frequent contributor to the Saturday Review, and wrote several books on Shakespeare, including The Mystery of William Shakespeare (1848) and The Authorship of Shakespeare (1875).", "He also wrote a biography of the poet John Keats (1848)." ]
# #test = [ "Gordon David Strachan (born 9 February 1957) is a Scottish football manager and former player.", "He is the manager of the Scotland national team.", "Strachan played for Dundee, Aberdeen, Manchester United, Leeds United and Coventry City, as well as the Scotland national team.", "He has also managed Coventry City, Southampton, Celtic and Middlesbrough.", "Strachan began his managerial career at Coventry City in 1996, leading them to the 1997 FA Cup Final, where they lost to Tottenham Hotspur.", "He then moved to Southampton in 2001, where he guided them to the 2003 FA Cup Final, which they lost to Arsenal.", "In 2005, he was appointed manager of Celtic, where he won three consecutive Scottish Premier League titles and the Scottish League Cup twice.", "He left Celtic in 2009 and was appointed manager of Middlesbrough in October 2010.", "He left Middlesbrough in October 2013.", "In January 2013, Strachan was appointed manager of the Scotland national team.", "He has since led Scotland to the UEFA Euro 2016 qualifying playoffs, where they were eliminated by eventual finalists, and to the 2018 FIFA World Cup" ]
# text = ""
# for i in test:
#    text += " " + i
# print(text)

# #text = "Claims of justification rest both on norms that permit the nominal commission of offenses and the perception of facts that support the application of the norm. The simplest justification is consent, for which the norm is simply whether the intended victim wants or desires the defendant's conduct to occur. Slightly more complicated is self-defense which requires three objective elements: (1) an actual attack, (2) a minimally necessary response, and (2) and a relationship of proportionality between the threatened interest and the harm done."

def number_of_direct_links_in_dbpedia(text):
    pairs = get_sentence_based_links(text)
    number_of_pairs = len(pairs)
    existing_links = 0
    
    for i in tqdm(range(len(pairs)), desc="Processing entries", unit="entry"):
        if(check_direct_link(pairs[i][0], pairs[i][1])):
            existing_links= existing_links+1
    
    fraction = -1
    if(number_of_pairs>0):
        fraction = existing_links/number_of_pairs
    print(f"The fraction of correct links = {fraction}")
    return fraction

def check_i_th_entry_in_database(i):
    sentences = dataset["evaluation"][i]["gpt3_text"]
    ground_truth = dataset["evaluation"][i]["wiki_bio_text"]
    annotation = dataset["evaluation"][i]["annotation"]

    ground_truth_pairs = get_sentence_based_links(ground_truth)
    
    sentence_pairs = get_sentence_based_links(sentences)
    
    fraction = -1; 
    count = len(sentence_pairs)
    match = 0
    for pair in sentence_pairs:
        if pair in ground_truth_pairs:
            match+=1
    if(count!=0):
        fraction=match/count
    return sentences, ground_truth,fraction,annotation,sentence_pairs,ground_truth_pairs
  
def write_entries_to_files(entries, folder_name="Self_GPT_Testing"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    for i, entry in enumerate(entries):
        filename = os.path.join(folder_name, f"entry_{i+1}.txt")
        with open(filename, 'w') as file:
            file.write("#############GROUND_PAIRS############\n\n")
            for x in entry[5]:
                file.write(f"{x[0]} and {x[1]}\n")
            file.write("#############SENTENCE_PAIRS############\n\n")
            for x in entry[4]:
                file.write(f"{x[0]} and {x[1]}\n")
            file.write("%%%%%%%%%%%%%%%%%%%%SENTENCES%%%%%%%%%%%%%%%%%\n")
            file.write(entry[0])
            file.write("\n\n")
            file.write("%%%%%%%%%%%%%%%%%%%%GROUND_TRUTH%%%%%%%%%%%%%%%\n")
            file.write(entry[1])
            file.write("\n\n")
            file.write("%%%%%%%%%%%%%%%%%%%%FRACTIONS%%%%%%%%%%%%%%%%%%\n")
            file.write(f"{entry[2]}")
            file.write("\n\n")
            file.write("%%%%%%%%%%%%%%%%%%%%ANNOTATIONS%%%%%%%%%%%%%%%%\n")
            for i in entry[3]:
                file.write(f"{i} ")
            file.write("\n\n")
            
checking = []
correct_scores = []
incorrect_scores = []

for i in tqdm(range(5), desc="Processing entries", unit="entry"):
    sentences = dataset["evaluation"][i]["gpt3_text"]
    ground_truth = dataset["evaluation"][i]["wiki_bio_text"]
    annotation = dataset["evaluation"][i]["annotation"]
    
    sentences_score = number_of_direct_links_in_dbpedia(sentences)
    ground_truth_score = number_of_direct_links_in_dbpedia(ground_truth)
    correct_scores.append(ground_truth_score)
    
    correct_count = annotation.count("accurate")
    incorrect_count = annotation.count("minor_inaccurate") + annotation.count("major_inaccurate")
    total = correct_count + incorrect_count
    if(total>0):
        if(correct_count==total):
            correct_scores.append(sentences_score)
        if(incorrect_count/total>0.75):
            incorrect_scores.append(sentences_score)
            
print(correct_scores)
print(incorrect_scores)

# write_entries_to_files(checking)