from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree


# Define a function to extract entities using NLTK's ne_chunk function
def get_ner(pure_text: str) -> list[(str, str)]:
    entities = []
    tree = ne_chunk(pos_tag(word_tokenize(pure_text)))
    for node in tree:
        if type(node) is Tree:
            entity = ' '.join(word for word, tag in node.leaves())
            if node.label() == 'PERSON':
                entities.append((entity, 'PERSON'))
            elif node.label() == 'GPE':
                entities.append((entity, 'LOCATION'))
            elif node.label() == 'ORGANIZATION':
                entities.append((entity, 'ORGANIZATION'))
    return list(set(entities))
