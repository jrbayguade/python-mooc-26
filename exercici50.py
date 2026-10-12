'''
Please write a phone book application. It should work as follows:
Sample output

command (1 search, 2 add, 3 quit): 2
name: peter
number: 040-5466745
ok!
command (1 search, 2 add, 3 quit): 2
name: emily
number: 045-1212344
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
040-5466745
command (1 search, 2 add, 3 quit): 1
name: mary
no number
command (1 search, 2 add, 3 quit): 2
name: peter
number: 09-22223333
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
09-22223333
command (1 search, 2 add, 3 quit): 3
quitting...
'''

data = {}

while True:
    comanda = input("command (1 search, 2 add, 3 quit): ")

    match comanda:
        case "1": # Search
            name = input("name: ")

            if name in data:
                item = data[name]
                print(item)
            else:
                print("no number")

            continue

        case "2": # Add
            name = input("name: ")
            number = input("number: ")
            data[name] = number
            print("ok!")

            continue

        case "3": # Quit
            break