import main
import math
import sec_tree


def find(temp_mail):
    #print(type(temp_mail))
    for i in range(len(temp_mail)):
        if temp_mail[i] == '@':
            return i


def invoke():
    ascii_store = []
    email_list = []
    # index = 1
    done = False
    while not done:
        # name = input("Enter the mail: ")
        list = main.get_info()
        # address=input("Enter your address: ")
        # ph_no=input("Enter your ph no: ")
        print(list)
        temp_mail = list.get('email')

        mailsplit = temp_mail[0:find(temp_mail)]

        se = 0
        for i in range(len(mailsplit)):
            se += ord(mailsplit[i])
        ascii_store.append(se)

        email_list.append(temp_mail)

        d_done = input("Press 'n' to exit or 'continue to another key :")
        if d_done == 'n' or d_done == 'N':
            done = True
    print(ascii_store)
    # import math
    # Seletion Sort..........
    def selection_sort(ascii_store:list,email_list:list):
        n = len(ascii_store)

        for i in range(n - 1):
            min = i
            for j in range(i + 1, n):

                if ascii_store[j] < ascii_store[min]:
                    min = j
            ascii_store[i], ascii_store[min] = ascii_store[min], ascii_store[i]
            email_list[i],email_list[min]=email_list[min],email_list[i]
        return ascii_store
    print(selection_sort(ascii_store,email_list))
    print(email_list)

    #print(selection_sort(email_list))

    search_name = input("Enter  email to search...:")
    sem = 0
    for i in range(len(search_name)):
        sem += ord(search_name[i])
    print(sem)
    # print(list[sem])


    def jump_search(A, item):
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

        return linear_search(B, item, i)


    def linear_search(B, item, loc):
        # print("\t Entering Linear Search")
        i = 0

        while i != len(B):
            if B[i] == item:
                # return f"found in index {loc+i} "
                print("found index ",loc+i)
                return i
            i += 1
        return -1

    #print(list[jump_search(ascii_store, sem)])
    print(list,linear_search(ascii_store,sem,0))
        #sec_data = sec_tree.tree
