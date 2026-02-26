
names = ["Sara", "Andi", "Festa"]

for name in names:
    print(names)

sentence = "Hello world"

for character in sentence:
    if character.isalpha():
        print(character)

for number in range(1,9):
    print(number)

number = [1, 35, 45, 78, 99, 84, 55]

maximum = number[0]

for num in number:
    if num > maximum:
        maximum = num
        print("The biggest number is the number " , maximum)