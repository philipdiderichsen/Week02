#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

# Exercise 2.3:

# Write a script that takes this file (from this Kaggle competition), extracts the request_text field from each dictionary in the list, and construct a bag of words representation of the string (string to count-list).

# There should be one row pr. text. The matrix should be N x M where N is the number of texts and M is the number of distinct words in all the texts.

# The result should be a list of lists ([[0,1,0],[1,0,0]] is a matrix with two rows and three columns).

import json
import os
import sys


def extract_requests(jsontxt): 
  """
  :param jsonfile: Json input as string
  :returns: List of request strings 
  """

  # Get json representation of data
  pizza_json = json.loads(jsontxt)

  # Extract a list of request texts
  request_list = [d['request_text'] for d in pizza_json]

  return(request_list)


def request_to_countlist(l, terms): 
  """
  :param l: List representation of request text
  :param terms: List of distinct terms
  :returns: List of counts of each term from terms in l
  """

  counts = [l.count(term) for term in terms]

  return(counts)


#def build_matrix


if __name__ == '__main__':
  # Try method with 1 arg
  try:
 
    print(sys.argv[1])

  except IndexError as e: 
    
    print('No input file specified. Using data/pizza-train.json.\n')
    
    infile = os.path.abspath(os.path.dirname(__file__)) + '/../data/pizza-train.json'
    
    pizza_train = open(infile, 'r').read()

    # List of request strings
    request_list = extract_requests(pizza_train)

    # Number of texts
    N = len(request_list)

    # Convert request texts to lists
    requests_as_lists = [s.split() for s in request_list]

    # Flatten list of request lists, get distinct values with set(), convert back to list
    distinct_terms = list(set([term for reqst in requests_as_lists for term in reqst]))
    
    # Number of distinct terms
    M = len(distinct_terms)
    
    print(N, M)

    # Build matrix. One list of counts for each request-as-list
    matrix = [request_to_countlist(reqst, distinct_terms) for reqst in request_list]

    print(str(distinct_terms[:10]))
    print( '\n'.join([str(l[:10]) for l in matrix][:8])  )

