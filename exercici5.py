while True:
    num_input = int(input("Please type in a number: "))

    if num_input <= 0:
        break

    pas = 1
    factorial = 1

    while pas <= num_input:
        factorial *= pas
        pas += 1

    print(f"The factorial of the number {num_input} is {factorial}")

print("Thanks and bye!")