num_input = int(input("Please type in a number: "))
#num_input = 3

target_1 = False
target_2 = False

base1 = 1
base2 = 0

if num_input >= 0:
    while target_1 == False:
        while target_2 == False:
            if base2 < num_input:
                base2 += 1
                print(f"{base1} x {base2} = {base1 * base2}")
            else:
                target_2 = True
                break

        if base1 < num_input:
                base1 += 1
                base2 = 1
                target_2 = False

                print(f"{base1} x {base2} = {base1 * base2}")

               
        else:
            target_1 = True
            continue

        