# All Link Forming Approach

## Features

1. **Link Formation**: Links are created between all entities that lie in the same sentence.
2. **Scoring**: Each paragraph is scored as the fraction of links that are present in Wikidata divided by the total links in the paragraph, rather than at the sentence level.
3. **Special Symbol Handling**: All special symbols are removed, but three-worded names are retained.

## Problems

1. **Indirect Links**: Links are formed between objects that do not have direct links.
   - **Example**: 
     - **Sentence**: `Kabir is a maths student and an instrument player.`
     - **Issue**: A link is made between "maths student" and "instrument player," which is unlikely to be present in the knowledge graph.
   
2. **Wrongful Subject Extraction**: Subjects are sometimes extracted incorrectly, and there is no straightforward way to detect when this happens.

3. **Paragraph-Level Scoring**: Scoring at the paragraph level means that if most links are correct and only one is incorrect, the paragraph's score remains high.

4. **Same Issues as Version 2**: The approach still suffers from issues present in version 2 of the method.

## Scores Achieved

- **Incorrect Sentences**: 0.2
- **Correct Sentences**: 0.18

Based on 476 test cases.
