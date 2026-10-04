sentence = input("Please type in a sentence:")
#sentence = "la marina està morena"
index = 0
firstLetter = True

if len(sentence) > 0:
    while index < len(sentence):
        if index == 0:
            print(sentence[index])
            firstLetter = False
        else:
            letter = sentence[index]

            if letter != " " and firstLetter == True:
                firstLetter = False
                print(letter)
            elif letter == " " and firstLetter == False:
                firstLetter = True

        index +=1

