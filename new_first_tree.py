import math
import re
import string
#from random import random
import random


class Node:
    def __init__(self):
        self.data = None
        self.link_sec_tree = None
        self.store_sec_tree = None
        self.left = None
        self.right = None


def get_info():
    done = False
    while not done:
        email = input("Enter your email: ")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        ph_no = input("Enter your ph no: ")
        address = input("Enter your address: ")
        budget_count = int(input("Enter your budget count: "))
        data = {'email': email, 'name': name, 'password': password, 'ph_no': ph_no, 'address': address,
                'budget_count': budget_count}
        # val_mail=[data.get("email")]
        exits = input("Press n to exit or another key to continue: ")
        if exits == "n" or exits == "N": done = True
        return data


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
        print(node.store_sec_tree)
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


def search_data(node: Node, name: str,count):
    if node.data == name[0]:
        if not node.link_sec_tree:
            return None
        count+=1
        return search_sec_data(node.link_sec_tree, name,count)
    elif node.data < name[0]:
        count+=1
        return search_data(node.right, name,count)
    else:
        count+=1
        return search_data(node.left, name,count)


def search_sec_data(node: Node, name: str,count):
    count+=1
    if node.data == len(name):
        if not node.store_sec_tree:
            return None
        print(node.store_sec_tree)
        # return node.store_sec_tree[node.store_sec_tree.index(name)]
        count+=1
        return linear_search(node.store_sec_tree, name,count)
        print(node.store_sec_tree)
    elif node.data < len(name):
        return search_sec_data(node.right, name,count)
    else:
        return search_sec_data(node.left, name,count)


"""def selection_sort(ascii_store: list, email_list: list):
    n = len(ascii_store)

    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):

            if ascii_store[j] < ascii_store[min]:
                min = j
        ascii_store[i], ascii_store[min] = ascii_store[min], ascii_store[i]
        email_list[i], email_list[min] = email_list[min], email_list[i]
    return ascii_store
    print(selection_sort(ascii_store, email_list))
    print(email_list)"""


def find(temp_mail):
    # print(type(temp_mail))
    for i in range(len(temp_mail)):
        if temp_mail[i] == '@':
            return i


"""def jump_search(A, item):
    print("Searching the name.....")
    n = len(A)  # Length of the array
    m = int(math.sqrt(n))  # Step length
    i = 0  # Starting interval

    while i != len(A) - 1 and A[i] < item:
        print("Processing Block - {}".format(A[i: i + m]))
        if A[i + m - 1] == item:  # Found the search key
            return i + m - 1
        elif A[i + m - 1] > item:  # Linear search for key in block
            B = A[i: i + m - 1]
            return linear_search(B, item, i)
        i += m

    B = A[i:i + m]  # Step 5
    print("Processing Block - {}".format(B))

    return linear_search(B, item, i)"""


def linear_search(B, item,count):
    # print("\t Entering Linear Search")
    i = 0

    while i != len(B):
        if B[i] == item:
            # return f"found in index {loc+i} "
            print('found',end='')
            print(count,'times')
            return B[i]
        i += 1
    return 'not found'


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check(email):
    if (re.search(regex, email)):
        return True
    else:
        return False


def random_char():
    username = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(6, 12)))
    return f"{username}@gmail.com"


# def generate_random_email():
#     username=''.join(random.choice(string.ascii_lowercase)for _ in range(random.randint(6,12)))
#     domain=''.join(random.choice(string.ascii_lowercase)for _ in range(random.randint(6,10)))
#     tld=random.choice(['com','net','org'])
#     return f"{username}@{domain}.{tld}"


if __name__ == '__main__':
    #first_tree = create_tree()
    email_list = []
    first_tree = create_tree()

    index = 0

    while index < 10:
        # email=generate_random_email()
        email = random_char()
        insert_data(first_tree, email)
        count=0
        search_data(first_tree,email,count)
        #print(email)
        #email_list.append(email)
        index += 1
    # print(email_list)
    #
    # insert_data(first_tree, email)

    # ndata=get_info()
    # name = input("Enter your email: ")
    # while name:
    #     # store_SE_value = []
    #     # val_mail=[ndata.get("email")]
    #     if check(name):
    #         # while name:
    #         insert_data(first_tree, name)
    #         name = input("Enter your email: ")
    #     else:
    #         print("Invalid Email! Please reenter your email!")
    #         name = input("Enter your email: ")
    #
    #     # ascii = convert_to_Ascii(name)
    #     # store_SE_value.append(ascii)
    #
    #search_name = input("Enter the search name: ")
    # # print(jump_search(store_sec_tree, name))
    # # print(' ')
    # # print(store_SE_value)
    #print(search_data(first_tree, search_name))
