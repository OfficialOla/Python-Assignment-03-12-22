user_input = int(input("enter a number: "))


def left_asterisk(input):
    for i in range(1, input, 1):
        i = i * "*"
        print(i)


left_asterisk(user_input)
print()

user_input = int(input("enter a number: "))


def right_asterisk(input):
    for i in range(1, input, 1):
        i = i * "*"
        print(f"{i:>{input}}")


right_asterisk(user_input)
print()

user_input = int(input("enter a number: "))


def print_diamond(input1):
    for i in range(-1, input1, 2):
        i = i * "*"
        print(i.center(input1))
    for j in range(input1, -1, -2):
        asterisk = j * "*"
        print(asterisk.center(input1))


print_diamond(user_input)
print()
