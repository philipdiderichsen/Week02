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

  pizza_json = json.loads(jsontxt)

  request_list = [d['request_text'] for d in pizza_json]

  return(request_list)



if __name__ == '__main__':
  # Try method with 1 arg
  try:
 
    print(sys.argv[1])


  except IndexError as e: 
    
    print('No input file specified. Using data/pizza-train.json.\n')
    
    infile = os.path.abspath(os.path.dirname(__file__)) + '/../data/pizza-train.json'
    
    pizza_train = open(infile, 'r').read()

    request_list = extract_requests(pizza_train)

    print(str(request_list[:2])) 
