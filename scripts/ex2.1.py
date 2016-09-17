#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

# Exercise 2.1:

# Write a script with two methods. The first method should read in a matrix like the one here and return a list of lists. The second method should do the inverse, namely take, as input, a list of lists and save it in a file with same format as the initial file. The first method should take the file name as a parameter. The second method should take two arguments, the list of lists, and a filename of where to save the output.

import ast
import os
import sys

def mat2list(matrix = '1 2 3\n2 4 6'): 
  """ 
  Transform a text matrix to a list of lists. 
  :param matrix: A matrix as space- and newline separated text.
  :returns: A list of lists.
  """
  
  # Split matrix into rows - after stripping leading and trailing space
  list_of_rows = matrix.strip().split('\n')

  # Split each list into elements
  list_of_lists = [row.split() for row in list_of_rows]

  # Change number strings to digits
  list_of_lists = [[int(s) for s in split_row] for split_row in list_of_lists]

  return(list_of_lists)


def list2mat(l = [[2, 3, 3], [4, 4, 4]], outfile = '../data/matrix.out.txt'): 
  """
  Transform a list of lists to a matrix and write it to file
  :param l: List of lists of numbers describing a matrix
  :returns: Returns nothing, prints matrix to outfile
  """
  
  # Convert list values to strings
  inner_strings = [[str(i) for i in inner_list] for inner_list in l]
 
  # Join inner lists
  list_of_strings = [' '.join(inner_list) for inner_list in inner_strings]

  # Join outer list
  text_matrix = '\n'.join(list_of_strings) + '\n'

  print(text_matrix)
  
  # Prepare outfile
  out = open(outfile, 'w')

  # Write result to outfile
  out.write(text_matrix)


if __name__ == '__main__':
  # Try method with 2 args
  try:
    # Filename from 2nd arg
    outfile = sys.argv[2]

    # Create list from string input 
    list_of_lists = ast.literal_eval(sys.argv[1])

    # Convert list of lists to matrix and write it to filename
    list2mat(list_of_lists, outfile)

  except IndexError as e: 

    # Try method with 1 arg
    try:
      # Read file contents
      matrix = open(sys.argv[1]).read()
      
      print(matrix)

      # Make list of lists
      list_of_lists = mat2list(matrix) 
      
      # Print the list of lists
      print(list_of_lists)

    # Error handling
    except IndexError as e: 
      print(e, '- husk korrekt antal argumenter. "[[2, 3], [4, 4]]" <outputfil> eller <matrixfil>')
