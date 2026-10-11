'''
Please write a function named everything_reversed, which takes a list of strings as its argument. 
The function returns a new list with all of the items on the original list reversed. Also the order 
of items should be reversed on the new list.

An example of how the function should work:

my_list = ["Hi", "there", "example", "one more"]
new_list = everything_reversed(my_list)
print(new_list)

Sample output

['erom eno', 'elpmaxe', 'ereht', 'iH']
'''

def everything_reversed(strs:list):
    newList = []
    finalList = []

    for i in range(len(strs) - 1, -1, -1):
        newList.append(strs[i])

    for i in newList:
        element = ""
        for j in range(len(i) - 1, -1, -1):
            element += i[j]

        finalList.append(element)


    return finalList

my_list = ["Hi", "there", "example", "one more"]
new_list = everything_reversed(my_list)
print(new_list)