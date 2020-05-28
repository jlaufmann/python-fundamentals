'''
Write a script that takes a tuple and turns it into a list.

'''

# KISS - Keep It Simple Stupid!

tuple_ = [(1, 2, 3, 4), 'str_object', (5, 6), (7, 8, 9), 10, (11, (12, 13))]
# tuple_ = 'a',
print(f"tuple_ = {tuple_}")

#####################################################################
# sub-tuples will be converted to sub-lists, but sub-sub-tuples will not be converted to sub-sub-lists.
# If it is not desired to convert sub-tuples to sub-lists, the code between these hashed lines should be commented out.
for i in range(len(tuple_)):
    if isinstance(tuple_[i], tuple):  # if there are sub-tuples in the main tuple
        tuple_[i] = list(tuple_[i])  # sublists are converted to tuples
#####################################################################

list_ = list(tuple_)
print(f"list_ = {list_}")
