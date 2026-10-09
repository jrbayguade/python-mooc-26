'''
Please write a function named same_chars, which takes one string and two integers as arguments. 
The integers refer to indexes within the string. The function should return True if the two 
characters at the indexes specified are the same. Otherwise, and especially if either of the 
indexes falls outside the scope of the string, the function returns False.

Some examples of how the function is used:
'''

def same_chars(chars, index_0, index_1):
    if index_0 < 0 or index_1 <0 or index_1 > len(chars):
        return False
    elif chars[index_0] == chars[index_1]:
        return True
    else:
        return False


print(same_chars("programmer", 6, 7))
print(same_chars("programmer", 0, 4)) 
print(same_chars("programmer", 0, 12))