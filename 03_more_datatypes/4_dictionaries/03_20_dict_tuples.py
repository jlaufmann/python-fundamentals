'''
CHALLENGE: Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

NOTE: Check out the Python docs and see whether you can come up with a solution, even if you don't yet
      completely understand _why_ it works the way it does:
      https://docs.python.org/3/howto/sorting.html#key-functions
      Feel free to discuss any questions you have with your mentor and on the forum!

'''

input_dict = {"item1": 5, "item2": 6, "item3": 1, "item4": 2}
print(f"input_dict = {input_dict}")

result_list = [(k, v) for k, v in input_dict.items()]
result_list = sorted(result_list, key=lambda values: values[1])

# OR:
'''
keys = list(input_dict.keys())
vals = list(input_dict.values())

result_list = []
while len(vals) > 0:
    min_ind = vals.index(min(vals))
    result_list.append((keys.pop(min_ind), vals.pop(min_ind)))
'''
print(f"result_list = {result_list}")
