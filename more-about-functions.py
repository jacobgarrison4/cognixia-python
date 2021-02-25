
def prob2(nums):
    for n in nums:
        if ((n % 2) == 1):
            print("Weird")
        elif ((n % 2) == 0 and n in range(2, 6)):
            print("Not Weird")
        elif ((n % 2) == 0 and n in range(6, 21)):
            print("Weird")
        elif ((n % 2) == 0 and n > 20):
            print("Not Weird")

numlist = [1,2,3,4,6,8,11,18,20]
prob2(numlist)

from math import floor

def center_zeroes(array):
    zero_count = 0
    middle = floor(len(array) / 2)
    for i in array:
        if i == 0:
            zero_count += 1
    for i in range(zero_count):
        array.remove(0)
    start = middle - (zero_count // 2)
    for i in range(zero_count):
        array.insert(start, 0)
    print(array)

center_zeroes([1,3,1])
center_zeroes([1,3,0])
center_zeroes([1,3,0,1])
center_zeroes([1,1,3,0,6,0])
center_zeroes([0,1,0,3,0,1,0,6,0,1,0,3,0,7])


def fibonacci():
    print(0)
    print(1)
    fib1 = 0
    fib2 = 1
    fib3 = 1
    while fib3 < 1000:
        fib3 = fib2 + fib1
        if fib3 >= 1000:
            break
        fib1 = fib2
        fib2 = fib3
        print(fib3)

fibonacci()
