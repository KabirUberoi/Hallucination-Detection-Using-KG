# Per Sentence, Subject Based Link Forming Approach

## Features 

1. **Link Formation:** Links are formed between the subject of each sentence and all other entities in that sentence.
2. **Scoring:** The score is calculated as the fraction of links that are present in Wikidata over the total links in each sentence individually. Sentences with no possible links are ignored for scoring.
3. **Character Handling:** Special characters except `.`, `,`, `"`, `'`, `-` are removed only.
4. **Confidence Score:** The confidence score is increased from 0.35 to 0.5.
5. **Testing Criteria:** Only test cases where the score for the ground truth is > 0.1 are considered. This ensures that only cases where the subject is correctly identified and linked to the correct real-world person are tested.
6. **Pre-processing:** Sentences are pre-processed to ensure each new sentence is on a new line and ends with a period to increase accuracy.

## Main Problems

1. **Subject Extraction Issue:**
   - Example: In the passage:
     ```
     Richard Keith Mahler (August 5, 1953 in Austin, Texas - March 2, 2005 in Jupiter, Florida) was a starting pitcher in Major League Baseball who played for the Atlanta Braves (1979-1988, 1991), Cincinnati Reds (1989-1990) and Montreal Expos (1991).
     ```
     The subject is being linked to ```Gustav Mahler``` instead of ```Richard Mahler```.

2. **No Direct Link Exists:**
   - Example: The system forms a link between "John_Russell_Reynolds" and "Neurology". There is no direct link between them, hence this link is given a score of 0. However, there is a link between "John_Russell_Reynolds" and "Neurologist".

## Scores Achieved

- **Accurate Sentence:** 0.54
- **Minor Inaccurate Sentences:** 0.39
- **Major Inaccurate Sentences:** 0.28

On 846 test cases:
- Accurate: 590
- Minor Inaccurate: 141
- Major Inaccurate: 115
