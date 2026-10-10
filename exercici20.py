
list = []
index = 1

while True:
    print(f"The list is now {list}")
    action = input("a(d)d, (r)emove or e(x)it: ")

    if action.lower() == "x":
        break
    elif action.lower() == "d":
        index += 1
        list.append(index)
    elif action.lower() == "r":
        index -= 1
        list.pop()