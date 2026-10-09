while True:
    editor = input("Editor: ").lower()

    if editor == "visual studio code":
        print("an excellent choice!")
        break
    elif editor == "notepad":
        print("awful")
    else:
        print("not good")