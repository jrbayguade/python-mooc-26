'''
Please write a function named no_vowels, which takes a string argument. The function returns a new string, 
which should be the same as the original but with all vowels removed.

You can assume the string will contain only characters from the lowercase English alphabet a...z.

An example of expected behaviour:

my_string = "this is an example"
print(no_vowels(my_string))

Sample output

ths s n xmpl
'''

def no_vowels(text: str):
    text = text.replace("a","")
    text = text.replace("e","")
    text = text.replace("i","")
    text = text.replace("o","")
    text = text.replace("u","")

    return text

my_string = "this is an example"
print(no_vowels(my_string))