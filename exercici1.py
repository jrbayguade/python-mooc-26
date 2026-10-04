LONGITUD = 20

frase = input("Please type in a string: ")
output = ""
espai = LONGITUD - len(frase)
cont = 0
index = 0

while cont < LONGITUD:
    if cont < espai:
        output += "*"
    else:
        output += frase[index]
        index += 1

    
    cont +=1

print(output)


'''
while cont < 20:
    if cont < len(frase):
        output += frase[cont]
    else:
        output += "*"
    
    cont +=1

print(output)
'''