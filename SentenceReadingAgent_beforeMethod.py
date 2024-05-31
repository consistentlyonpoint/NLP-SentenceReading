# import spacy
# import pathlib
class SentenceReadingAgent:
    def __init__(self):
        # If you want to do any initial processing, add it here.
        self.mode_dict = {'Serena': {'pos': 'PROPN', 'tag': 'NNP'}, 'Andrew': {'pos': 'PROPN', 'tag': 'NNP'},
                     'Bobbie': {'pos': 'PROPN', 'tag': 'NNP'}, 'Cason': {'pos': 'PROPN', 'tag': 'NNP'},
                     'David': {'pos': 'PROPN', 'tag': 'NNP'}, 'Farzana': {'pos': 'PROPN', 'tag': 'NNP'},
                     'Frank': {'pos': 'PROPN', 'tag': 'NNP'}, 'Hannah': {'pos': 'PROPN', 'tag': 'NNP'},
                     'Ida': {'pos': 'PROPN', 'tag': 'NNP'}, 'Irene': {'pos': 'PROPN', 'tag': 'NNP'},
                     'Jim': {'pos': 'PROPN', 'tag': 'NNP'}, 'Jose': {'pos': 'PROPN', 'tag': 'NNP'},
                     'Keith': {'pos': 'PROPN', 'tag': 'NNP'}, 'Laura': {'pos': 'PROPN', 'tag': 'NNP'},
                     'Lucy': {'pos': 'PROPN', 'tag': 'NNP'}, 'Meredith': {'pos': 'PROPN', 'tag': 'NNP'},
                     'Nick': {'pos': 'PROPN', 'tag': 'NNP'}, 'Ada': {'pos': 'PROPN', 'tag': 'NNP'},
                     'Yeeling': {'pos': 'PROPN', 'tag': 'NNP'}, 'Yan': {'pos': 'PROPN', 'tag': 'NNP'},
                     'the': {'pos': 'PRON', 'tag': 'DT'}, 'of': {'pos': 'ADP', 'tag': 'IN'},
                     'to': {'pos': 'PART', 'tag': 'TO'}, 'do': {'pos': 'AUX', 'tag': 'VBP'},
                     'run': {'pos': 'NOUN', 'tag': 'NN'}, 'sleep': {'pos': 'NOUN', 'tag': 'NN'},
                     'cook': {'pos': 'VERB', 'tag': 'VB'}, 'eat': {'pos': 'VERB', 'tag': 'VB'},
                     'drink': {'pos': 'VERB', 'tag': 'VB'}, 'learn': {'pos': 'VERB', 'tag': 'VB'},
                     'write': {'pos': 'VERB', 'tag': 'VB'}, 'read': {'pos': 'VERB', 'tag': 'VBN'},
                     'think': {'pos': 'NOUN', 'tag': 'NN'}, 'dream': {'pos': 'VERB', 'tag': 'VB'},
                     'drive': {'pos': 'NOUN', 'tag': 'NN'}, 'walk': {'pos': 'VERB', 'tag': 'VB'},
                     'sit': {'pos': 'VERB', 'tag': 'VB'}, 'jump': {'pos': 'VERB', 'tag': 'VB'},
                     'and': {'pos': 'CCONJ', 'tag': 'CC'}, 'a': {'pos': 'PRON', 'tag': 'DT'},
                     'in': {'pos': 'ADP', 'tag': 'IN'}, 'is': {'pos': 'AUX', 'tag': 'VBZ'},
                     'it': {'pos': 'PRON', 'tag': 'PRP'}, 'you': {'pos': 'PRON', 'tag': 'PRP'},
                     'that': {'pos': 'SCONJ', 'tag': 'IN'}, 'he': {'pos': 'PRON', 'tag': 'PRP'},
                     'was': {'pos': 'AUX', 'tag': 'VBD'}, 'for': {'pos': 'ADP', 'tag': 'IN'},
                     'on': {'pos': 'ADP', 'tag': 'IN'}, 'are': {'pos': 'AUX', 'tag': 'VBP'},
                     'with': {'pos': 'ADP', 'tag': 'IN'}, 'as': {'pos': 'ADP', 'tag': 'IN'},
                     'I': {'pos': 'PRON', 'tag': 'PRP'}, 'his': {'pos': 'PRON', 'tag': 'PRP$'},
                     'they': {'pos': 'PRON', 'tag': 'PRP'}, 'be': {'pos': 'VERB', 'tag': 'VBP'},
                     'at': {'pos': 'ADP', 'tag': 'IN'}, 'have': {'pos': 'VERB', 'tag': 'VBP'},
                     'this': {'pos': 'PRON', 'tag': 'DT'}, 'from': {'pos': 'ADP', 'tag': 'IN'},
                     'or': {'pos': 'CCONJ', 'tag': 'CC'}, 'had': {'pos': 'VERB', 'tag': 'VBD'},
                     'by': {'pos': 'ADP', 'tag': 'IN'}, 'hot': {'pos': 'ADJ', 'tag': 'JJ'},
                     'but': {'pos': 'CCONJ', 'tag': 'CC'}, 'some': {'pos': 'DET', 'tag': 'DT'},
                     'what': {'pos': 'PRON', 'tag': 'WP'}, 'there': {'pos': 'PRON', 'tag': 'EX'},
                     'we': {'pos': 'PRON', 'tag': 'PRP'}, 'can': {'pos': 'AUX', 'tag': 'MD'},
                     'out': {'pos': 'ADP', 'tag': 'RP'}, 'other': {'pos': 'ADJ', 'tag': 'JJ'},
                     'were': {'pos': 'AUX', 'tag': 'VBD'}, 'all': {'pos': 'ADV', 'tag': 'RB'},
                     'your': {'pos': 'PRON', 'tag': 'PRP$'}, 'when': {'pos': 'SCONJ', 'tag': 'WRB'},
                     'up': {'pos': 'NOUN', 'tag': 'NN'}, 'use': {'pos': 'VERB', 'tag': 'VB'},
                     'word': {'pos': 'NOUN', 'tag': 'NN'}, 'how': {'pos': 'SCONJ', 'tag': 'WRB'},
                     'said': {'pos': 'VERB', 'tag': 'VBD'}, 'an': {'pos': 'DET', 'tag': 'DT'},
                     'each': {'pos': 'DET', 'tag': 'DT'}, 'she': {'pos': 'PRON', 'tag': 'PRP'},
                     'which': {'pos': 'PRON', 'tag': 'WDT'}, 'their': {'pos': 'PRON', 'tag': 'PRP$'},
                     'time': {'pos': 'NOUN', 'tag': 'NN'}, 'if': {'pos': 'SCONJ', 'tag': 'IN'},
                     'will': {'pos': 'AUX', 'tag': 'MD'}, 'way': {'pos': 'NOUN', 'tag': 'NN'},
                     'about': {'pos': 'ADV', 'tag': 'RB'}, 'many': {'pos': 'ADJ', 'tag': 'JJ'},
                     'then': {'pos': 'ADV', 'tag': 'RB'}, 'them': {'pos': 'PRON', 'tag': 'PRP'},
                     'would': {'pos': 'AUX', 'tag': 'MD'}, 'wrote': {'pos': 'VERB', 'tag': 'VBN'},
                     'like': {'pos': 'INTJ', 'tag': 'UH'}, 'so': {'pos': 'ADV', 'tag': 'RB'},
                     'these': {'pos': 'DET', 'tag': 'DT'}, 'her': {'pos': 'PRON', 'tag': 'PRP$'},
                     'long': {'pos': 'ADJ', 'tag': 'JJ'}, 'make': {'pos': 'VERB', 'tag': 'VB'},
                     'thing': {'pos': 'NOUN', 'tag': 'NN'}, 'see': {'pos': 'VERB', 'tag': 'VBP'},
                     'him': {'pos': 'PRON', 'tag': 'PRP'}, 'has': {'pos': 'AUX', 'tag': 'VBZ'},
                     'look': {'pos': 'VERB', 'tag': 'VB'}, 'more': {'pos': 'ADV', 'tag': 'RBR'},
                     'day': {'pos': 'NOUN', 'tag': 'NN'}, 'could': {'pos': 'AUX', 'tag': 'MD'},
                     'go': {'pos': 'AUX', 'tag': 'VB'}, 'come': {'pos': 'NOUN', 'tag': 'NN'},
                     'did': {'pos': 'AUX', 'tag': 'VBD'}, 'my': {'pos': 'PRON', 'tag': 'PRP$'},
                     'sound': {'pos': 'NOUN', 'tag': 'NN'}, 'no': {'pos': 'DET', 'tag': 'DT'},
                     'most': {'pos': 'ADJ', 'tag': 'JJS'}, 'number': {'pos': 'NOUN', 'tag': 'NN'},
                     'who': {'pos': 'PRON', 'tag': 'WP'}, 'over': {'pos': 'ADV', 'tag': 'RB'},
                     'know': {'pos': 'VERB', 'tag': 'VB'}, 'water': {'pos': 'NOUN', 'tag': 'NN'},
                     'than': {'pos': 'ADP', 'tag': 'IN'}, 'call': {'pos': 'VERB', 'tag': 'VB'},
                     'first': {'pos': 'ADJ', 'tag': 'JJ'}, 'people': {'pos': 'NOUN', 'tag': 'NNS'},
                     'may': {'pos': 'AUX', 'tag': 'MD'}, 'down': {'pos': 'ADP', 'tag': 'RP'},
                     'side': {'pos': 'NOUN', 'tag': 'NN'}, 'been': {'pos': 'AUX', 'tag': 'VBN'},
                     'now': {'pos': 'ADV', 'tag': 'RB'}, 'find': {'pos': 'VERB', 'tag': 'VBP'},
                     'any': {'pos': 'DET', 'tag': 'DT'}, 'new': {'pos': 'ADJ', 'tag': 'JJ'},
                     'work': {'pos': 'NOUN', 'tag': 'NN'}, 'part': {'pos': 'NOUN', 'tag': 'NN'},
                     'take': {'pos': 'VERB', 'tag': 'VB'}, 'get': {'pos': 'NOUN', 'tag': 'NN'},
                     'place': {'pos': 'NOUN', 'tag': 'NN'}, 'made': {'pos': 'VERB', 'tag': 'VBN'},
                     'live': {'pos': 'VERB', 'tag': 'VB'}, 'where': {'pos': 'SCONJ', 'tag': 'WRB'},
                     'after': {'pos': 'ADP', 'tag': 'IN'}, 'back': {'pos': 'ADV', 'tag': 'RB'},
                     'little': {'pos': 'ADJ', 'tag': 'JJ'}, 'only': {'pos': 'ADV', 'tag': 'RB'},
                     'round': {'pos': 'ADJ', 'tag': 'JJ'}, 'man': {'pos': 'NOUN', 'tag': 'NN'},
                     'year': {'pos': 'NOUN', 'tag': 'NN'}, 'came': {'pos': 'VERB', 'tag': 'VBD'},
                     'show': {'pos': 'NOUN', 'tag': 'NN'}, 'every': {'pos': 'DET', 'tag': 'DT'},
                     'good': {'pos': 'ADJ', 'tag': 'JJ'}, 'me': {'pos': 'PRON', 'tag': 'PRP'},
                     'give': {'pos': 'VERB', 'tag': 'VB'}, 'our': {'pos': 'PRON', 'tag': 'PRP$'},
                     'under': {'pos': 'ADP', 'tag': 'IN'}, 'name': {'pos': 'NOUN', 'tag': 'NN'},
                     'very': {'pos': 'ADV', 'tag': 'RB'}, 'through': {'pos': 'ADP', 'tag': 'IN'},
                     'just': {'pos': 'ADV', 'tag': 'RB'}, 'form': {'pos': 'VERB', 'tag': 'VB'},
                     'much': {'pos': 'ADJ', 'tag': 'JJ'}, 'great': {'pos': 'ADJ', 'tag': 'JJ'},
                     'say': {'pos': 'VERB', 'tag': 'VBP'}, 'help': {'pos': 'VERB', 'tag': 'VB'},
                     'low': {'pos': 'ADJ', 'tag': 'JJ'}, 'line': {'pos': 'NOUN', 'tag': 'NN'},
                     'before': {'pos': 'SCONJ', 'tag': 'IN'}, 'turn': {'pos': 'NOUN', 'tag': 'NN'},
                     'cause': {'pos': 'NOUN', 'tag': 'NN'}, 'same': {'pos': 'ADJ', 'tag': 'JJ'},
                     'mean': {'pos': 'NOUN', 'tag': 'NN'}, 'differ': {'pos': 'VERB', 'tag': 'VBP'},
                     'move': {'pos': 'NOUN', 'tag': 'NN'}, 'right': {'pos': 'ADJ', 'tag': 'JJ'},
                     'boy': {'pos': 'NOUN', 'tag': 'NN'}, 'old': {'pos': 'ADJ', 'tag': 'JJ'},
                     'too': {'pos': 'ADV', 'tag': 'RB'}, 'does': {'pos': 'AUX', 'tag': 'VBZ'},
                     'tell': {'pos': 'VERB', 'tag': 'VB'}, 'sentence': {'pos': 'NOUN', 'tag': 'NN'},
                     'set': {'pos': 'VERB', 'tag': 'VBD'}, 'want': {'pos': 'VERB', 'tag': 'VB'},
                     'air': {'pos': 'NOUN', 'tag': 'NN'}, 'well': {'pos': 'ADV', 'tag': 'RB'},
                     'also': {'pos': 'ADV', 'tag': 'RB'}, 'play': {'pos': 'VERB', 'tag': 'VBP'},
                     'small': {'pos': 'ADJ', 'tag': 'JJ'}, 'end': {'pos': 'NOUN', 'tag': 'NN'},
                     'put': {'pos': 'VERB', 'tag': 'VBN'}, 'home': {'pos': 'NOUN', 'tag': 'NN'},
                     'hand': {'pos': 'NOUN', 'tag': 'NN'}, 'port': {'pos': 'NOUN', 'tag': 'NN'},
                     'large': {'pos': 'ADJ', 'tag': 'JJ'}, 'spell': {'pos': 'NOUN', 'tag': 'NN'},
                     'add': {'pos': 'VERB', 'tag': 'VB'}, 'even': {'pos': 'ADV', 'tag': 'RB'},
                     'land': {'pos': 'NOUN', 'tag': 'NN'}, 'here': {'pos': 'ADV', 'tag': 'RB'},
                     'must': {'pos': 'AUX', 'tag': 'MD'}, 'big': {'pos': 'ADJ', 'tag': 'JJ'},
                     'high': {'pos': 'ADJ', 'tag': 'JJ'}, 'such': {'pos': 'ADJ', 'tag': 'JJ'},
                     'follow': {'pos': 'NOUN', 'tag': 'NN'}, 'act': {'pos': 'NOUN', 'tag': 'NN'},
                     'why': {'pos': 'SCONJ', 'tag': 'WRB'}, 'ask': {'pos': 'VERB', 'tag': 'VB'},
                     'men': {'pos': 'NOUN', 'tag': 'NNS'}, 'change': {'pos': 'NOUN', 'tag': 'NN'},
                     'went': {'pos': 'VERB', 'tag': 'VBD'}, 'light': {'pos': 'ADJ', 'tag': 'JJ'},
                     'kind': {'pos': 'NOUN', 'tag': 'NN'}, 'off': {'pos': 'ADP', 'tag': 'RP'},
                     'need': {'pos': 'NOUN', 'tag': 'NN'}, 'house': {'pos': 'NOUN', 'tag': 'NN'},
                     'picture': {'pos': 'NOUN', 'tag': 'NN'}, 'try': {'pos': 'VERB', 'tag': 'VBP'},
                     'us': {'pos': 'PRON', 'tag': 'PRP'}, 'again': {'pos': 'ADV', 'tag': 'RB'},
                     'animal': {'pos': 'NOUN', 'tag': 'NN'}, 'point': {'pos': 'NOUN', 'tag': 'NN'},
                     'mother': {'pos': 'NOUN', 'tag': 'NN'}, 'world': {'pos': 'NOUN', 'tag': 'NN'},
                     'near': {'pos': 'ADP', 'tag': 'IN'}, 'build': {'pos': 'VERB', 'tag': 'VB'},
                     'self': {'pos': 'NOUN', 'tag': 'NN'}, 'earth': {'pos': 'NOUN', 'tag': 'NN'},
                     'father': {'pos': 'NOUN', 'tag': 'NN'}, 'head': {'pos': 'NOUN', 'tag': 'NN'},
                     'stand': {'pos': 'VERB', 'tag': 'VB'}, 'own': {'pos': 'ADJ', 'tag': 'JJ'},
                     'page': {'pos': 'NOUN', 'tag': 'NN'}, 'should': {'pos': 'AUX', 'tag': 'MD'},
                     'country': {'pos': 'NOUN', 'tag': 'NN'}, 'found': {'pos': 'VERB', 'tag': 'VBN'},
                     'answer': {'pos': 'NOUN', 'tag': 'NN'}, 'school': {'pos': 'NOUN', 'tag': 'NN'},
                     'grow': {'pos': 'VERB', 'tag': 'VB'}, 'study': {'pos': 'NOUN', 'tag': 'NN'},
                     'still': {'pos': 'ADV', 'tag': 'RB'}, 'plant': {'pos': 'NOUN', 'tag': 'NN'},
                     'cover': {'pos': 'VERB', 'tag': 'VB'}, 'food': {'pos': 'NOUN', 'tag': 'NN'},
                     'sun': {'pos': 'NOUN', 'tag': 'NN'}, 'thought': {'pos': 'NOUN', 'tag': 'NN'},
                     'let': {'pos': 'AUX', 'tag': 'VBN'}, 'keep': {'pos': 'VERB', 'tag': 'VB'},
                     'eye': {'pos': 'NOUN', 'tag': 'NN'}, 'never': {'pos': 'ADV', 'tag': 'RB'},
                     'last': {'pos': 'ADJ', 'tag': 'JJ'}, 'door': {'pos': 'NOUN', 'tag': 'NN'},
                     'between': {'pos': 'ADP', 'tag': 'IN'}, 'city': {'pos': 'NOUN', 'tag': 'NN'},
                     'tree': {'pos': 'NOUN', 'tag': 'NN'}, 'cross': {'pos': 'NOUN', 'tag': 'NN'},
                     'since': {'pos': 'ADV', 'tag': 'RB'}, 'hard': {'pos': 'ADJ', 'tag': 'JJ'},
                     'start': {'pos': 'NOUN', 'tag': 'NN'}, 'might': {'pos': 'AUX', 'tag': 'MD'},
                     'story': {'pos': 'NOUN', 'tag': 'NN'}, 'saw': {'pos': 'VERB', 'tag': 'VBD'},
                     'far': {'pos': 'ADV', 'tag': 'RB'}, 'sea': {'pos': 'NOUN', 'tag': 'NN'},
                     'draw': {'pos': 'NOUN', 'tag': 'NN'}, 'left': {'pos': 'VERB', 'tag': 'VBN'},
                     'late': {'pos': 'ADJ', 'tag': 'JJ'}, "n't": {'pos': 'PART', 'tag': 'RB'},
                     'while': {'pos': 'SCONJ', 'tag': 'IN'}, 'press': {'pos': 'NOUN', 'tag': 'NN'},
                     'close': {'pos': 'ADJ', 'tag': 'JJ'}, 'night': {'pos': 'NOUN', 'tag': 'NN'},
                     'real': {'pos': 'ADJ', 'tag': 'JJ'}, 'life': {'pos': 'NOUN', 'tag': 'NN'},
                     'few': {'pos': 'ADJ', 'tag': 'JJ'}, 'stop': {'pos': 'VERB', 'tag': 'VB'},
                     'open': {'pos': 'ADJ', 'tag': 'JJ'}, 'seem': {'pos': 'VERB', 'tag': 'VBP'},
                     'together': {'pos': 'ADV', 'tag': 'RB'}, 'next': {'pos': 'ADJ', 'tag': 'JJ'},
                     'white': {'pos': 'ADJ', 'tag': 'JJ'}, 'children': {'pos': 'NOUN', 'tag': 'NNS'},
                     'begin': {'pos': 'VERB', 'tag': 'VBP'}, 'got': {'pos': 'AUX', 'tag': 'VBD'},
                     'example': {'pos': 'NOUN', 'tag': 'NN'}, 'ease': {'pos': 'NOUN', 'tag': 'NN'},
                     'paper': {'pos': 'NOUN', 'tag': 'NN'}, 'often': {'pos': 'ADV', 'tag': 'RB'},
                     'always': {'pos': 'ADV', 'tag': 'RB'}, 'music': {'pos': 'NOUN', 'tag': 'NN'},
                     'those': {'pos': 'DET', 'tag': 'DT'}, 'both': {'pos': 'CCONJ', 'tag': 'CC'},
                     'mark': {'pos': 'NOUN', 'tag': 'NN'}, 'book': {'pos': 'NOUN', 'tag': 'NN'},
                     'letter': {'pos': 'NOUN', 'tag': 'NN'}, 'until': {'pos': 'SCONJ', 'tag': 'IN'},
                     'mile': {'pos': 'NOUN', 'tag': 'NN'}, 'river': {'pos': 'NOUN', 'tag': 'NN'},
                     'car': {'pos': 'NOUN', 'tag': 'NN'}, 'feet': {'pos': 'NOUN', 'tag': 'NNS'},
                     'care': {'pos': 'NOUN', 'tag': 'NN'}, 'second': {'pos': 'ADJ', 'tag': 'JJ'},
                     'group': {'pos': 'NOUN', 'tag': 'NN'}, 'carry': {'pos': 'NOUN', 'tag': 'NN'},
                     'took': {'pos': 'VERB', 'tag': 'VBD'}, 'rain': {'pos': 'NOUN', 'tag': 'NN'},
                     'room': {'pos': 'NOUN', 'tag': 'NN'}, 'friend': {'pos': 'NOUN', 'tag': 'NN'},
                     'began': {'pos': 'VERB', 'tag': 'VBD'}, 'idea': {'pos': 'NOUN', 'tag': 'NN'},
                     'fish': {'pos': 'NOUN', 'tag': 'NN'}, 'mountain': {'pos': 'NOUN', 'tag': 'NN'},
                     'north': {'pos': 'NOUN', 'tag': 'NN'}, 'once': {'pos': 'ADV', 'tag': 'RB'},
                     'base': {'pos': 'NOUN', 'tag': 'NN'}, 'hear': {'pos': 'VERB', 'tag': 'VBP'},
                     'horse': {'pos': 'NOUN', 'tag': 'NN'}, 'cut': {'pos': 'NOUN', 'tag': 'NN'},
                     'sure': {'pos': 'ADJ', 'tag': 'JJ'}, 'watch': {'pos': 'VERB', 'tag': 'VB'},
                     'color': {'pos': 'NOUN', 'tag': 'NN'}, 'face': {'pos': 'NOUN', 'tag': 'NN'},
                     'wood': {'pos': 'NOUN', 'tag': 'NN'}, 'main': {'pos': 'ADJ', 'tag': 'JJ'},
                     'enough': {'pos': 'ADJ', 'tag': 'JJ'}, 'plain': {'pos': 'ADJ', 'tag': 'JJ'},
                     'girl': {'pos': 'NOUN', 'tag': 'NN'}, 'usual': {'pos': 'ADJ', 'tag': 'JJ'},
                     'young': {'pos': 'ADJ', 'tag': 'JJ'}, 'ready': {'pos': 'ADJ', 'tag': 'JJ'},
                     'above': {'pos': 'ADP', 'tag': 'IN'}, 'ever': {'pos': 'ADV', 'tag': 'RB'},
                     'red': {'pos': 'ADJ', 'tag': 'JJ'}, 'Red': {'pos': 'ADJ', 'tag': 'JJ'},
                     'list': {'pos': 'NOUN', 'tag': 'NN'}, 'though': {'pos': 'ADV', 'tag': 'RB'},
                     'feel': {'pos': 'VERB', 'tag': 'VB'}, 'talk': {'pos': 'NOUN', 'tag': 'NN'},
                     'bird': {'pos': 'NOUN', 'tag': 'NN'}, 'soon': {'pos': 'ADV', 'tag': 'RB'},
                     'body': {'pos': 'NOUN', 'tag': 'NN'}, 'dog': {'pos': 'NOUN', 'tag': 'NN'},
                     'dogs': {'pos': 'NOUN', 'tag': 'NNS'}, "'s": {'pos': 'PART', 'tag': 'POS'},
                     'family': {'pos': 'NOUN', 'tag': 'NN'}, 'direct': {'pos': 'ADJ', 'tag': 'JJ'},
                     'pose': {'pos': 'NOUN', 'tag': 'NN'}, 'leave': {'pos': 'VERB', 'tag': 'VBP'},
                     'song': {'pos': 'NOUN', 'tag': 'NN'}, 'measure': {'pos': 'NOUN', 'tag': 'NN'},
                     'state': {'pos': 'NOUN', 'tag': 'NN'}, 'product': {'pos': 'NOUN', 'tag': 'NN'},
                     'black': {'pos': 'ADJ', 'tag': 'JJ'}, 'short': {'pos': 'ADJ', 'tag': 'JJ'},
                     'numeral': {'pos': 'ADJ', 'tag': 'JJ'}, 'class': {'pos': 'NOUN', 'tag': 'NN'},
                     'wind': {'pos': 'NOUN', 'tag': 'NN'}, 'question': {'pos': 'NOUN', 'tag': 'NN'},
                     'happen': {'pos': 'VERB', 'tag': 'VB'}, 'complete': {'pos': 'ADJ', 'tag': 'JJ'},
                     'ship': {'pos': 'NOUN', 'tag': 'NN'}, 'area': {'pos': 'NOUN', 'tag': 'NN'},
                     'half': {'pos': 'ADJ', 'tag': 'JJ'}, 'rock': {'pos': 'NOUN', 'tag': 'NN'},
                     'order': {'pos': 'NOUN', 'tag': 'NN'}, 'fire': {'pos': 'NOUN', 'tag': 'NN'},
                     'south': {'pos': 'ADJ', 'tag': 'JJ'}, 'problem': {'pos': 'NOUN', 'tag': 'NN'},
                     'piece': {'pos': 'NOUN', 'tag': 'NN'}, 'told': {'pos': 'VERB', 'tag': 'VBD'},
                     'knew': {'pos': 'VERB', 'tag': 'VBD'}, 'pass': {'pos': 'VERB', 'tag': 'VB'},
                     'farm': {'pos': 'NOUN', 'tag': 'NN'}, 'top': {'pos': 'ADJ', 'tag': 'JJ'},
                     'whole': {'pos': 'ADJ', 'tag': 'JJ'}, 'king': {'pos': 'NOUN', 'tag': 'NN'},
                     'size': {'pos': 'NOUN', 'tag': 'NN'}, 'heard': {'pos': 'VERB', 'tag': 'VBD'},
                     'best': {'pos': 'ADJ', 'tag': 'JJS'}, 'hour': {'pos': 'NOUN', 'tag': 'NN'},
                     'better': {'pos': 'ADJ', 'tag': 'JJR'}, 'true': {'pos': 'ADJ', 'tag': 'JJ'},
                     'during': {'pos': 'ADP', 'tag': 'IN'}, 'hundred': {'pos': 'NUM', 'tag': 'CD'},
                     'am': {'pos': 'AUX', 'tag': 'VBP'}, 'remember': {'pos': 'VERB', 'tag': 'VB'},
                     'step': {'pos': 'NOUN', 'tag': 'NN'}, 'early': {'pos': 'ADJ', 'tag': 'JJ'},
                     'hold': {'pos': 'VERB', 'tag': 'VB'}, 'west': {'pos': 'NOUN', 'tag': 'NN'},
                     'ground': {'pos': 'NOUN', 'tag': 'NN'}, 'interest': {'pos': 'NOUN', 'tag': 'NN'},
                     'reach': {'pos': 'VERB', 'tag': 'VBP'}, 'fast': {'pos': 'ADJ', 'tag': 'JJ'},
                     'sing': {'pos': 'NOUN', 'tag': 'NN'}, 'sings': {'pos': 'NOUN', 'tag': 'NNS'},
                     'listen': {'pos': 'VERB', 'tag': 'VBP'}, 'table': {'pos': 'NOUN', 'tag': 'NN'},
                     'travel': {'pos': 'NOUN', 'tag': 'NN'}, 'less': {'pos': 'ADJ', 'tag': 'JJR'},
                     'morning': {'pos': 'NOUN', 'tag': 'NN'}, 'simple': {'pos': 'ADJ', 'tag': 'JJ'},
                     'several': {'pos': 'ADJ', 'tag': 'JJ'}, 'vowel': {'pos': 'NOUN', 'tag': 'NN'},
                     'toward': {'pos': 'ADP', 'tag': 'IN'}, 'war': {'pos': 'NOUN', 'tag': 'NN'},
                     'lay': {'pos': 'VERB', 'tag': 'VBD'}, 'against': {'pos': 'ADP', 'tag': 'IN'},
                     'pattern': {'pos': 'NOUN', 'tag': 'NN'}, 'slow': {'pos': 'ADJ', 'tag': 'JJ'},
                     'center': {'pos': 'NOUN', 'tag': 'NN'}, 'love': {'pos': 'NOUN', 'tag': 'NN'},
                     'person': {'pos': 'NOUN', 'tag': 'NN'}, 'money': {'pos': 'NOUN', 'tag': 'NN'},
                     'serve': {'pos': 'VERB', 'tag': 'VBP'}, 'appear': {'pos': 'VERB', 'tag': 'VB'},
                     'road': {'pos': 'NOUN', 'tag': 'NN'}, 'map': {'pos': 'NOUN', 'tag': 'NN'},
                     'science': {'pos': 'NOUN', 'tag': 'NN'}, 'rule': {'pos': 'NOUN', 'tag': 'NN'},
                     'govern': {'pos': 'NOUN', 'tag': 'NN'}, 'pull': {'pos': 'VERB', 'tag': 'VB'},
                     'cold': {'pos': 'ADJ', 'tag': 'JJ'}, 'notice': {'pos': 'NOUN', 'tag': 'NN'},
                     'voice': {'pos': 'NOUN', 'tag': 'NN'}, 'fall': {'pos': 'NOUN', 'tag': 'NN'},
                     'power': {'pos': 'NOUN', 'tag': 'NN'}, 'town': {'pos': 'NOUN', 'tag': 'NN'},
                     'fine': {'pos': 'ADJ', 'tag': 'JJ'}, 'certain': {'pos': 'ADJ', 'tag': 'JJ'},
                     'fly': {'pos': 'NOUN', 'tag': 'NN'}, 'unit': {'pos': 'NOUN', 'tag': 'NN'},
                     'lead': {'pos': 'VERB', 'tag': 'VBP'}, 'cry': {'pos': 'NOUN', 'tag': 'NN'},
                     'dark': {'pos': 'ADJ', 'tag': 'JJ'}, 'machine': {'pos': 'NOUN', 'tag': 'NN'},
                     'note': {'pos': 'NOUN', 'tag': 'NN'}, 'wait': {'pos': 'VERB', 'tag': 'VB'},
                     'plan': {'pos': 'NOUN', 'tag': 'NN'}, 'figure': {'pos': 'NOUN', 'tag': 'NN'},
                     'star': {'pos': 'NOUN', 'tag': 'NN'}, 'box': {'pos': 'NOUN', 'tag': 'NN'},
                     'noun': {'pos': 'NOUN', 'tag': 'NN'}, 'field': {'pos': 'NOUN', 'tag': 'NN'},
                     'rest': {'pos': 'NOUN', 'tag': 'NN'}, 'correct': {'pos': 'ADJ', 'tag': 'JJ'},
                     'able': {'pos': 'ADJ', 'tag': 'JJ'}, 'pound': {'pos': 'NOUN', 'tag': 'NN'},
                     'done': {'pos': 'VERB', 'tag': 'VBN'}, 'beauty': {'pos': 'NOUN', 'tag': 'NN'},
                     'stood': {'pos': 'VERB', 'tag': 'VBD'}, 'contain': {'pos': 'VERB', 'tag': 'VBP'},
                     'front': {'pos': 'ADJ', 'tag': 'JJ'}, 'teach': {'pos': 'NOUN', 'tag': 'NN'},
                     'week': {'pos': 'NOUN', 'tag': 'NN'}, 'final': {'pos': 'ADJ', 'tag': 'JJ'},
                     'gave': {'pos': 'VERB', 'tag': 'VBD'}, 'green': {'pos': 'ADJ', 'tag': 'JJ'},
                     'oh': {'pos': 'ADJ', 'tag': 'JJ'}, 'quick': {'pos': 'ADJ', 'tag': 'JJ'},
                     'develop': {'pos': 'VERB', 'tag': 'VB'}, 'warm': {'pos': 'ADJ', 'tag': 'JJ'},
                     'free': {'pos': 'ADJ', 'tag': 'JJ'}, 'minute': {'pos': 'NOUN', 'tag': 'NN'},
                     'strong': {'pos': 'ADJ', 'tag': 'JJ'}, 'special': {'pos': 'ADJ', 'tag': 'JJ'},
                     'mind': {'pos': 'NOUN', 'tag': 'NN'}, 'behind': {'pos': 'ADP', 'tag': 'IN'},
                     'clear': {'pos': 'ADJ', 'tag': 'JJ'}, 'tail': {'pos': 'NOUN', 'tag': 'NN'},
                     'produce': {'pos': 'NOUN', 'tag': 'NN'}, 'fact': {'pos': 'NOUN', 'tag': 'NN'},
                     'street': {'pos': 'NOUN', 'tag': 'NN'}, 'inch': {'pos': 'NOUN', 'tag': 'NN'},
                     'lot': {'pos': 'NOUN', 'tag': 'NN'}, 'nothing': {'pos': 'PRON', 'tag': 'NN'},
                     'course': {'pos': 'NOUN', 'tag': 'NN'}, 'stay': {'pos': 'VERB', 'tag': 'VB'},
                     'wheel': {'pos': 'NOUN', 'tag': 'NN'}, 'full': {'pos': 'ADJ', 'tag': 'JJ'},
                     'force': {'pos': 'NOUN', 'tag': 'NN'}, 'blue': {'pos': 'ADJ', 'tag': 'JJ'},
                     'object': {'pos': 'NOUN', 'tag': 'NN'}, 'decide': {'pos': 'VERB', 'tag': 'VB'},
                     'surface': {'pos': 'NOUN', 'tag': 'NN'}, 'deep': {'pos': 'ADJ', 'tag': 'JJ'},
                     'moon': {'pos': 'NOUN', 'tag': 'NN'}, 'island': {'pos': 'NOUN', 'tag': 'NN'},
                     'foot': {'pos': 'NOUN', 'tag': 'NN'}, 'yet': {'pos': 'ADV', 'tag': 'RB'},
                     'busy': {'pos': 'ADJ', 'tag': 'JJ'}, 'test': {'pos': 'NOUN', 'tag': 'NN'},
                     'record': {'pos': 'NOUN', 'tag': 'NN'}, 'boat': {'pos': 'NOUN', 'tag': 'NN'},
                     'common': {'pos': 'ADJ', 'tag': 'JJ'}, 'gold': {'pos': 'NOUN', 'tag': 'NN'},
                     'possible': {'pos': 'ADJ', 'tag': 'JJ'}, 'plane': {'pos': 'NOUN', 'tag': 'NN'},
                     'age': {'pos': 'NOUN', 'tag': 'NN'}, 'dry': {'pos': 'ADJ', 'tag': 'JJ'},
                     'wonder': {'pos': 'NOUN', 'tag': 'NN'}, 'laugh': {'pos': 'NOUN', 'tag': 'NN'},
                     'thousand': {'pos': 'NUM', 'tag': 'CD'}, 'ago': {'pos': 'ADP', 'tag': 'IN'},
                     'ran': {'pos': 'VERB', 'tag': 'VBD'}, 'check': {'pos': 'NOUN', 'tag': 'NN'},
                     'game': {'pos': 'NOUN', 'tag': 'NN'}, 'shape': {'pos': 'NOUN', 'tag': 'NN'},
                     'yes': {'pos': 'INTJ', 'tag': 'UH'}, 'cool': {'pos': 'ADJ', 'tag': 'JJ'},
                     'miss': {'pos': 'NOUN', 'tag': 'NN'}, 'brought': {'pos': 'VERB', 'tag': 'VBN'},
                     'heat': {'pos': 'NOUN', 'tag': 'NN'}, 'snow': {'pos': 'NOUN', 'tag': 'NN'},
                     'bed': {'pos': 'NOUN', 'tag': 'NN'}, 'bring': {'pos': 'VERB', 'tag': 'VBP'},
                     'perhaps': {'pos': 'ADV', 'tag': 'RB'}, 'fill': {'pos': 'VERB', 'tag': 'VB'},
                     'east': {'pos': 'NOUN', 'tag': 'NN'}, 'weight': {'pos': 'NOUN', 'tag': 'NN'},
                     'language': {'pos': 'NOUN', 'tag': 'NN'}, 'among': {'pos': 'ADP', 'tag': 'IN'},
                     'adult': {'pos': 'NOUN', 'tag': 'NN'}, 'adults': {'pos': 'NOUN', 'tag': 'NNS'},
                     '00:00': {'pos': 'NUM', 'tag': 'CD'}, 'AM': {'pos': 'NOUN', 'tag': 'NN'},
                     '00:15': {'pos': 'NUM', 'tag': 'CD'}, '00:30': {'pos': 'NUM', 'tag': 'CD'},
                     '00:45': {'pos': 'NUM', 'tag': 'CD'}, '01:00': {'pos': 'NUM', 'tag': 'CD'},
                     '01:15': {'pos': 'NUM', 'tag': 'CD'}, '01:30': {'pos': 'NUM', 'tag': 'CD'},
                     '01:45': {'pos': 'NUM', 'tag': 'CD'}, '02:00': {'pos': 'NUM', 'tag': 'CD'},
                     '02:15': {'pos': 'NUM', 'tag': 'CD'}, '02:30': {'pos': 'NUM', 'tag': 'CD'},
                     '02:45': {'pos': 'NUM', 'tag': 'CD'}, '03:00': {'pos': 'NUM', 'tag': 'CD'},
                     '03:15': {'pos': 'NUM', 'tag': 'CD'}, '03:30': {'pos': 'NUM', 'tag': 'CD'},
                     '03:45': {'pos': 'NUM', 'tag': 'CD'}, '04:00': {'pos': 'NUM', 'tag': 'CD'},
                     '04:15': {'pos': 'NUM', 'tag': 'CD'}, '04:30': {'pos': 'NUM', 'tag': 'CD'},
                     '04:45': {'pos': 'NUM', 'tag': 'CD'}, '05:00': {'pos': 'NUM', 'tag': 'CD'},
                     '05:15': {'pos': 'NUM', 'tag': 'CD'}, '05:30': {'pos': 'NUM', 'tag': 'CD'},
                     '05:45': {'pos': 'NUM', 'tag': 'CD'}, '06:00': {'pos': 'NUM', 'tag': 'CD'},
                     '06:15': {'pos': 'NUM', 'tag': 'CD'}, '06:30': {'pos': 'NUM', 'tag': 'CD'},
                     '06:45': {'pos': 'NUM', 'tag': 'CD'}, '07:00': {'pos': 'NUM', 'tag': 'CD'},
                     '07:15': {'pos': 'NUM', 'tag': 'CD'}, '07:30': {'pos': 'NUM', 'tag': 'CD'},
                     '07:45': {'pos': 'NUM', 'tag': 'CD'}, '08:00': {'pos': 'NUM', 'tag': 'CD'},
                     '08:15': {'pos': 'NUM', 'tag': 'CD'}, '08:30': {'pos': 'NUM', 'tag': 'CD'},
                     '08:45': {'pos': 'NUM', 'tag': 'CD'}, '09:00': {'pos': 'NUM', 'tag': 'CD'},
                     '09:15': {'pos': 'NUM', 'tag': 'CD'}, '09:30': {'pos': 'NUM', 'tag': 'CD'},
                     '09:45': {'pos': 'NUM', 'tag': 'CD'}, '0:00': {'pos': 'NUM', 'tag': 'CD'},
                     '0:15': {'pos': 'NUM', 'tag': 'CD'}, '0:30': {'pos': 'NUM', 'tag': 'CD'},
                     '0:45': {'pos': 'NUM', 'tag': 'CD'}, '1:00': {'pos': 'NUM', 'tag': 'CD'},
                     '1:15': {'pos': 'NUM', 'tag': 'CD'}, '1:30': {'pos': 'NUM', 'tag': 'CD'},
                     '1:45': {'pos': 'NUM', 'tag': 'CD'}, '2:00': {'pos': 'NUM', 'tag': 'CD'},
                     '2:15': {'pos': 'NUM', 'tag': 'CD'}, '2:30': {'pos': 'NUM', 'tag': 'CD'},
                     '2:45': {'pos': 'NUM', 'tag': 'CD'}, '3:00': {'pos': 'NUM', 'tag': 'CD'},
                     '3:15': {'pos': 'NUM', 'tag': 'CD'}, '3:30': {'pos': 'NUM', 'tag': 'CD'},
                     '3:45': {'pos': 'NUM', 'tag': 'CD'}, '4:00': {'pos': 'NUM', 'tag': 'CD'},
                     '4:15': {'pos': 'NUM', 'tag': 'CD'}, '4:30': {'pos': 'NUM', 'tag': 'CD'},
                     '4:45': {'pos': 'NUM', 'tag': 'CD'}, '5:00': {'pos': 'NUM', 'tag': 'CD'},
                     '5:15': {'pos': 'NUM', 'tag': 'CD'}, '5:30': {'pos': 'NUM', 'tag': 'CD'},
                     '5:45': {'pos': 'NUM', 'tag': 'CD'}, '6:00': {'pos': 'NUM', 'tag': 'CD'},
                     '6:15': {'pos': 'NUM', 'tag': 'CD'}, '6:30': {'pos': 'NUM', 'tag': 'CD'},
                     '6:45': {'pos': 'NUM', 'tag': 'CD'}, '7:00': {'pos': 'NUM', 'tag': 'CD'},
                     '7:15': {'pos': 'NUM', 'tag': 'CD'}, '7:30': {'pos': 'NUM', 'tag': 'CD'},
                     '7:45': {'pos': 'NUM', 'tag': 'CD'}, '8:00': {'pos': 'NUM', 'tag': 'CD'},
                     '8:15': {'pos': 'NUM', 'tag': 'CD'}, '8:30': {'pos': 'NUM', 'tag': 'CD'},
                     '8:45': {'pos': 'NUM', 'tag': 'CD'}, '9:00': {'pos': 'NUM', 'tag': 'CD'},
                     '9:15': {'pos': 'NUM', 'tag': 'CD'}, '9:30': {'pos': 'NUM', 'tag': 'CD'},
                     '9:45': {'pos': 'NUM', 'tag': 'CD'}, '10:00': {'pos': 'NUM', 'tag': 'CD'},
                     '10:15': {'pos': 'NUM', 'tag': 'CD'}, '10:30': {'pos': 'NUM', 'tag': 'CD'},
                     '10:45': {'pos': 'NUM', 'tag': 'CD'}, '11:00': {'pos': 'NUM', 'tag': 'CD'},
                     '11:15': {'pos': 'NUM', 'tag': 'CD'}, '11:30': {'pos': 'NUM', 'tag': 'CD'},
                     '11:45': {'pos': 'NUM', 'tag': 'CD'}, '12:00': {'pos': 'NUM', 'tag': 'CD'},
                     'PM': {'pos': 'NOUN', 'tag': 'NN'}, '12:15': {'pos': 'NUM', 'tag': 'CD'},
                     '12:30': {'pos': 'NUM', 'tag': 'CD'}, '12:45': {'pos': 'NUM', 'tag': 'CD'},
                     'one': {'pos': 'NUM', 'tag': 'CD'}, 'two': {'pos': 'NUM', 'tag': 'CD'},
                     'three': {'pos': 'NUM', 'tag': 'CD'}, 'four': {'pos': 'NUM', 'tag': 'CD'},
                     'five': {'pos': 'NUM', 'tag': 'CD'}, 'six': {'pos': 'NUM', 'tag': 'CD'},
                     'seven': {'pos': 'NUM', 'tag': 'CD'}, 'eight': {'pos': 'NUM', 'tag': 'CD'},
                     'nine': {'pos': 'NUM', 'tag': 'CD'}, 'ten': {'pos': 'NUM', 'tag': 'CD'}}
        self.mode_names_list = []
        self.number_string_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                                   "ten"]
        self.five_w_dict = {"Who": "name", "What": "object", "Where": "location", "When": "time",
                            "How": "adjective adverb",
                            "Why": "reason"}
        self.prepositions_list = [
            "about", "above", "across", "after", "against", "along", "among", "around",
            "as", "at", "before", "behind", "below", "beneath", "beside", "between",
            "beyond", "by", "concerning", "considering", "despite", "down", "during",
            "except", "for", "from", "in", "inside", "into", "like", "near", "of",
            "off", "on", "out", "over", "past", "regarding", "round", "since", "through",
            "to", "toward", "under", "until", "up", "upon", "with", "within", "without"
        ]
        self.time_nlp_list = ["00:00 AM", "00:15 AM", "00:30 AM", "00:45 AM", "01:00 AM", "01:15 AM", "01:30 AM",
                              "01:45 AM", "02:00 AM", "02:15 AM", "02:30 AM", "02:45 AM", "03:00 AM", "03:15 AM",
                              "03:30 AM", "03:45 AM", "04:00 AM", "04:15 AM", "04:30 AM", "04:45 AM", "05:00 AM",
                              "05:15 AM", "05:30 AM", "05:45 AM", "06:00 AM", "06:15 AM", "06:30 AM", "06:45 AM",
                              "07:00 AM", "07:15 AM", "07:30 AM", "07:45 AM", "08:00 AM", "08:15 AM", "08:30 AM",
                              "08:45 AM", "09:00 AM", "09:15 AM", "09:30 AM", "09:45 AM", "0:00 AM", "0:15 AM",
                              "0:30 AM", "0:45 AM", "01:00 AM", "01:15 AM", "01:30 AM", "01:45 AM", "02:00 AM",
                              "02:15 AM", "02:30 AM", "02:45 AM", "03:00 AM", "03:15 AM", "03:30 AM", "03:45 AM",
                              "04:00 AM", "04:15 AM", "04:30 AM", "04:45 AM", "05:00 AM", "05:15 AM", "05:30 AM",
                              "05:45 AM", "06:00 AM", "06:15 AM", "06:30 AM", "06:45 AM", "07:00 AM", "07:15 AM",
                              "07:30 AM", "07:45 AM", "08:00 AM", "08:15 AM", "08:30 AM", "08:45 AM", "09:00 AM",
                              "09:15 AM", "09:30 AM", "09:45 AM", "10:00 AM", "10:15 AM", "10:30 AM", "10:45 AM",
                              "11:00 AM", "11:15 AM", "11:30 AM", "11:45 AM", "12:00 PM", "12:15 PM", "12:30 PM",
                              "12:45 PM", "01:00 PM", "01:15 PM", "01:30 PM", "01:45 PM", "02:00 PM", "02:15 PM",
                              "02:30 PM", "02:45 PM", "03:00 PM", "03:15 PM", "03:30 PM", "03:45 PM", "04:00 PM",
                              "04:15 PM", "04:30 PM", "04:45 PM", "05:00 PM", "05:15 PM", "05:30 PM", "05:45 PM",
                              "06:00 PM", "06:15 PM", "06:30 PM", "06:45 PM", "07:00 PM", "07:15 PM", "07:30 PM",
                              "07:45 PM", "08:00 PM", "08:15 PM", "08:30 PM", "08:45 PM", "09:00 PM", "09:15 PM",
                              "09:30 PM", "09:45 PM", "1:00 PM", "1:15 PM", "1:30 PM", "1:45 PM", "2:00 PM", "2:15 PM",
                              "2:30 PM", "2:45 PM", "3:00 PM", "3:15 PM", "3:30 PM", "3:45 PM", "4:00 PM", "4:15 PM",
                              "4:30 PM", "4:45 PM", "5:00 PM", "5:15 PM", "5:30 PM", "5:45 PM", "6:00 PM", "6:15 PM",
                              "6:30 PM", "6:45 PM", "7:00 PM", "7:15 PM", "7:30 PM", "7:45 PM", "8:00 PM", "8:15 PM",
                              "8:30 PM", "8:45 PM", "9:00 PM", "9:15 PM", "9:30 PM", "9:45 PM", "10:00 PM", "10:15 PM",
                              "10:30 PM", "10:45 PM", "11:00 PM", "11:15 PM", "11:30 PM", "11:45 PM", "12:00AM"]

        self.articles_list = ["a", "an", "the"]
        self.adjectives_list = [
            "short", "long", "strong", "bony", "broad", "chunky", "massive", "tall", "tiny", "fat",
            "skinny", "weak", "hot", "cold", "warm", "cool", "slow", "fast", "quick", "timid", "angry",
            "mad", "happy", "peaceful", "giant", "tiny", "kind", "cruel", "old", "young", "nice",
            "black", "blue", "brown", "green", "grey", "orange", "pink", "purple", "red", "white", "yellow"
        ]
        self.conjunctions_list = ["and", "as", "but", "for", "if", "nor", "or", "so", "yet"]
        self.days_of_week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.duration_list = ["hour", "minute", "second", "day", "week", "month", "year"]
        self.distance_list = ["inch", "foot", "yard", "mile", "millimeter", "meter", "kilometer"]
        self.verb_tag_list = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]

        self.sentence = str()
        self.sentence_list = []
        self.question = str()
        self.question_list = []
        self.remainder_list = []

    def question_method(self):
        if self.question_list[0] in self.five_w_dict.keys():
            q_word = self.question_list[0]
            # print("q_word is: ", q_word)
            # print("q_word.upper() is: ", q_word.upper())
            if q_word.upper() == "WHO":
                for w in self.remainder_list:
                    # print("w is ", w)
                    if w in self.mode_names_list:
                        return w
            if q_word.upper() == "WHOSE":
                for w in self.remainder_list:
                    # print("w is ", w)
                    idx_poss_list = [i for i, e in enumerate(self.remainder_list) if e == "'s"]
                    if len(idx_poss_list) > 0:
                        poss_idx = idx_poss_list[0]
                        if poss_idx > 0:
                            whose_idx = poss_idx - 1
                            return self.remainder_list[whose_idx]
                    elif w in self.mode_names_list:
                        return w
            elif q_word.upper() == "WHAT":
                remainder_list_1 = [s for s in self.remainder_list if s not in self.mode_names_list]
                remainder_list_2 = [s for s in remainder_list_1 if s not in self.articles_list]
                remainder_list_3 = [s for s in remainder_list_2 if s not in self.adjectives_list]
                remainder_list_4 = [s for s in remainder_list_3 if s not in self.conjunctions_list]
                remainder_list_5 = [s for s in remainder_list_4 if s not in self.prepositions_list]
                remainder_list_6 = [s for s in remainder_list_5 if s not in self.number_string_list]
                if len(remainder_list_6) > 1:
                    return remainder_list_6[-1]
                else:
                    return remainder_list_6.pop()
            elif q_word.upper() == "WHERE":
                remainder_list_1 = [s for s in self.remainder_list if s not in self.mode_names_list]
                remainder_list_2 = [s for s in remainder_list_1 if s not in self.articles_list]
                remainder_list_3 = [s for s in remainder_list_2 if s not in self.adjectives_list]
                remainder_list_4 = [s for s in remainder_list_3 if s not in self.conjunctions_list]
                remainder_list_5 = [s for s in remainder_list_4 if s not in self.number_string_list]
                location_list = []
                for i, w in enumerate(remainder_list_5):
                    if w in self.prepositions_list:
                        try:
                            if remainder_list_5[i + 1] in self.prepositions_list:
                                continue
                            else:
                                location_list.append(remainder_list_5[i + 1])
                        except Exception as e:
                            print(Exception, " error \n", e)
                            break
                for loc in location_list:
                    # if loc[0].isdigit():
                    #     continue
                    if len(loc) <= 3:
                        continue
                    else:
                        return loc
            elif q_word.upper() == "WHEN":
                remainder_list_1 = [s for s in self.remainder_list if s not in self.mode_names_list]
                remainder_list_2 = [s for s in remainder_list_1 if s not in self.articles_list]
                remainder_list_3 = [s for s in remainder_list_2 if s not in self.adjectives_list]
                remainder_list_4 = [s for s in remainder_list_3 if s not in self.conjunctions_list]
                location_list = []
                for i, w in enumerate(remainder_list_4):
                    if w in self.prepositions_list:
                        try:
                            location_list.append(remainder_list_4[i + 1])
                        except Exception as e:
                            break
                for loc in location_list:
                    if loc[0].isdigit():
                        return loc
                    elif loc in self.number_string_list:
                        return loc
            elif q_word.upper() == "HOW":
                if self.question_list[1] in self.mode_dict.keys():
                    w2 = self.question_list[1]
                    w2_pos_ = self.mode_dict[w2]['pos']
                    w2_tag_ = self.mode_dict[w2]['tag']
                    if w2_pos_ == "ADV" and w2_tag_ == "RB":
                        # for ans in remainder_list[1:]:
                        for ans in self.remainder_list:
                            if ans in self.distance_list:
                                return ans
                            elif ans in self.duration_list:
                                return ans
                        # elif w2_pos_ == "AUX" and w2_tag_ == "VBP":
                    elif w2_pos_ == "AUX" and w2_tag_ in ["VB", "VBD", "VBN", "VBP", "VBZ"]:
                        # print("look for verb")
                        # for rem in remainder_list[1:]:
                        for rem in self.remainder_list:
                            if rem in self.mode_dict.keys():
                                rem_pos_ = self.mode_dict[rem]['pos']
                                rem_tag_ = self.mode_dict[rem]['tag']
                                if rem_pos_ == "VERB" and rem_tag_ in ["VB", "VBD", "VBN", "VBP", "VBZ"]:
                                    return rem
                # print("remainder_list: ", remainder_list)
                remainder_list_1 = [s for s in self.remainder_list if s not in self.mode_names_list]
                # print("remainder_list_1: ", remainder_list_1)
                remainder_list_2 = [s for s in remainder_list_1 if s not in self.articles_list]
                # print("remainder_list_2: ", remainder_list_2)
                remainder_list_3 = [s for s in remainder_list_2 if s not in self.prepositions_list]
                # print("remainder_list_3: ", remainder_list_3)
                remainder_list_4 = [s for s in remainder_list_3 if s not in self.number_string_list]
                # print("remainder_list_4: ", remainder_list_4)
                hows_list = []
                for i, w in enumerate(remainder_list_4):
                    if w in self.adjectives_list:
                        try:
                            hows_list.append(remainder_list_4[i])
                        except Exception as e:
                            print(Exception, " is ", e)
                            break
                if len(hows_list) > 1:
                    return hows_list[0]
                elif len(hows_list) == 1:
                    return hows_list.pop()
            elif q_word.upper() == "WHY":
                remainder_list_1 = [s for s in self.remainder_list if s not in self.mode_names_list]
                remainder_list_2 = [s for s in remainder_list_1 if s not in self.articles_list]
                remainder_list_3 = [s for s in remainder_list_2 if s not in self.prepositions_list]
                remainder_list_4 = [s for s in remainder_list_3 if s not in self.number_string_list]
                # longest_word = [r for r in remainder_list_4 if r is max(remainder_list_4, key=len)]
                longest_word = max(remainder_list_4, key=len)
                print("longest_word: ", longest_word)
                return longest_word
        return None

    def solve(self, sentence, question):

        '''
          You can use a library like spacy (https://spacy.io/usage/linguistic-features) to preprocess the
            mostcommon.txt file. There are others that could be used but you must use them in preprocessing only.
            You CANNOT import the library into Gradescope.
          
          You must include whatever preprocessing you've done into your SentenceReadingAgent.py.
          
          DO NOT use another file .txt or .csv. Hard code your DICTS | LISTS into this .py file
          
          While the supplied mostcommon.txt contains most of the common words you will need
            you can (and SHOULD) expand the file as you find cases that the agent has problems
            processing. 
            
          Also not all words will be processed using the correct lexing for every possible problem the 
            agent might encounter and you are ENCOURAGED to expand these in your agents knowledge representation.
        '''

        # read in the file
        mode_words_file = open("mostcommon.txt", "r")
        mode_words_data = mode_words_file.read()
        mode_words_list = mode_words_data.split("\n")
        mode_words_file.close()

        # spacy?
        # nlp = spacy.load("en_core_web_sm")
        # txt_spacy = nlp(mode_words_data)
        # print(type(txt_spacy))
        # print(token.text for token in txt_spacy)
        # mode_nlp = nlp(pathlib.Path("mostcommon.txt").read_text(encoding="utf-8"))
        # print([token.text for token in mode_nlp])
        #
        # sentence_nlp = nlp(sentence)
        # question_nlp = nlp(question)
        # sentence_nlp_list = list(sentence_nlp)
        # question_nlp_list = list(question_nlp)

        ## gunna want the lemma list
        ## 8 parts of speech

        # lemma_dict = {}
        # adjective_nlp_list = []
        # adposition_nlp_list = []
        # adverb_nlp_list = []
        # auxiliary_nlp_list = []
        # conjunction_nlp_list = []
        # coordinating_conjunction_nlp_list = []
        # determiner_nlp_list = []
        # email_nlp_list = []
        # existential_there_nlp_list = []
        # foreign_word_nlp_list = []
        # infinitival_nlp_list = []
        # interjection_nlp_list = []
        # noun_nlp_list = []
        # num_nlp_list = []
        # particle_nlp_list = []
        # pronoun_nlp_list = []
        # proper_noun_nlp_list = []
        # punctuation_nlp_list = []
        # subordinating_conjunction_nlp_list = []
        # symbol_nlp_list = []
        # verb_nlp_list = []
        # aux_be_nlp_list = []
        # haves_nlp_list = []
        #
        # cardinal_number_nlp_list = []
        lemma_words_list = []
        # mode_nlp = mode_nlp.
        # for token in mode_nlp:
        #     token_pos = token.pos_
        #     if token_pos != "SPACE":
        #         #if token != '\n':
        #         #print("token? ", token)
        #         token_pos = token.pos_
        #         token_tag = token.tag_
        #         token_lemma = token.lemma_
        #         lemma_pos = [t for t in nlp(token_lemma)][0].pos_
        #         lemma_tag = [t for t in nlp(token_lemma)][0].tag_
        #         lemma_lemma = [t for t in nlp(token_lemma)][0].lemma_
        #         if token not in mode_dict.keys():
        #             token_dict = {"pos": token_pos, "tag": token_tag}#, "lemma": token_lemma}
        #             #
        #             mode_dict[str(token)] = token_dict
        #         # if token_lemma not in mode_dict.keys():
        #         #     #lemma_dict["lemma"]: lemma_lemma, "pos": lemma_pos, "tag": lemma_tag}
        #         #     lemma_dict = {"pos": lemma_pos, "tag": lemma_tag}# , "lemma": token_lemma
        #         #     mode_dict[token] = lemma_dict
        #     # else:
        #     #     print("token? ", token)
        # # for ent in mode_nlp.ents:
        # #     if ent.label_ == "TIME":
        # #         time_nlp_list.append(ent)
        # print("doc dict: \n", mode_dict)
        # # print("doc time_nlp_list: ", time_nlp_list)
        # # both O(n)
        self.mode_names_list = [word for word in mode_words_list if any(char.isupper() for char in word)]
        print("names list\n", self.mode_names_list)

        self.sentence = sentence.replace(",", " ")
        self.sentence = sentence.replace("?", " ")
        self.sentence = sentence.replace("!", " ")
        self.sentence = sentence.replace(".", " ")
        self.sentence = sentence.replace(";", " ")
        # sentence = sentence.replace("'s", " ")

        self.sentence_list = sentence.split()
        # new_sentence_list = []
        # for w in sentence_list:
        #     # if "'s" in sentence_list:
        #     # idx_poss_list = [i for i, e in enumerate(sentence_list) if e == "'s"]
        #     # for idx in idx_poss_list:
        #     if w == "'s":
        #

        # question = question.replace(",", " ")
        self.question = question.replace("?", " ")
        self.question = question.replace("!", " ")
        self.question = question.replace(".", " ")
        self.question = question.replace(";", " ")
        # question = question.replace("'s", " ")
        self.question_list = question.split()
        # remainder_list = [s for s in sentence_list if s not in question_list]
        self.remainder_list = []
        for s in self.sentence_list:
            if s not in self.question_list:
                self.remainder_list.append(s)
            elif s in self.mode_dict.keys():
                s_pos_ = self.mode_dict[s]['pos']
                s_tag_ = self.mode_dict[s]['tag']
                if s_tag_ in self.verb_tag_list:
                    self.remainder_list.append(s)
        ############

            #######
        ########
        if question_list[0] in self.prepositions_list:
            prep_word = question_list[0]
        ########
        remainder_list_1 = [s for s in self.remainder_list if s not in self.articles_list]
        remainder_list_2 = [s for s in remainder_list_1 if s not in self.adjectives_list]
        remainder_list_3 = [s for s in remainder_list_2 if s not in self.conjunctions_list]
        remainder_list_4 = [s for s in remainder_list_3 if s not in self.prepositions_list]
        rand_ans = remainder_list_4[-1]
        print("random answer: ", rand_ans)
        return rand_ans
