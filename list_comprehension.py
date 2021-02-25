l = [1,2,3,4,5]

[print(i) for i in l if i > 3] #list comprehension

print()

(print(i) for i in l if i >= 3) #generator

print()

print(list(map(lambda x: x ** 2, l)))























