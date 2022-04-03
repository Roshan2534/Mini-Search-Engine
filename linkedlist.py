'''
@author: Sougata Saha
Institute: University at Buffalo
'''

import math


class Node:

    def __init__(self, value=None, next=None, tmfreq=None, TF_IDF=None):
        """ Class to define the structure of each node in a linked list (postings list).
            Value: document id, Next: Pointer to the next node
            Add more parameters if needed.
            Hint: You may want to define skip pointers & appropriate score calculation here"""
        self.value = value
        self.tmfreq = tmfreq
        self.next = next
        self.TF_IDF = TF_IDF
        self.skip_pointer = None

    def add_skip_pointer(self, node):
        self.skip_pointer = node

    def set_skip_none(self, node):
        self.skip_pointer = None

    def set_tf_idf(self, TFIDF):
        self.TF_IDF = TFIDF

    def get_skip_pointer(self, node):
        return self.skip_pointer


class LinkedList:
    """ Class to define a linked list (postings list). Each element in the linked list is of the type 'Node'
        Each term in the inverted index has an associated linked list object.
        Feel free to add additional functions to this class."""

    def __init__(self):
        self.start_node = None
        self.end_node = None
        self.length, self.n_skips, self.idf = 0, 0, 0.0
        self.skip_length = None

    def traverse_list(self):
        traversal = []
        if self.start_node is None:
            print("List has no element")
            return []
        else:
            n = self.start_node
            # Start traversal from head, and go on till you reach None
            while n is not None:
                traversal.append(n.value)
                n = n.next
            return traversal

    def traverse_list_tm(self):
        traversal = []
        if self.start_node is None:
            print("List has no element")
            return []
        else:
            n = self.start_node
            # Start traversal from head, and go on till you reach None
            while n is not None:
                traversal.append([n.value, n.tmfreq])
                n = n.next
            return traversal

    def get_NumPost(self):
        traversal = []
        if self.start_node is None:
            print("List has no element")
            return []
        else:
            n = self.start_node
            # Start traversal from head, and go on till you reach None
            while n is not None:
                traversal.append(n.value)
                n = n.next
                NumPostings = len(traversal)

            return NumPostings

    def traverse_skips(self):
        traversal2 = []
        if self.start_node is None:
            return
        else:
            n = self.start_node
            # Start traversal from head, and go on till you reach None
            while n is not None:
                traversal2.append(n.value)
                n = n.skip_pointer
            return traversal2

    def add_skip_connections(self):
        n_skips = math.floor(math.sqrt(self.length))
        difference = abs((n_skips - math.sqrt(self.length)))
        if difference > 0.5:
            n_skips = n_skips + 1
        """ Write logic to add skip pointers to the linked list. 
            This function does not return anything.
            To be implemented."""

        if (n_skips < 2):
            start_node = self.start_node
            node = start_node
            start_node.set_skip_none(node)

            return
        else:
            # print(n_skips)
            # ("This is n_skips")
            i = 0
            z = 0
            skip_length = 1
            starting_node = self.start_node
            while i <= n_skips:
                node = starting_node
                # print(i)
                # print("This is i")
                i += 1
                while z != n_skips:
                    # print(z)
                    # print("This is z")
                    z += 1
                    if node is not None:
                        node = node.next
                if z == n_skips:
                    # print(z)
                    # print("Are they equal")
                    # print(n_skips)
                    if node is not None:
                        starting_node.add_skip_pointer(node)
                    skip_length += 1
                    z = 0
                    starting_node = node
            self.skip_length = skip_length

    def insert_at_end(self, value, tmfreq):
        new_node = Node(value=value, tmfreq=tmfreq)
        n = self.start_node

        if self.start_node is None:
            self.start_node = new_node
            self.end_node = new_node
            return

        elif self.start_node.value >= value:
            self.start_node = new_node
            self.start_node.next = n
            return

        elif self.end_node.value <= value:
            self.end_node.next = new_node
            self.end_node = new_node
            return
        else:
            while n.value < value < self.end_node.value and n.next is not None:
                n = n.next

            m = self.start_node
            while m.next != n and m.next is not None:
                m = m.next
            m.next = new_node
            new_node.next = n
            return

    def insert_at_end_TFIDF(self, value, TFIDF):
        new_node = Node(value=value, TF_IDF=TFIDF)
        n = self.start_node

        if self.start_node is None:
            self.start_node = new_node
            self.end_node = new_node
            return

        elif self.start_node.TF_IDF >= TFIDF:
            self.start_node = new_node
            self.start_node.next = n
            return

        elif self.end_node.TF_IDF <= TFIDF:
            self.end_node.next = new_node
            self.end_node = new_node
            return
