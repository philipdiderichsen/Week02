#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

# Exercise 2.2:

# Write a script that takes an integer N, and outputs all bit-strings of length N as lists. For example: 3 -> [0,0,0], [0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]. As a sanity check, remember that there are 2^N such lists.

# Do not use the bin-function in Python. Do not use strings at all. Do not import anything. Try to solve this using only lists, integers, if-statements, loops and functions.

import ast
import os
import re
import sys


def binfunc(n):
  """
  :param n: bitstring length
  :returns: list of all bitstrings of length n
  """

  # Initialize list of bit-strings-as-lists
  l = [[0], [1]]
 
  # Length > 1: Run iterations
  if n > 1:
    # Range 1 less than n because of values already in l
    for a in range(n - 1): 

      # Initialize list to capture extended bit-strings
      extended_bitstrings = []

      # For each element in the initialized list
      for i in l: 

        # .. pair it with each binary value
        for j in [0, 1]: 

          # .. and add it to the list of extended bit-strings
          extended_bitstrings.append(i + [j])

      # Now go again with the extended bitstrings
      l = extended_bitstrings

  # Length < 1: Return None. 
  if n < 1: 
    l = None

  # Length 1: Return initial list.
  # l is already initial list. 


  return(l)

  

if __name__ == '__main__':
  # Try method with 1 arg
  try:
 
    # Afslut hvis inputtet ikke er et tal
    if not re.search(r'[0-9]+', sys.argv[1]):
       sys.exit('Error - Input must be an integer.\n')
 
    # Input integer 
    n = int(sys.argv[1])
    
    # Lav binære tal
    bin_list = binfunc(n)

    # Sanity check ..
    if (not len(bin_list) == 2**n) and (not bin_list is None): 
      sys.exit('Error - Number of bit-strings is wrong ..')

    # Print hvis alt er godt
    print(str(bin_list))
    
  except IndexError as e: 
    
    print(e, '- Missing input integer.\n')
