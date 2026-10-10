def palindromes(text):
    is_palindrome = text == text[::-1]
    
    if is_palindrome:
        print(f"{text} is a palindrome!")
    else:
        print("that wasn't a palindrome")

    return is_palindrome


pal = False

while not pal:
    word = input("Please type in a palindrome: ")

    if palindromes(word):
        break