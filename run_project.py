'''
@author: Sougata Saha
Institute: University at Buffalo
'''

from tqdm import tqdm
from preprocessor import Preprocessor
from indexer import Indexer
from collections import OrderedDict
from linkedlist import LinkedList
import inspect as inspector
import sys
import argparse
import json
import time
import random
import flask
from flask import Flask
from flask import request
import hashlib

app = Flask(__name__)

class ProjectRunner:
    def __init__(self):
        self.preprocessor = Preprocessor()
        self.indexer = Indexer()

    def _merge(self, term1, term2):
        """ Implement the merge algorithm to merge 2 postings list at a time.
            Use appropriate parameters & return types.
            While merging 2 postings list, preserve the maximum tf-idf value of a document.
            To be implemented."""
        Merged_list = LinkedList()
        if type(term1) is str:
            dict_term1 = {}
            dict_term2 = {}
            num_comparisons = 0
            Inverted_index = self.indexer.get_index()
            for key, value in Inverted_index.items():
                if term1 == key:
                    dict_term1[key] = value
            for key, value in Inverted_index.items():
                if term2 == key:
                    dict_term2[key] = value

            l1 = dict_term1[term1]
            n1 = l1.start_node
            print(dict_term1[term1].traverse_list())
            print("THis is 1")

            l2 = dict_term2[term2]
            n2 = l2.start_node

            while n1 is not None and n2 is not None:
                num_comparisons += 1
                if n1.value == n2.value:
                    if n1.TF_IDF < n2.TF_IDF:
                        Merged_list.insert_at_end_TFIDF(n2.value, n2.TF_IDF)
                    else:
                        if n1.TF_IDF == n2.TF_IDF:
                            Merged_list.insert_at_end_TFIDF(n1.value, n1.TF_IDF)
                        else:
                            Merged_list.insert_at_end_TFIDF(n1.value, n1.TF_IDF)
                    n1 = n1.next
                    n2 = n2.next
                else:
                    if n1.value < n2.value:
                        n1 = n1.next
                    else:
                        n2 = n2.next

            return Merged_list, num_comparisons

        else:
            n1 = term1.start_node
            dict_term2 = {}
            num_comparisons = 0
            Inverted_index = self.indexer.get_index()
            for key, value in Inverted_index.items():
                if term2 == key:
                    dict_term2[key] = value

            l2 = dict_term2[term2]
            n2 = l2.start_node
            print(dict_term2[term2].traverse_list())
            print("THis is 2")
            while n1 is not None and n2 is not None:
                num_comparisons += 1
                if n1.value == n2.value:
                    if n1.TF_IDF < n2.TF_IDF:
                        Merged_list.insert_at_end_TFIDF(n2.value, n2.TF_IDF)
                    else:
                        if n1.TF_IDF == n2.TF_IDF:
                            Merged_list.insert_at_end_TFIDF(n1.value, n1.TF_IDF)
                        else:
                            Merged_list.insert_at_end_TFIDF(n1.value, n1.TF_IDF)
                    n1 = n1.next
                    n2 = n2.next
                else:
                    if n1.value < n2.value:
                        n1 = n1.next
                    else:
                        n2 = n2.next

            return Merged_list, num_comparisons

    def _merge_with_skips(self, term1, term2):
        Merged_list = LinkedList()
        if type(term1) is str:
            dict_term1 = {}
            dict_term2 = {}
            num_comparisons = 0
            Inverted_index = self.indexer.get_index()
            for key, value in Inverted_index.items():
                if term1 == key:
                    dict_term1[key] = value

            for key, value in Inverted_index.items():
                if term2 == key:
                    dict_term2[key] = value
            l1 = dict_term1[term1]
            n1 = l1.start_node

            l2 = dict_term2[term2]
            n2 = l2.start_node

            print(dict_term1[term1].traverse_list())
            print("THis is 3")
            print(dict_term2[term2].traverse_list())
            while n1 is not None and n2 is not None:
                num_comparisons += 1
                if n1.value == n2.value:
                    if n1.TF_IDF < n2.TF_IDF:
                        Merged_list.insert_at_end_TFIDF(n2.value, n2.TF_IDF)
                    else:
                        if n1.TF_IDF == n2.TF_IDF:
                            Merged_list.insert_at_end_TFIDF(n1.value, n1.TF_IDF)
                        else:
                            Merged_list.insert_at_end_TFIDF(n1.value, n1.TF_IDF)
                    n1 = n1.next
                    n2 = n2.next
                else:
                    if n1.value < n2.value:
                        if n1.skip_pointer is not None and n1.skip_pointer.value < n2.value:
                            while n1.skip_pointer is not None:
                                if n1.skip_pointer.value < n2.value:
                                    n1 = n1.skip_pointer
                        else:
                            n1 = n1.next
                    else:
                        if n2.skip_pointer is not None and n2.skip_pointer.value < n1.value:
                            while n2.skip_pointer is not None:
                                if n2.skip_pointer.value < n1.value:
                                    n2 = n2.skip_pointer
                        else:
                            n2 = n2.next

            return Merged_list, num_comparisons
        else:
            n1 = term1.start_node
            dict_term2 = {}
            num_comparisons = 0
            Inverted_index = self.indexer.get_index()
            for key, value in Inverted_index.items():
                if term2 == key:
                    dict_term2[key] = value

            l2 = dict_term2[term2]
            n2 = l2.start_node

            print(dict_term2[key].traverse_list())
            print("THis is 4")
            while n1 is not None and n2 is not None:
                num_comparisons += 1
                if n1.value == n2.value:
                    if n1.TF_IDF < n2.TF_IDF:
                        Merged_list.insert_at_end_TFIDF(n2.value, n2.TF_IDF)
                    else:
                        if n1.TF_IDF == n2.TF_IDF:
                            Merged_list.insert_at_end_TFIDF(n1.value, n1.TF_IDF)
                        else:
                            Merged_list.insert_at_end_TFIDF(n1.value, n1.TF_IDF)
                    n1 = n1.next
                    n2 = n2.next
                else:
                    if n1.value < n2.value:
                        if n1.skip_pointer is not None and n1.skip_pointer.value < n2.value:
                            while n1.skip_pointer is not None:
                                if n1.skip_pointer.value < n2.value:
                                    n1 = n1.skip_pointer
                        else:
                            n1 = n1.next
                    else:
                        if n2.skip_pointer is not None and n2.skip_pointer.value < n1.value:
                            while n2.skip_pointer is not None:
                                if n2.skip_pointer.value < n1.value:
                                    n2 = n2.skip_pointer
                        else:
                            n2 = n2.next

            return Merged_list, num_comparisons

    def _daat_and(self, Queries, skip):
        """ Implement the DAAT AND algorithm, which merges the postings list of N query terms.
            Use appropriate parameters & return types.
            To be implemented."""
        postings = []
        Inverted_index = self.indexer.get_index()
        Total_Comparisons = 0
        Final = []
        length = len(postings)
        for query in Queries:
            postings.append(query)

        term1 = postings[0]
        term2 = postings[1]
        if skip:
            merged, comparisons = self._merge_with_skips(term1, term2)
            Total_Comparisons += comparisons
        else:
            merged, comparisons = self._merge(term1, term2)
            Total_Comparisons += comparisons

        for i in range(2, length):
            if skip:
                merged, comparisons = self._merge_with_skips(merged, postings[i])
                Total_Comparisons += 1
                if skip:
                    merged.add_skip_connections()
            else:
                merged, comparisons = self._merge(merged, postings[i])
                Total_Comparisons += 1

        MergedList = merged.traverse_list()

        return MergedList, Total_Comparisons

    def _get_postings(self, term):
        """ Function to get the postings list of a term from the index.
            Use appropriate parameters & return types.
            To be implemented."""
        return self.indexer.get_pList(term)

    def _output_formatter(self, op):
        """ This formats the result in the required format.
            Do NOT change."""
        if op is None or len(op) == 0:
            return [], 0
        op_no_score = [int(i) for i in op]
        results_cnt = len(op_no_score)
        return op_no_score, results_cnt

    def run_indexer(self):
        """ This function reads & indexes the corpus. After creating the inverted index,
            it sorts the index by the terms, add skip pointers, and calculates the tf-idf scores.
            Already implemented, but you can modify the orchestration, as you seem fit."""
        with open('input_corpus.txt', 'r') as fp:
            DocNum = len(fp.readlines())
            fp.close()
        with open('input_corpus.txt', 'r') as fp:
            for line in tqdm(fp.readlines()):
                doc_id, document = self.preprocessor.get_doc_id(line)
                tokenized_document, Nterms = self.preprocessor.tokenizer(document)
                self.indexer.generate_inverted_index(doc_id, tokenized_document, Nterms, DocNum)
        self.indexer.sort_terms()
        self.indexer.add_skip_connections()
        self.indexer.calculate_tf_idf()

    def sanity_checker(self, command):
        """ DO NOT MODIFY THIS. THIS IS USED BY THE GRADER. """

        index = self.indexer.get_index()
        kw = random.choice(list(index.keys()))
        return {"index_type": str(type(index)),
                "indexer_type": str(type(self.indexer)),
                "post_mem": str(index[kw]),
                "post_type": str(type(index[kw])),
                "node_mem": str(index[kw].start_node),
                "node_type": str(type(index[kw].start_node)),
                "node_value": str(index[kw].start_node.value),
                "command_result": eval(command) if "." in command else ""}

    def run_queries(self, query_list, random_command):
        """ DO NOT CHANGE THE output_dict definition"""
        output_dict = {'postingsList': {},
                       'postingsListSkip': {},
                       'daatAnd': {},
                       'daatAndSkip': {},
                       'daatAndTfIdf': {},
                       'daatAndSkipTfIdf': {},
                       'sanity': self.sanity_checker(random_command)}

        for query in tqdm(query_list):
            """ Run each query against the index. You should do the following for each query:
                1. Pre-process & tokenize the query.
                2. For each query token, get the postings list & postings list with skip pointers.
                3. Get the DAAT AND query results & number of comparisons with & without skip pointers.
                4. Get the DAAT AND query results & number of comparisons with & without skip pointers,
                    along with sorting by tf-idf scores."""

            input_term_arr, Nterms = self.preprocessor.tokenizer(query)

            for term in input_term_arr:
                postings, skip_postings = self.indexer.inverted_index[term].traverse_list(), \
                                          self.indexer.inverted_index[term].traverse_skips()

                """ Implement logic to populate initialize the above variables.
                    The below code formats your result to the required format.
                    To be implemented."""

                output_dict['postingsList'][term] = postings
                output_dict['postingsListSkip'][term] = skip_postings

            daat_no_skip, daat_no_skip_comparisons = self._daat_and(input_term_arr, False)
            and_op_no_skip = daat_no_skip
            and_comparisons_no_skip = daat_no_skip_comparisons

            daat_skip, daat_no_skip_comparisons = self._daat_and(input_term_arr, True)
            and_op_skip = daat_skip
            and_comparisons_skip = daat_no_skip_comparisons

            daat_tfidf_no_skip, daat_tfidf_no_skip_comparisons = self._daat_and(input_term_arr, False)
            and_op_no_skip_sorted = daat_tfidf_no_skip
            and_comparisons_no_skip_sorted = daat_no_skip_comparisons

            daat_tfidf_skip, daat_tfidf_skip_comparisons = self._daat_and(input_term_arr, True)
            and_op_skip_sorted = daat_tfidf_skip
            and_comparisons_skip_sorted = daat_tfidf_skip_comparisons
            # and_op_no_skip, and_op_skip, and_op_no_skip_sorted, and_op_skip_sorted = None, None, None, None
            # and_comparisons_no_skip, and_comparisons_skip, and_comparisons_no_skip_sorted, and_comparisons_skip_sorted = None, None, None, None
            """ Implement logic to populate initialize the above variables.
                The below code formats your result to the required format.
                To be implemented."""
            and_op_no_score_no_skip, and_results_cnt_no_skip = self._output_formatter(and_op_no_skip)
            and_op_no_score_skip, and_results_cnt_skip = self._output_formatter(and_op_skip)
            and_op_no_score_no_skip_sorted, and_results_cnt_no_skip_sorted = self._output_formatter(
                and_op_no_skip_sorted)
            and_op_no_score_skip_sorted, and_results_cnt_skip_sorted = self._output_formatter(and_op_skip_sorted)

            output_dict['daatAnd'][query.strip()] = {}
            output_dict['daatAnd'][query.strip()]['results'] = and_op_no_score_no_skip
            output_dict['daatAnd'][query.strip()]['num_docs'] = and_results_cnt_no_skip
            output_dict['daatAnd'][query.strip()]['num_comparisons'] = and_comparisons_no_skip

            output_dict['daatAndSkip'][query.strip()] = {}
            output_dict['daatAndSkip'][query.strip()]['results'] = and_op_no_score_skip
            output_dict['daatAndSkip'][query.strip()]['num_docs'] = and_results_cnt_skip
            output_dict['daatAndSkip'][query.strip()]['num_comparisons'] = and_comparisons_skip

            output_dict['daatAndTfIdf'][query.strip()] = {}
            output_dict['daatAndTfIdf'][query.strip()]['results'] = and_op_no_score_no_skip_sorted
            output_dict['daatAndTfIdf'][query.strip()]['num_docs'] = and_results_cnt_no_skip_sorted
            output_dict['daatAndTfIdf'][query.strip()]['num_comparisons'] = and_comparisons_no_skip_sorted

            output_dict['daatAndSkipTfIdf'][query.strip()] = {}
            output_dict['daatAndSkipTfIdf'][query.strip()]['results'] = and_op_no_score_skip_sorted
            output_dict['daatAndSkipTfIdf'][query.strip()]['num_docs'] = and_results_cnt_skip_sorted
            output_dict['daatAndSkipTfIdf'][query.strip()]['num_comparisons'] = and_comparisons_skip_sorted

        return output_dict


