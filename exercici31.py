'''
Please write a function named even_numbers, which takes a list of integers as an argument. 
The function returns a new list containing the even numbers from the original list.

my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)

Sample output

original [1, 2, 3, 4, 5]
new [2, 4]
'''

def even_numbers(ints:list):
    nova_llista = []

    for i in ints:
        if i % 2 == 0:
            nova_llista.append(i)

    return nova_llista

my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)