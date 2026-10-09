'''
Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters as specified by the examples below.

squared("ab", 3)
print()
squared("aybabtu", 5)

Sample output:

aba
bab
aba

aybab
tuayb
abtua
ybabt
uayba
'''

def squared(usr_string, usr_number):
    index = 0
    row_count = 0
    
    while row_count < usr_number:
        row = ""
        col_count = 0
        
        while col_count < usr_number:
            row += usr_string[index % len(usr_string)]
            index += 1
            col_count += 1
            
        print(row)
        row_count += 1

squared("ab", 3)
print()
squared("aybabtu", 5)