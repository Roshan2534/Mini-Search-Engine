'''
@author: Sougata Saha
Institute: University at Buffalo
'''

from linkedlist import LinkedList
from collections import OrderedDict


class Indexer:
    def __init__(self):
        """ Add more attributes if needed"""
        self.inverted_index = OrderedDict({})
        self.DocNum = None
        self.Termfq = None
        self.LenPost = None
        self.TermFreq = []
        self.Extracted = {}

    def get_index(self):
        """ Function to get the index.
            Already implemented."""
        return self.inverted_index

    def generate_inverted_index(self, doc_id, tokenized_document, Nterms, DocNum):
        """ This function adds each tokenized document to the index. This in turn uses the function add_to_index
            Already implemented."""
        self.DocNum = DocNum
        for t in tokenized_document.keys():
            self.add_to_index(t, doc_id, tokenized_document[t], Nterms, DocNum)

    def add_to_index(self, term_, doc_id_, tf, Nterms, DocNum):
        """ This function adds each term & document id to the index.
            If a term is not present in the index, then add the term to the index & initialize a new postings list (linked list).
            If a term is present, then add the document to the appropriate position in the posstings list of the term.
            To be implemented."""
        Term = term_
        DocID = doc_id_

        if Term not in self.inverted_index:
            # inverted[Term] = {LinkedList().insert_at_end(DocID)}
            self.inverted_index[Term] = LinkedList()

        Termfq = tf / Nterms
        self.Termfq = Termfq
        self.TermFreq.append(Termfq)
        self.inverted_index[Term].insert_at_end(DocID, Termfq)
        LenPostings = self.inverted_index[Term].get_NumPost()
        self.LenPost = LenPostings
        self.inverted_index[Term].idf = DocNum / LenPostings
        self.inverted_index[Term].length = LenPostings

    def sort_terms(self):
        """ Sorting the index by terms.
            Already implemented."""
        sorted_index = OrderedDict({})
        for k in sorted(self.inverted_index.keys()):
            sorted_index[k] = self.inverted_index[k]
        self.inverted_index = sorted_index
        # print(self.inverted_index.items())
        for key, value in self.inverted_index.items():
            self.Extracted.update(value.traverse_list_tm())

    def add_skip_connections(self):
        """ For each postings list in the index, add skip pointers.
            To be implemented."""
        skips = []
        for key, value in self.inverted_index.items():
            value.add_skip_connections()

    def calculate_tf_idf(self):
        for key, value1 in self.inverted_index.items():
            tm_freq = value1.traverse_list_tm()[0][1]
            for key2, value2 in self.Extracted.items():
                TFIDF = self.inverted_index[key].idf * tm_freq
                n = value1.start_node
                while n is not None:
                    n.set_tf_idf(TFIDF)
                    n = n.next

    def get_pList(self, term):
        dict_term = {}
        for key, value in self.Inverted_index.items():
            if term == key:
                dict_term[key] = value
        return dict_term
