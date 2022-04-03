'''
@author: Sougata Saha
Institute: University at Buffalo
'''

import collections
from nltk.stem import PorterStemmer
import re
from nltk.corpus import stopwords
import nltk
from collections import Counter

nltk.download('stopwords')
PS = PorterStemmer()

class Node:

    def __init__(self, value=None, next=None):
        """ Class to define the structure of each node in a linked list (postings list).
            Value: document id, Next: Pointer to the next node
            Add more parameters if needed.
            Hint: You may want to define skip pointers & appropriate score calculation here"""
        self.value = value
        self.next = next

class Preprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.ps = PorterStemmer()

    def get_doc_id(self, doc):
        """ Splits each line of the document, into doc_id & text.
            Already implemented"""
        arr = doc.split("\t")
        return int(arr[0]), arr[1]

    def tokenizer(self, text):
        """ Implement logic to pre-process & tokenize document text.
            Write the code in such a way that it can be re-used for processing the user's query.
            To be implemented."""

        SpecRemoved = re.sub(r"[^a-zA-Z0-9]+", ' ', text)

        Tokenized_Text = SpecRemoved.split()
        StopRemoved = []
        countterms = []
        stop_words = set(stopwords.words('english'))
        for sw in Tokenized_Text:
            if sw not in stop_words:
                StopRemoved.append(sw)
        Stemed = []

        for Stop in StopRemoved:
            i = PS.stem(Stop)
            Stemed.append((i))

        Tf_Stemed = Counter(Stemed)
        NTerms = len(Stemed)

        return Tf_Stemed, NTerms

