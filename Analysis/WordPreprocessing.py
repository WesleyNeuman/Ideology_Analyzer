import nltk
import stop_words
import numpy as np
import pandas as pd
import time

class Preprocessor(object):

    def __init__(self):
        self.tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
        self.stopper = stop_words.get_stop_words('en')
        self.p_stemmer = nltk.PorterStemmer()

    def get_tokens(self, text: str) -> list:
        return self.tokenizer.tokenize(text)

    def remove_stop(self, words: list):
        return [i for i in words if not i in self.stopper]

    def stem(self, words: list):
        return [self.p_stemmer.stem(i) for i in words]





