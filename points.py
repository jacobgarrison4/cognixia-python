'''
Students have been assigned a series of math problems that have points associated with them. Given a sorted points array, minimize the number of problems a student 
needs to solve based on the criteria below:

 a. They must always solve the first problem, index i = 0
 
 b. After solving the i-th problem, they have a choice: solve the next problem (i + 1) or skip ahead and work the (i + 2)
  problem.
 
 c. Students must keep solving problems until the difference between the maximum points and the minimum points questions
  solved so far meets or exceeds a specified threshold
 
 d. If a student cannot meet or exceed the threshold, they must work through all the problems. 
 
 Return the minimum number of problems a student needs to solve. 
 
 minimum_points(2, [1, 2, 3]) -> 2
 Explanation: if a student solves points[0] = 1, points[2] = 3, the difference between the minimum and the maximum points
  solved is 3 - 1 = 2. This meets the threshold, so the student must solve at least 2 problems. Return 2.
minimum_points(4, [1, 2, 3, 5, 8]) -> 3
 If the threshold is 4, again it takes 3 problems solving problems 1, 3 and 4 where points[3] - points[0] = 5 - 1 = 4.
  This meets the threshold, so the student must solve at least 3 problems. Return 3
'''
'''
l = [1,3,5,8]
print(max(l))
print(min(l))
print(l[-1])
'''

def minimum_points(threshold, points):
    
    #See if threshold can be acheived, if not, return all problems
    if ((points[-1] - points[0]) < threshold):
        return len(points)
    
    #keep min points
    min_points = points[0]

    #They must solve first problem, start problem counter and index for which problem we are solving next
    #go to next problem, if threshold met, increment counter and break
    #if not met, go to i + 2 problem and check same criteria
    #if neither were met, increment counter and set index to i + 3 problem
    counter = 1
    index = 1
    thresh = False
    while thresh == False:
        if ((points[index] - min_points) >= threshold):
            counter += 1
            thresh = True
        elif ((points[index + 1] - min_points) >= threshold):
            counter += 1
            thresh = True
        else:
            counter += 1
            index +=2
    return counter

def test_1():
    assert minimum_points(2, [1, 2, 3]) == 2


def test_2():
    assert minimum_points(4, [1, 2, 3, 4, 5]) == 3


def test_3():
    assert minimum_points(4, [1, 2, 3, 5, 8]) == 3


def test_4():
    assert minimum_points(12, [1, 2, 3, 5, 8, 13, 14, 15, 18]) == 4


def test_5():
    assert minimum_points(100, [1]) == 1

test_1()
test_2()
test_3()
test_4()
test_5()









