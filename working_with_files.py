file = open('generic_text.txt', 'r')
for line in file:
    print("This line says: ", line)

file.close()

print('*************************')

# OR #

with open('generic_text.txt', 'r') as f:
    print(f.read(10)) #automatically closes file

print('*************************')

with open('generic_text.txt', 'r') as f:
    print(f.readlines()) #automatically closes file

print('*************************')

with open('generic_text.txt', 'r') as f:
    print(f.readline()) #automatically closes file
    print(f.readline())
    print(f.readline().strip())
    print(f.readline())

print('*************************')

#with open('generic_text.txt', 'a') as f:    #append
#   f.write("\nfifth line")

new_contents = ['new line 1', 'new line 2']
'''
with open('generic_text.txt', 'r') as f:
    old_contents = f.readlines()

with open('generic_text.txt', 'a') as f:
    for item in new_contents:
        f.write('\n' + item)
    f.write('\n')
    for item in old_contents:
        f.write(item)

with open('new_generic_text.txt', 'w+') as f:
    for item in new_contents:
        f.write(item + '\n')
'''

with open('generic_text.txt', 'r') as f:
    print(f.readlines())
    f.seek(0)
    lines_list = list(map(lambda i: i.replace("\n", ""), f.readlines()))
    print(lines_list)

