'''
Please write a function named list_sum which takes two lists of integers as arguments. 
The function returns a new list which contains the sums of the items at each index in the 
two original lists. You may assume both lists have the same number of items.

An example of the function at work:

a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b)) # [8, 10, 12]
'''

def list_sum(int1:list, int2:list):
    newList = []

    for i in range(len(int1)):
        newList.append(int1[i] + int2[i])

    return newList

a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b)) # [8, 10, 12]