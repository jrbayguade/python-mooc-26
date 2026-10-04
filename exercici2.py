ASTERISCS_WIDTH = 30 

word = input("Word: ")
# DEBUG 
#word = "test_long_words"
#*                              *
#*       test_long_words        *

count = 0
output1 = ""
output2 = ""
output3 = ""
starting_word_position = int(ASTERISCS_WIDTH / 2) - int(len(word)/2)
ending_word_position = starting_word_position + len(word)
index = 0

while count < ASTERISCS_WIDTH:
    output1 += "*"
    count += 1
count = 0

while count < ASTERISCS_WIDTH:
    output3 += "*"
    count += 1
count = 0

while count < ASTERISCS_WIDTH:
    if count >= starting_word_position and count < ending_word_position:
        output2 += word[index] 
        index += 1
    elif count == 0:
        output2 = "*"
    elif count == ASTERISCS_WIDTH - 1:
        output2 += "*"
    else:
        output2 += " "

    count += 1


print(output1)
print(output2)
print(output3)