@app.route("/execute_query1", methods=['POST'])
def execute_query1():
    queries = request.json["queries"]
    random_command = request.json["random_command"]
    return 'Success' + str(queries)


@app.route("/execute_query", methods=['POST'])
def execute_query():
    """ This function handles the POST request to your endpoint.
        Do NOT change it."""
    start_time = time.time()

    queries = request.json["queries"]
    random_command = request.json["random_command"]

    """ Running the queries against the pre-loaded index. """
    output_dict = runner.run_queries(queries, random_command)

    """ Dumping the results to a JSON file. """
    with open(output_location, 'w') as fp:
        json.dump(output_dict, fp)

    response = {
        "Response": output_dict,
        "time_taken": str(time.time() - start_time),
        "username_hash": username_hash
    }
    return flask.jsonify(response)


if __name__ == "__main__":
    """ Driver code for the project, which defines the global variables.
        Do NOT change it."""

    output_location = "project2_output.json"
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--corpus", type=str, help="Corpus File name, with path.")
    parser.add_argument("--output_location", type=str, help="Output file name.", default=output_location)
    parser.add_argument("--username", type=str,
                        help="Your UB username. It's the part of your UB email id before the @buffalo.edu. "
                             "DO NOT pass incorrect value here")

    argv = parser.parse_args()

    corpus = argv.corpus
    output_location = argv.output_location
    username_hash = hashlib.md5(argv.username.encode()).hexdigest()

    """ Initialize the project runner"""
    runner = ProjectRunner()

    """ Index the documents from beforehand. When the API endpoint is hit, queries are run against
        this pre-loaded in memory index. """
    runner.run_indexer()

    app.run(host="0.0.0.0", port=9999)
