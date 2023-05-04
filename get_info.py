import random,string
import json
dict={}
for i in range(10):
    #create random email
    email = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(6, 12)))
#    print(f"Random email {email}@gmail.com")
    user_email=f'{email}@gmail.com'
    #random create password
    password = ''.join(random.choice(string.printable) for _ in range(8))
    p_word=password
    #create random name
    name = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(6, 12)))
    username=name    #random create phno
    def generate_ph_no():

        first=str(random.randint(100,999))
        second=str(random.randint(1,888)).zfill(3)
        last=(str(random.randint(1,9998)).zfill(4))
        while last in ['1111','2222','3333','4444','5555','6666','7777','8888']:
            last=(str(random.randint(1,9998)).zfill(4))
        return '{}-{}-{}'.format(first,second,last)
    num=generate_ph_no()
    dict.update({
        len(dict):{'email':user_email,'username':username,'password':p_word,'ph_no':num}
    })
print(dict)
f=open('datasaving.json','w')
f.write(json.dumps(dict))
f.close()