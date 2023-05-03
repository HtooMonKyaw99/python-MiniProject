import math
import random
import string


class Node:
    def __init__(self):
        self.data = None
        self.link_sec_tree = None
        self.store_sec_tree = None
        self.left = None
        self.right = None


total = []


def insert_data_to_tree(tree: Node, data: list):  # insert_tree_data
    if len(data) > 0:
        # mid=len(data)//2
        if len(data) % 2 == 0:
            mid = (len(data) // 2) - 1
            tree.data = data[mid]
            if len(data[:mid]) > 0:
                tree.left = Node()
                insert_data_to_tree(tree.left, data[:mid])
            if len(data[mid + 1:]) > 0:
                tree.right = Node()
                insert_data_to_tree(tree.right, data[mid + 1:])
        else:
            mid = len(data) // 2
            tree.data = data[mid]
            if len(data[:mid]) > 0:
                tree.left = Node()
                insert_data_to_tree(tree.left, data[:mid])
            if len(data[mid + 1:]) > 0:
                tree.right = Node()
                insert_data_to_tree(tree.right, data[mid + 1:])


def insert_sec_data(node: Node, name: str):
    # print(node.data, node.store_sec_tree)
    if node.data == len(name):

        print(node.store_sec_tree)
        if not node.store_sec_tree:
            node.store_sec_tree = []

        idx = index(node.store_sec_tree, name)
        node.store_sec_tree = node.store_sec_tree[:idx] + [name] + node.store_sec_tree[idx:]
        # print(node.store_sec_tree)
        # convert_to_Ascii(node.store_sec_tree)
        # print(node.store_sec_tree)
    elif node.data < len(name):
        insert_sec_data(node.right, name)
    else:
        insert_sec_data(node.left, name)


# second tree
def insert_data(node: Node, name: str):
    if node.data == name[0]:
        if not node.link_sec_tree:
            node.link_sec_tree = create_sec_tree()
        insert_sec_data(node.link_sec_tree, name)
    elif node.data < name[0]:
        insert_data(node.right, name)
    else:
        insert_data(node.left, name)


def compare_str(str1, str2):
    for i in range(len(str2)):
        if str1[i] > str2[i]:
            return True
        elif str1[i] < str2[i]:
            return False


def index(arr: list, num):
    for i in range(len(arr)):
        if compare_str(arr[i], num): return i
    return len(arr)


def printing(tree: Node):
    if tree is not None:
        printing(tree.left)
        print(tree.data)
        printing(tree.right)


def tree_data():
    tree = []
    for i in range(97, 123):
        tree.append(chr(i))
    return tree


def sec_tree_data():
    sec_tree = []
    for x in range(1, 51):
        sec_tree.append(x)
    return sec_tree


def create_tree():
    data = tree_data()
    tree_node = Node()
    insert_data_to_tree(tree_node, data)
    # printing(tree_node)
    return tree_node


def create_sec_tree():
    sec_data = sec_tree_data()
    # print(sec_data)
    tree = Node()
    insert_data_to_tree(tree, sec_data)
    # print(sec_data)
    return tree


'''def convert_to_Ascii(arr: str):
    ascii_store = []
    # index = 1
    while arr:

        mailsplit = arr[0:find(arr)]

        se = 0
        for i in range(len(mailsplit)):
            se += ord(mailsplit[i])
        ascii_store.append(se)
        # print(ascii_store)
        return ascii_store'''


def search_data(node: Node, name: str, ct):
    if node.data == name[0]:
        if not node.link_sec_tree:
            return None
        ct += 1
        return search_sec_data(node.link_sec_tree, name, ct)
    elif node.data < name[0]:
        ct += 1
        return search_data(node.right, name, ct)
    else:
        ct += 1
        return search_data(node.left, name, ct)


def search_sec_data(node: Node, name: str, ct):
    ct += 1
    if node.data == len(name):
        if not node.store_sec_tree:
            return None
        print(node.store_sec_tree)
        # return node.store_sec_tree[node.store_sec_tree.index(name)]
        ct += 1
        return linear_search(node.store_sec_tree, name, ct)
        print(node.store_sec_tree)
    elif node.data < len(name):
        ct += 1
        return search_sec_data(node.right, name, ct)
    else:
        ct += 1
        return search_sec_data(node.left, name, ct)


def linear_search(B, item, ct):
    # print("\t Entering Linear Search")
    i = 0

    while i != len(B):
        if B[i] == item:
            # return f"found in index {loc+i} "
            print('found at', end=' ')
            print(ct, 'times')
            total.append(ct)
            return B[i]
        i += 1
    return 'not found'


import re

# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


# Define a function for
# for validating an Email
def check(email):
    # pass the regular expression
    # and the string into the fullmatch() method
    if re.fullmatch(regex, email):
        return True

    else:
        return False


"""def generate_email():
    # Generate a random username of length between 6 and 12 characters
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(6, 12)))
    # Generate a random domain name of length between 6 and 10 characters
    domain = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(6, 10)))
    # Append a random top-level domain (TLD)
    tld = random.choice(['com', 'net', 'org'])
    # Concatenate the username, domain, and TLD to form the email address
    return f"{username}@gmail.com"""


def random_char():
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(6, 12)))
    return f"{username}@gmail.com"

if __name__ == '__main__':
    # first_tree = create_tree()

    count = 1000
    email_list=[]
    fir_tree = create_tree()
    while count > 0:
        email = random_char()
        insert_data(fir_tree, email)
        cot = 0
        search_data(fir_tree, email, cot)

        count = count - 1
    with open('listfile.txt', 'w') as filehandle:
        for listitem in email:
            filehandle.write(f'{listitem}\n')
        #print(filehandle)
sum = 0
for i in total:
    sum += i
print("Average time for searching is ", sum / 1000)

# while name:5
#
#     if check(name):
#
#         insert_data(first_tree, name)
#         name =generate_email()
#         findData = input('enter s to search.')
#         if findData == 's':
#             search_name = input("Enter the search name: ")
#             print(search_data(first_tree, search_name))
#
#         else:
#             print('None')
#
#     else:
#         print("Invalid email format.")
#         name = input("Enter your email: ")
