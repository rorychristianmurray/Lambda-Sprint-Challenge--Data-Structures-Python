from bst import BinarySearchTree
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# orig approach O(n^2)
# duplicates = []
# for name_1 in names_1:  # O(n)
#     for name_2 in names_2:  # O(n)
#         if name_1 == name_2:
#             duplicates.append(name_1)


# bst
# instantiate tree
duplicates = []
n_tree = BinarySearchTree(None)
for name_1 in names_1:
    n_tree.insert(name_1)

for name_2 in names_2:
    if n_tree.contains(name_2):
        duplicates.append(name_2)

    # dict approach
# duplicates = []
# n1_dict = dict()

# # create a dict from name_1
# for name_1 in names_1:
#     n1_dict[name_1] = name_1
#     # print(f"name1 : {name_1}")

# # print(n1_dict)

# for name_2 in names_2:
#     if name_2 in n1_dict:
#         duplicates.append(name_2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
