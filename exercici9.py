def switchFlags(currentFlag):
    if currentFlag == "0":
        currentFlag = "1"
    else:
        currentFlag = "0"

    return currentFlag

def chessboard(width):
    count = 1
    flag = "1"
    while count <= width:
        subcount = 1
        output = ""
        while subcount <= width:
            output = output + flag
            subcount += 1

            flag = switchFlags(flag)

        if width % 2 == 0:
            flag = switchFlags(flag)

        print(output)       
        count += 1
        

# Testing the function
if __name__ == "__main__":
    chessboard(6)
