'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(lista):
  print(f"List max: {max(lista)}")
  print(f"List min: {min(lista)}")
  print(f"List average: {sum(lista) / len(lista)}")
  print(f"List sum: {sum(lista)}")

stats(example_list)
