from PIL.ImImagePlugin import number

while True:

    user_input = input("Please enter a positive number")

    if user_input.isnumeric():
        number = int(user_input)

        if number > 0:
         break

    print("The number you entered isn't valid")

print("You entered a valid number", user_input)