'''
Please write a function named length_of_longest, which takes a list of strings as its argument. 
The function returns the length of the longest string.

my_list = ["first", "second", "fourth", "eleventh"]

result = length_of_longest(my_list)
print(result)

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = length_of_longest(my_list)
print(result)

Sample output

8
7
'''

def length_of_longest(strlist:list):
    longest = ""

    for str in strlist:
        if len(str)>len(longest):
            longest = str

    return len(longest)

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richardson"]

result = length_of_longest(my_list)
print(result)