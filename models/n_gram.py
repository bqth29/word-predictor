from typing import List, Tuple
from nltk import FreqDist
from nltk.util import ngrams 
from nltk.tokenize import RegexpTokenizer

import os

FILES = ['./data/' + filename for filename in os.listdir('./data')]

class FilterableDict(FreqDist):

    def __init__(self, n_gram_model: int, samples=None):
        super().__init__(samples)
        self.n_gram_model = n_gram_model

    def predict(self, words: List[str], first_characters: str = '') -> List[Tuple[str, int]]:

        assert len(words) == self.n_gram_model - 1

        filtered = list(
            filter(
                lambda item: (words == list(item[0])[:-1] and item[0][-1].startswith(first_characters)),
                self.items()
            )
        )

        sublist = [(key[-1], value) for key, value in filtered]
        sublist.sort(key = lambda y: y[1], reverse = True)

        return sublist

class nGramProcessor():

    def __init__(self, n: int, filenames: List[str]) -> None:
        
        self.n = n
        self.frequencies = FilterableDict(n)

        # Process the files

        for filename in filenames:

            print(f'Processing {filename}')
            textfile = open(filename, 'r', errors='ignore')

            for line in textfile:

                if len(line) > 1:
                    
                    # Remove non-letters characters
                    tokenizer = RegexpTokenizer(r'\w+')
                    tokenized = tokenizer.tokenize(line)
                    tokens = [word.lower() for word in tokenized]

                    n_grams = ngrams(tokens, n)
                    self.frequencies.update(n_grams)

            textfile.close()

model = nGramProcessor(3, FILES)
print(model.frequencies.predict(['see', 'you'], 'l'))