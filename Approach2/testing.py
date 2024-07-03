import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Example text
text = " In 2014, Nigel Milsom won the Doug Moran National Portrait Prize for Nigel Milsom painting \"Uncle Paddy\" and in 2012 Nigel Milsom won the Sulman Prize for Nigel Milsom painting \"Judo House Pt 4 (Golden Mud)\"."

# Process the text
doc = nlp(text)

# Initialize variables
subject_token = None
subject_entity = None

# Iterate over sentences
for sent in doc.sents:
    # Initialize subject token variable
    for token in sent:
        if token.dep_ == 'nsubj':
            subject_token = token
            break  # Break once the subject token is found
    
    # Find the entity that contains the subject token
    if subject_token:
        for ent in sent.ents:
            if subject_token.idx >= ent.start_char and subject_token.idx < ent.end_char:
                subject_entity = ent.text
                break  # Break once the entity containing the subject token is found
        break  # Break once the subject entity is found

if subject_entity:
    print(f"Entity containing the subject token '{subject_token.text}': {subject_entity}")
else:
    print("No suitable entity found.")
