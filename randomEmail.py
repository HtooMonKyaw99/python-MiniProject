import random
import string


def random_char(char_num):
     return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


for i in range(10):
    print(random_char(7) +"@gmail.com")
