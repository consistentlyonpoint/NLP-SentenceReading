# CS7637_SP24-NLP-SentenceReading

## Overview
This report presents an agent designed to answers simple ques-tions. The agent is prompted with both a statement and question. The agent uses a preprocessed library of common words to return a one-word response. The agent’s preprocessed library utilized the natural language processing capability in the spaCy library.

## Description
### Preprocessed Data
The agent is designed with several preprocessed dictionaries and lists. To begin with, all values in the “mostcommon.txt” file are keys in the largest preprocessed dictionary, and each key’s value is a nested dictionary. The nested dictionary’s key-value pairs are the spaCy assigned simple and detailed “part-of-speech” tags. Figure 1, below, represents a portion of the largest preprocessed dictionary. 
<figure>
  <img src="https://github.gatech.edu/storage/user/36047/files/9947bf1c-3375-4997-9d35-2a3099ebf97b"
 alt="Preprocessing">
  <figcaption>Figure 1: Figure 1—	Snippet of python dictionary with keys from the “mostcommon.txt” file and values from spaCy assignement.</figcaption>
</figure>

Next, the agent includes a dictionary with the “5Ws” (“who”, “what”, “when”, “where”, “how”, and “why”) as keys. The value for each key is equal to the part of speech associated with an answer to the key. In addition to the “5Ws”, t agent includes “whose” and “which” in the keys of the dictionary.
In addition, several lists are predefined. These include lists for prepositions, arti-cles, conjunctions, timestamps, days of the week, and common adjectives.

### Runtime Processed Data
At runtime, the agent is prompted with two strings, “sentence” and “question”. The agent splits each string into separate lists. Next, the agent generates a list of proper nouns in the prompt based on the proper nouns in the preprocessed dic-tionary, see Figure 1 above. After, the agent generates a thematic role dictionary for the sentence. 
Finally, the agent generates a list of possible response words from the “sentence” list by eliminating certain “parts-of-speech” words also present in the “question” list.

### Logic
The agent determines the question word (“W” of the “5Ws”) in the prompted question. For each of the “5Ws”, the agent has specific logic to solve the prompt. First, for a “who” prompt, the agent identifies the proper nouns and pronouns of the sentence, and based on the question, will return the name or pronoun associ-ated with the subject or object of the sentence.
Second, for a “whose” prompt, the agent identifies all nouns in the sentence with a “possessive ending”. 
Third, for a “what” prompt, the agent determines the part of speech for the word following “what”. Each simple and/or detailed “part-of-speech” has individual actions.
Fourth, for a “where” prompt, the agent first eliminates possible answer words that are found in some of the preprocessed lists, such as the conjunctions list and proper noun list. Next, the agent looks for prepositions, and the agent makes a list of objects of all prepositional phrases. The agent returns an element from the list determined to be a location.
Fifth, for a “when” prompt, the agent performs an elimination process as in the case of a “where” prompt, and a preposition search. However, the agent includes “NUM” as a part of speech option for the objects of the prepositional phrases.
Sixth, for a “how” prompt, the agent performs a part of speech search on the subsequent word, as in the case of a “what” prompt. 
Seventh, for a “why” prompt, the agent looks for nouns and participles following subordinating conjunctions. Additionally, the agent searches for objects of prep-ositional phrases, but the agent does this if and only if there are no subordinating conjunctions. 
Eighth, for a “which” prompt, the agent determines if the prompt question in-cludes a proper noun, or pronoun. For first and third person pronouns, the agent returns the object of the sentence. For second person pronouns, the agent finds the position of the object of the question in the sentence, and the agent returns the subject or object of the sentence based on the position. If the agent does not find a pronoun or proper noun in the question, the agent will return the subject of the sentence.

## Performance
For sentence prompts, the agent fails with passive voice sentences, and with sen-tences written with an auxiliary verb. Similarly, for questions, the agent fails for questions using a linking verb, and the agent fails with passive voice questions.

## Efficiency
The agent includes several instances of “nested for-loops”. The worst-case per-formance, for both time and space complexity, is O(n2), with n representing the length of the input question or sentence. Therefore, the agent solves in exponen-tial time.
