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
                          'the': {'pos': 'DET', 'tag': 'DT'}, 'of': {'pos': 'ADP', 'tag': 'IN'},
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
                          'up': {'pos': 'ADP', 'tag': 'IN'}, 'use': {'pos': 'VERB', 'tag': 'VB'},
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
                          'go': {'pos': 'AUX', 'tag': 'VB'}, 'come': {'pos': 'VERB', 'tag': 'VB'},
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
                          'one': {'pos': 'NUM', 'tag': 'CD'}, 'two': {'pos': 'NUM', 'tag': 'CD'},
                          'three': {'pos': 'NUM', 'tag': 'CD'}, 'four': {'pos': 'NUM', 'tag': 'CD'},
                          'five': {'pos': 'NUM', 'tag': 'CD'}, 'six': {'pos': 'NUM', 'tag': 'CD'},
                          'seven': {'pos': 'NUM', 'tag': 'CD'}, 'eight': {'pos': 'NUM', 'tag': 'CD'},
                          'nine': {'pos': 'NUM', 'tag': 'CD'}, 'ten': {'pos': 'NUM', 'tag': 'CD'},
                          'because': {'pos': 'SCONJ', 'tag': 'IN'}, 'enjoy': {'pos': 'VERB', 'tag': 'VBP'}}
        self.nlp_verbs = [k for k, nested_dict in self.mode_dict.items() if nested_dict.get("pos") == "VERB"]
        # print("self.nlp_verbs ", self.nlp_verbs)
        self.nlp_nouns = [k for k, nested_dict in self.mode_dict.items() if nested_dict.get("pos") == "NOUN"]
        # print("self.nlp_nouns ", self.nlp_nouns)
        self.nlp_pronouns = [k for k, nested_dict in self.mode_dict.items() if nested_dict.get("pos") == "PRON"
                             and nested_dict.get("tag") != "EX" and nested_dict.get("tag") != "WDT"
                             and nested_dict.get("tag") != "WP"]
        # print("self.nlp_pronouns ", self.nlp_pronouns)
        self.nlp_proper_noun = [k for k, nested_dict in self.mode_dict.items() if nested_dict.get("pos") == "PROPN"]
        # print("self.nlp_proper_noun ", self.nlp_proper_noun)
        self.nlp_gerund = [k for k, nested_dict in self.mode_dict.items() if nested_dict.get("pos") == "VBZ"]
        # print("self.nlp_gerund ", self.nlp_gerund)

        # self.nlp_nouns = [v for v in self.mode_dict['pos'].values() if v == "NOUN"]
        # self.nlp_pronouns = [v for v in self.mode_dict['pos'].values() if v == "PRON"]
        # self.nlp_proper_noun = [v for v in self.mode_dict['pos'].values() if v == "PROPN"]
        # self.nlp_gerund = [v for v in self.mode_dict['tag'].values() if v == "VBZ"]

        self.mode_names_list = []
        self.number_string_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                                   "ten"]
        self.five_w_dict = {"Who": "name", "What": "object", "Where": "location", "When": "time",
                            "How": "adjective adverb", "Why": "reason", "Which": "object"}
        self.prepositions_list = [
            "about", "above", "across", "after", "against", "along", "among", "around",
            "as", "at", "before", "behind", "below", "beneath", "beside", "between",
            "beyond", "by", "concerning", "considering", "despite", "down", "during",
            "except", "for", "from", "in", "inside", "into", "like", "near", "of",
            "off", "on", "out", "over", "past", "regarding", "round", "since", "through",
            "to", "toward", "under", "until", "up", "upon", "with", "within", "without"
        ]
        self.time_nlp_list = ["00:00 am", "00:15 am", "00:30 am", "00:45 am", "01:00 am", "01:15 am", "01:30 am",
                              "01:45 am", "02:00 am", "02:15 am", "02:30 am", "02:45 am", "03:00 am", "03:15 am",
                              "03:30 am", "03:45 am", "04:00 am", "04:15 am", "04:30 am", "04:45 am", "05:00 am",
                              "05:15 am", "05:30 am", "05:45 am", "06:00 am", "06:15 am", "06:30 am", "06:45 am",
                              "07:00 am", "07:15 am", "07:30 am", "07:45 am", "08:00 am", "08:15 am", "08:30 am",
                              "08:45 am", "09:00 am", "09:15 am", "09:30 am", "09:45 am", "0:00 am", "0:15 am",
                              "0:00 am", "0:30 am", "0:45 am", "01:00 am", "01:15 am", "01:30 am", "01:45 am",
                              "2:00 am", "2:15 am", "2:30 am", "2:45 am", "3:00 am", "3:15 am", "3:30 am", "3:45 am",
                              "4:00 am", "4:15 am", "4:30 am", "4:45 am", "5:00 am", "5:15 am", "5:30 am", "5:45 am",
                              "6:00 am", "6:15 am", "6:30 am", "6:45 am", "7:00 am", "7:15 am", "7:30 am", "7:45 am",
                              "8:00 am", "8:15 am", "8:30 am", "8:45 am", "9:00 am", "9:15 am", "9:30 am", "9:45 am",
                              "10:00 am", "10:15 am", "10:30 am", "10:45 am", "11:00 am", "11:15 am", "11:30 am",
                              "11:45 am", "12:00 pm", "12:15 pm", "12:30 pm", "12:45 pm", "01:00 pm", "01:15 pm",
                              "01:30 pm", "01:45 pm", "02:00 pm", "02:15 pm", "02:30 pm", "02:45 pm", "03:00 pm",
                              "03:15 pm", "03:30 pm", "03:45 pm", "04:00 pm", "04:15 pm", "04:30 pm", "04:45 pm",
                              "05:00 pm", "05:15 pm", "05:30 pm", "05:45 pm", "06:00 pm", "06:15 pm", "06:30 pm",
                              "06:45 pm", "07:00 pm", "07:15 pm", "07:30 pm", "07:45 pm", "08:00 pm", "08:15 pm",
                              "08:30 pm", "08:45 pm", "09:00 pm", "09:15 pm", "09:30 pm", "09:45 pm", "1:00 pm",
                              "1:15 pm", "1:30 pm", "1:45 pm", "2:00 pm", "2:15 pm", "2:30 pm", "2:45 pm", "3:00 pm",
                              "3:15 pm", "3:30 pm", "3:45 pm", "4:00 pm", "4:15 pm", "4:30 pm", "4:45 pm", "5:00 pm",
                              "5:15 pm", "5:30 pm", "5:45 pm", "6:00 pm", "6:15 pm", "6:30 pm", "6:45 pm", "7:00 pm",
                              "7:15 pm", "7:30 pm", "7:45 pm", "8:00 pm", "8:15 pm", "8:30 pm", "8:45 pm", "9:00 pm",
                              "9:15 pm", "9:30 pm", "9:45 pm", "10:00 pm", "10:15 pm", "10:30 pm", "10:45 pm",
                              "11:00 pm", "11:15 pm", "11:30 pm", "11:45 pm", "12:00 am",
                              "00:00am", "00:15 am", "00:30am", "00:45 am", "01:00am", "01:15 am", "01:30am",
                              "01:45 am", "02:00am", "02:15 am", "02:30am", "02:45 am", "03:00am", "03:15 am",
                              "03:30am", "03:45 am", "04:00am", "04:15 am", "04:30am", "04:45 am", "05:00am",
                              "05:15 am", "05:30am", "05:45 am", "06:00am", "06:15 am", "06:30am", "06:45 am",
                              "07:00am", "07:15 am", "07:30am", "07:45 am", "08:00am", "08:15 am", "08:30am",
                              "08:45 am", "09:00am", "09:15 am", "09:30am", "09:45 am", "0:00am", "0:15 am",
                              "0:00am", "0:30am", "0:45 am", "01:00am", "01:15 am", "01:30am", "01:45 am",
                              "2:00am", "2:15 am", "2:30am", "2:45 am", "3:00am", "3:15 am", "3:30am", "3:45 am",
                              "4:00am", "4:15 am", "4:30am", "4:45 am", "5:00am", "5:15 am", "5:30am", "5:45 am",
                              "6:00am", "6:15 am", "6:30am", "6:45 am", "7:00am", "7:15 am", "7:30am", "7:45 am",
                              "8:00am", "8:15 am", "8:30am", "8:45 am", "9:00am", "9:15 am", "9:30am", "9:45 am",
                              "10:00am", "10:15 am", "10:30am", "10:45 am", "11:00am", "11:15 am", "11:30am",
                              "11:45 am", "12:00pm", "12:15 pm", "12:30pm", "12:45 pm", "01:00pm", "01:15 pm",
                              "01:30pm", "01:45 pm", "02:00pm", "02:15 pm", "02:30pm", "02:45 pm", "03:00pm",
                              "03:15 pm", "03:30pm", "03:45 pm", "04:00pm", "04:15 pm", "04:30pm", "04:45 pm",
                              "05:00pm", "05:15 pm", "05:30pm", "05:45 pm", "06:00pm", "06:15 pm", "06:30pm",
                              "06:45 pm", "07:00pm", "07:15 pm", "07:30pm", "07:45 pm", "08:00pm", "08:15 pm",
                              "08:30pm", "08:45 pm", "09:00pm", "09:15 pm", "09:30pm", "09:45 pm", "1:00pm",
                              "1:15 pm", "1:30pm", "1:45 pm", "2:00pm", "2:15 pm", "2:30pm", "2:45 pm", "3:00pm",
                              "3:15 pm", "3:30pm", "3:45 pm", "4:00pm", "4:15 pm", "4:30pm", "4:45 pm", "5:00pm",
                              "5:15 pm", "5:30pm", "5:45 pm", "6:00pm", "6:15 pm", "6:30pm", "6:45 pm", "7:00pm",
                              "7:15 pm", "7:30pm", "7:45 pm", "8:00pm", "8:15 pm", "8:30pm", "8:45 pm", "9:00pm",
                              "9:15 pm", "9:30pm", "9:45 pm", "10:00pm", "10:15 pm", "10:30pm", "10:45 pm",
                              "11:00pm", "11:15 pm", "11:30pm", "11:45 pm", "12:00am"
                              ]

        # self.articles_list = ["a", "A", "an", "An", "the", "The"]
        self.articles_list = ["a", "an", "the"]
        self.adjectives_list = [
            "short", "long", "strong", "bony", "broad", "chunky", "massive", "tall", "tiny", "fat",
            "skinny", "weak", "hot", "cold", "warm", "cool", "slow", "fast", "quick", "timid", "angry",
            "mad", "happy", "peaceful", "giant", "tiny", "kind", "cruel", "old", "young", "nice",
            "black", "blue", "brown", "green", "grey", "orange", "pink", "purple", "red", "white", "yellow"
        ]
        self.conjunctions_list = ["and", "as", "but", "for", "if", "nor", "or", "so", "yet"]
        self.days_of_week_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        self.duration_list = ["hour", "minute", "second", "day", "week", "month", "year"]
        self.distance_list = ["inch", "foot", "yard", "mile", "millimeter", "meter", "kilometer"]
        self.verb_tag_list = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]

        self.first_personal_pronouns = ["I", "ME", "WE", "US"]
        self.second_personal_pronouns = ["you", "your"]
        self.thid_personal_pronouns = ["he", "she", "they", "it", "him", "her", "them", "they"]

        self.sentence = str()
        self.sentence_list = []
        self.question = str()
        self.question_list = []
        self.remainder_list = []

        self.sentence_thematic_roles = {}
        self.question_thematic_roles = {}

    def question_method(self, q_word, question_list):
        idx_q_list = [i for i, e in enumerate(question_list) if e == q_word]
        if idx_q_list:
            q_idx = idx_q_list[0]
        else:
            q_idx = 0
        # if self.question_list[0] in self.five_w_dict.keys():
        # q_word = question_list[0]
        # print("q_word is: ", q_word)
        # print("q_word.upper() is: ", q_word.upper())
        if q_word.upper() == "WHO":
            # print("self.remainder_list is: ", self.remainder_list)
            if (("verb" in self.question_thematic_roles and "verb" in self.question_thematic_roles) and
                    (self.question_thematic_roles["verb"] == self.sentence_thematic_roles["verb"])):
                if "agent" in self.sentence_thematic_roles:
                    return self.sentence_thematic_roles["agent"]
            elif "beneficiary" in self.sentence_thematic_roles:
                return self.sentence_thematic_roles["beneficiary"]
            else:
                noun_list = []
                prep_check = False
                for w in self.remainder_list:
                    # print("w is ", w)
                    if w in self.mode_names_list:
                        return w
                    elif w in self.nlp_nouns and prep_check is False:
                        noun_list.append(w)
                    elif w in self.nlp_nouns and prep_check:
                        prep_check = False
                    elif w in self.prepositions_list:
                        prep_check = True
                if noun_list:
                    return noun_list[0]
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
            #if question_list[1].lower() in (k.lower() for k in self.mode_dict.keys()):
            # print("what is q_idx", question_list[q_idx])
            # print("what is question_list: ", question_list)
            # print("question_list[q_idx+1]: ", question_list[q_idx+1])
            try:
                if question_list[q_idx+1].upper() == "TIME":
                    # print("self.remainder_list: ", self.remainder_list)
                    for w in self.remainder_list:
                        # print("w is ", w)
                        if w.lower() in self.time_nlp_list:
                            return w
                # else:
                #     print("question_list[q_idx+1].upper(): ", question_list[q_idx+1].upper())
                #     print(question_list[q_idx+1].upper() == "TIME")
                elif question_list[q_idx + 1].lower() in self.mode_dict.keys():
                    #elif question_list[q_idx+1].lower() in (k.lower() for k in self.mode_dict.keys()):
                    # w2 = question_list[1]
                    w2 = question_list[q_idx+1]
                    w2_pos_ = self.mode_dict[w2]['pos']
                    w2_tag_ = self.mode_dict[w2]['tag']
                    if w2_pos_ == "AUX" and w2_tag_ in ["VB", "VBD", "VBN", "VBP", "VBZ"]:
                        # main_vb = []
                        #if w2_tag_ == "VBD" or w2_tag_ == "":
                        if w2_tag_ in ["VBD", "VBN", "VBP", "VBZ"]:
                            # print("question_list[q_idx+1:]: ", question_list[q_idx+1:])
                            for qs in question_list[q_idx+2:]:
                                #if qs.lower() in (k.lower() for k in self.mode_dict.keys()):
                                if qs.lower() in self.mode_dict.keys():
                                    qs_pos_ = self.mode_dict[qs]['pos']
                                    if qs_pos_ == "VERB":
                                        for rem in self.remainder_list:
                                            #if rem.lower() in (k.lower() for k in self.mode_dict.keys()):
                                            if rem.lower() in self.mode_dict.keys():
                                                rem_pos_ = self.mode_dict[rem]['pos']
                                                if rem_pos_ == "NOUN":
                                                    return rem
                                    elif qs_pos_ == "NOUN":
                                        if "agent" in self.sentence_thematic_roles:
                                            return self.sentence_thematic_roles["agent"]
                                        elif "verb" in self.sentence_thematic_roles and "verb" in self.question_thematic_roles:
                                            if self.sentence_thematic_roles["verb"] == self.question_thematic_roles["verb"]:
                                                vb = self.sentence_thematic_roles["verb"]
                                                nouns_before_verb = []
                                                for rem in self.remainder_list:
                                                    if rem in self.nlp_nouns:
                                                        nouns_before_verb.append(rem)
                                                    elif rem == vb:
                                                        break
                                                if nouns_before_verb:
                                                    return nouns_before_verb[-1]
                                        else:
                                            nouns_before_verb = []
                                            for rem in self.remainder_list:
                                                if rem in self.nlp_nouns:
                                                    nouns_before_verb.append(rem)
                                                elif rem in self.nlp_verbs:
                                                    break
                                            if nouns_before_verb:
                                                return nouns_before_verb[-1]

                        else:
                            # print("look for verb")
                            # for rem in remainder_list[1:]:
                            for rem in self.remainder_list:
                                #if rem.lower() in (k.lower() for k in self.mode_dict.keys()):
                                if rem.lower() in self.mode_dict.keys():
                                    rem_pos_ = self.mode_dict[rem]['pos']
                                    rem_tag_ = self.mode_dict[rem]['tag']
                                    if rem_pos_ == "VERB" and rem_tag_ in ["VB", "VBD", "VBN", "VBP", "VBZ"]:
                                        return rem
                    elif w2_pos_ == "ADV" and w2_tag_ == "RB":
                        for ans in self.remainder_list:
                            #if ans.lower() in (d.lower() for d in self.distance_list):
                            if ans.lower() in self.distance_list:
                                return ans
                            elif ans.lower() in self.duration_list:
                                #elif ans.lower() in (d.lower() for d in self.duration_list):
                                return ans
            except Exception as e:
                print(Exception, "e is ", e)
            ####
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
            # prep_count = 0
            try:
                for i, w in enumerate(remainder_list_5):
                    #if w.lower() in (p.lower() for p in self.prepositions_list):
                    if w.lower() in self.prepositions_list:
                        prep_idx = i
                        for n in remainder_list_5[i+1:]:
                            #if n.lower() in (k.lower() for k in self.mode_dict.keys()):
                            if n.lower() in self.mode_dict.keys():
                                n_pos_ = self.mode_dict[n]['pos']
                                if n_pos_ == "NOUN":
                                    location_list.append(n)
                                elif n.lower() in self.prepositions_list:
                                    #elif n.lower() in (p.lower() for p in self.prepositions_list):
                                    break
                                elif n_pos_ == "DET":
                                    break
                        # prep_count += 1
                        # try:
                        #     # if remainder_list_5[i + 1].lower() in (p.lower() for p in self.prepositions_list):
                        #     #     continue
                        #     # else:
                        #     #     location_list.append(remainder_list_5[i + 1])
                        #     if remainder_list_5[i + 1].lower() in (k.lower() for k in self.mode_dict.keys()):
                        # except Exception as e:
                        #     print(Exception, " error \n", e)
                        #     break
                for loc in location_list:
                    # if loc[0].isdigit():
                    #     continue
                    if len(loc) <= 2:
                        continue
                    elif len(loc) > 2:
                        return loc
                    else:
                        return remainder_list_5[-1]
            except Exception as e:
                print(Exception, "e is ", e)
                return remainder_list_5[-1]
        elif q_word.upper() == "WHEN":
            remainder_list_1 = [s for s in self.remainder_list if s not in self.mode_names_list]
            remainder_list_2 = [s for s in remainder_list_1 if s not in self.articles_list]
            remainder_list_3 = [s for s in remainder_list_2 if s not in self.adjectives_list]
            remainder_list_4 = [s for s in remainder_list_3 if s not in self.conjunctions_list]
            time_list = []
            try:
                for i, w in enumerate(remainder_list_4):
                    #if w.lower() in (p.lower() for p in self.prepositions_list):
                    if w.lower() in self.prepositions_list:
                        for n in remainder_list_4[i+1:]:
                            #if n.lower() in (k.lower() for k in self.mode_dict.keys()):
                            if n.lower() in self.mode_dict.keys():
                                n_pos_ = self.mode_dict[n]['pos']
                                if n_pos_ == "NOUN" or n_pos_ == "NUM":
                                    time_list.append(n)
                                elif n.lower() in self.prepositions_list:
                                    #elif n.lower() in (p.lower() for p in self.prepositions_list):
                                    break
                                elif n_pos_ == "DET":
                                    break
                        # try:
                        #     location_list.append(remainder_list_4[i + 1])
                        # except Exception as e:
                        #     break
                for t in time_list:
                    #if t.lower() in (n.lower() for n in self.number_string_list) or self.mode_dict[t]['tag'] == "CD":
                    if t.lower() in self.number_string_list or self.mode_dict[t]['tag'] == "CD":
                        return t
                    elif t[0].isdigit():
                        return t
            except Exception as e:
                print(Exception, "e is ", e)
                return remainder_list_4[-1]
        elif q_word.upper() == "HOW":
            try:
                # if question_list[1].lower() in (k.lower() for k in self.mode_dict.keys()):
                if question_list[q_idx + 1].lower() in self.mode_dict.keys():
                    # w2 = question_list[1]
                    w2 = question_list[q_idx + 1]
                    w2_pos_ = self.mode_dict[w2]['pos']
                    w2_tag_ = self.mode_dict[w2]['tag']
                    if w2_pos_ == "ADV" and w2_tag_ == "RB":
                        # for ans in remainder_list[1:]:
                        for ans in self.remainder_list:
                            #if ans.lower() in (d.lower() for d in self.distance_list):
                            if ans.lower() in self.distance_list:
                                return ans
                            elif ans.lower() in self.duration_list:
                                #elif ans.lower() in (d.lower() for d in self.duration_list):
                                return ans
                        # elif w2_pos_ == "AUX" and w2_tag_ == "VBP":
                    elif w2_pos_ == "AUX" and w2_tag_ in ["VB", "VBD", "VBN", "VBP", "VBZ"]:
                        # print("look for verb")
                        # for rem in remainder_list[1:]:
                        for rem in self.remainder_list:
                            #if rem.lower() in (k.lower() for k in self.mode_dict.keys()):
                            if rem.lower() in self.mode_dict.keys():
                                rem_pos_ = self.mode_dict[rem]['pos']
                                rem_tag_ = self.mode_dict[rem]['tag']
                                if rem_pos_ == "VERB" and rem_tag_ in ["VB", "VBD", "VBN", "VBP", "VBZ"]:
                                    return rem
                    elif w2_pos_ == "ADJ":
                        adj_list = []
                        noun_list = []
                        for rem in self.remainder_list:
                            #if rem.lower() in (k.lower() for k in self.mode_dict.keys()):
                            if rem.lower() in self.mode_dict.keys():
                                rem_pos_ = self.mode_dict[rem]['pos']
                                if rem_pos_ == "ADJ":
                                    return rem
            except Exception as e:
                print(Exception, "e is ", e)
            #else:
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
                #if w.lower() in (a.lower() for a in self.adjectives_list):
                if w.lower() in self.adjectives_list:
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
            # print("longest_word: ", longest_word)
            return longest_word
        elif q_word.upper() == "WHICH":
            first_third_pro = False
            second_pro = False
            for p in question_list:
                if p.lower() in self.thid_personal_pronouns or p.upper() in self.first_personal_pronouns:
                    first_third_pro = True
                elif p.lower() in self.second_personal_pronouns:
                    second_pro = True
            if first_third_pro:
                if "object" in self.sentence_thematic_roles:
                    return self.sentence_thematic_roles["object"]
                elif "thematicObj" in self.sentence_thematic_roles:
                    return self.sentence_thematic_roles["thematicObj"]
            elif second_pro:
                if "verb" in self.sentence_thematic_roles:
                    vb = self.sentence_thematic_roles["verb"]
                    if vb.lower() in self.mode_dict.keys():
                        vb_pos_ = self.mode_dict[vb]['pos']
                        vb_tag_ = self.mode_dict[vb]['tag']
                        if vb_tag_ == "VBP":
                            if "object" in self.sentence_thematic_roles:
                                return self.sentence_thematic_roles["object"]
                            elif "thematicObj" in self.sentence_thematic_roles:
                                return self.sentence_thematic_roles["thematicObj"]
                        elif vb_tag_ == "VBN":
                            verb_pass = False
                            for p in self.remainder_list:
                                if p.lower() in self.nlp_nouns and verb_pass is False:
                                    return p
                                elif p.lower() in self.nlp_verbs:
                                    verb_pass = True
                                else:
                                    continue
            else:
                remainder_list_1 = [s for s in self.remainder_list if s not in self.mode_names_list]
                remainder_list_2 = [s for s in remainder_list_1 if s not in self.articles_list]
                remainder_list_3 = [s for s in remainder_list_2 if s not in self.adjectives_list]
                remainder_list_4 = [s for s in remainder_list_3 if s not in self.prepositions_list]
                remainder_list_5 = [s for s in remainder_list_4 if s not in self.conjunctions_list]
                verb_pass = False
                for p in remainder_list_5:
                    if p.lower() in self.nlp_nouns and verb_pass is False:
                        return p
                    elif p.lower() in self.nlp_verbs:
                        verb_pass = True
        else:
            return None

    def solve(self, sentence, question):
        self.mode_names_list = []
        self.sentence = str()
        self.sentence_list = []
        self.question = str()
        self.question_list = []
        self.remainder_list = []
        self.sentence_thematic_roles = {}
        self.question_thematic_roles = {}
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
        # print("names list\n", self.mode_names_list)

        self.sentence = sentence.replace(",", " ")
        self.sentence = self.sentence.replace("?", " ")
        self.sentence = self.sentence.replace("!", " ")
        self.sentence = self.sentence.replace(".", " ")
        self.sentence = self.sentence.replace(";", " ")
        # sentence = sentence.replace("'s", " ")

        self.sentence_list = self.sentence.split()
        # print("self.sentence_list: ", self.sentence_list)
        # new_sentence_list = []
        # for w in sentence_list:
        #     # if "'s" in sentence_list:
        #     # idx_poss_list = [i for i, e in enumerate(sentence_list) if e == "'s"]
        #     # for idx in idx_poss_list:
        #     if w == "'s":
        #

        # question = question.replace(",", " ")
        self.question = question.replace("?", " ")
        self.question = self.question.replace("!", " ")
        self.question = self.question.replace(".", " ")
        self.question = self.question.replace(";", " ")
        # question = question.replace("'s", " ")
        self.question_list = self.question.split()
        # print("self.question_list: ", self.question_list)
        # print("self.question_list[0]: ", self.question_list[0])
        # remainder_list = [s for s in sentence_list if s not in question_list]
        self.remainder_list = []
        #self.nlp_verbs = [v for v in self.mode_dict['tag'].values() if v == "VERB"]
        #self.nlp_nouns = [v for v in self.mode_dict['tag'].values() if v == "NOUN"]
        #self.nlp_pronouns = [v for v in self.mode_dict['tag'].values() if v == "PRON"]
        #self.nlp_proper_noun
        #self.sentence_thematic_roles = {"verb", "agent", "coagent", "beneficiary", "thematicObj", "instrument", "destination", "conveyance"}
        #self.question_thematic_roles = {}
        sent_count = 0
        prep_phrase = False
        prep = str()
        det_flag = False
        for s in self.sentence_list:
            if s.lower() in self.nlp_verbs:
                self.sentence_thematic_roles["verb"] = s
            elif (s in self.nlp_proper_noun or s.lower() in self.nlp_pronouns) and sent_count == 0:
                self.sentence_thematic_roles["agent"] = s
            elif ((s in self.nlp_proper_noun or s.lower() in self.nlp_pronouns) and sent_count > 0 and
                  "agent" not in self.sentence_thematic_roles.keys()):
                self.question_thematic_roles["agent"] = s
            elif ((s in self.nlp_proper_noun or s.lower() in self.nlp_pronouns) and sent_count > 0 and
                  "verb" not in self.sentence_thematic_roles.keys()):
                self.sentence_thematic_roles["coagent"] = s
            elif ((s in self.nlp_proper_noun or s.lower() in self.nlp_pronouns) and sent_count > 0 and
                  "verb" in self.sentence_thematic_roles.keys()):
                self.sentence_thematic_roles["beneficiary"] = s
            elif ((s.lower() in self.nlp_nouns or det_flag) and sent_count > 0 and
                  "verb" in self.sentence_thematic_roles.keys() and prep_phrase is False):
                self.sentence_thematic_roles["object"] = s
            elif (s.lower() in self.nlp_nouns or det_flag) and sent_count > 0 and prep_phrase:
                if prep == "with":
                    self.sentence_thematic_roles["instrument"] = s
                elif prep == "by":
                    self.sentence_thematic_roles["conveyance"] = s
                elif prep == "to":
                    self.sentence_thematic_roles["thematicObj"] = s
            elif s.lower() in self.prepositions_list:
                prep_phrase = True
                prep = s.lower()
            elif s.lower in self.articles_list:
                det_flag = True
            try: 
                if s.lower() not in (q.lower() for q in self.question_list):
                    self.remainder_list.append(s)
                elif s.lower() in (k.lower() for k in self.mode_dict.keys()):
                    s_pos_ = self.mode_dict[s]['pos']
                    s_tag_ = self.mode_dict[s]['tag']
                    if s_tag_.lower() in (v.lower() for v in self.verb_tag_list):
                        self.remainder_list.append(s)
                    elif s_tag_ == "ADJ":
                        self.remainder_list.append(s)
            except Exception as e:
                print(Exception, " is ", e)
            sent_count += 1
        ############
        quest_count = 0
        prep_phrase = False
        prep = str()
        det_flag = False
        for s in self.question_list:
            if s.lower() in self.nlp_verbs:
                self.question_thematic_roles["verb"] = s
            elif (s in self.nlp_proper_noun or s.lower() in self.nlp_pronouns) and quest_count == 0:
                self.question_thematic_roles["agent"] = s
            elif ((s in self.nlp_proper_noun or s.lower() in self.nlp_pronouns) and quest_count > 0 and
                  "agent" not in self.question_thematic_roles.keys()):
                self.question_thematic_roles["agent"] = s
            elif ((s in self.nlp_proper_noun or s.lower() in self.nlp_pronouns) and quest_count > 0 and
                  "verb" not in self.question_thematic_roles.keys()):
                self.question_thematic_roles["coagent"] = s
            elif ((s in self.nlp_proper_noun or s.lower() in self.nlp_pronouns) and sent_count > 0 and
                  "verb" in self.question_thematic_roles.keys()):
                self.question_thematic_roles["beneficiary"] = s
            elif ((s.lower() in self.nlp_nouns or det_flag) and quest_count > 0 and
                  "verb" in self.question_thematic_roles.keys() and prep_phrase is False):
                self.question_thematic_roles["object"] = s
            elif (s.lower() in self.nlp_nouns or det_flag) and quest_count > 0 and prep_phrase:
                if prep == "with":
                    self.question_thematic_roles["instrument"] = s
                elif prep == "by":
                    self.question_thematic_roles["conveyance"] = s
                elif prep == "to":
                    self.question_thematic_roles["thematicObj"] = s
            elif s.lower() in self.prepositions_list:
                prep_phrase = True
                prep = s.lower()
            elif s.lower in self.articles_list:
                det_flag = True
            quest_count += 1
        # print("self.sentence_thematic_roles: ", self.sentence_thematic_roles)
        # print("self.question_thematic_roles: ", self.question_thematic_roles)
        ############
        if self.question_list[0].lower() in (fw.lower() for fw in self.five_w_dict.keys()):
            q_word = self.question_list[0]
            method_ans = self.question_method(q_word, self.question_list)
            if method_ans is not None:
                return method_ans
            else:
                return self.guess_ans()
        elif self.question_list[0].lower() in (p.lower() for p in self.prepositions_list):
            prep_word = self.question_list[0]
            for q_words in self.question_list:
                if q_words.lower() in (fw.lower() for fw in self.five_w_dict.keys()):
                    q_word = q_words
                    method_ans = self.question_method(q_word, self.question_list)
                    if method_ans is not None:
                        return method_ans
                    else:
                        return self.guess_ans()

        return self.guess_ans()

    def guess_ans(self):
        ########
        remainder_list_1 = [s for s in self.remainder_list if s not in self.articles_list]
        remainder_list_2 = [s for s in remainder_list_1 if s not in self.adjectives_list]
        remainder_list_3 = [s for s in remainder_list_2 if s not in self.conjunctions_list]
        remainder_list_4 = [s for s in remainder_list_3 if s not in self.prepositions_list]
        rand_ans = remainder_list_4[-1]
        # print("random answer: ", rand_ans)
        return rand_ans
