items=['mango','Orange','htoo','Mon']
file=open('item.txt','w')
for item in items:
    file.write(item+'\n')
print(file)
file.close()