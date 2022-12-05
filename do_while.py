# # # walrus equation
# # # score = int(input("enter a number or -1 to exit: "))
# # while (score := int(input("enter a number or -1 to exit: "))) != -1:
# #     print(score)
# #     # score = int(input("enter a number or -1 to exit: "))
#
# for i in range(1, 11):
#     print("*" * i)

string = "mississippi is the longest river"
# print(string[27:32])
# print(string[-5:])
# print(string[15:18])
# print(string[0:8])
# print(string[:23:4])
# print(string[:-18:-1])
# # print(string[:])
# print(string[-15:-33:-1])
#
# user = int(input("Enter a number: "))
# if user == (user[::-1]):
#     print("palindrome")
# u = int(input("Enter a nuber: "))
# u = str(u)
# if u == u[::-1]:
#     print("palindrome")

# name = "Yinka"
# age = 18
# s = "{} is {} years old and he loves {}".format(name, age, "Java")
# s = f"{name:-^20} is {age:>10.2%} years old, and {name} loves{'Java'}"
# print(s)
# hello_world = "hello world now"
# for index, letter in enumerate(hello_world):
#     print(f"{letter} --> {index}")
# for index in range(len(hello_world)):
#     print(f"{hello_world[index]}-->{index}")
# for i in range(1, 21, 3):
#     s = "*" * i
#     print(f"{s:20}{s:^20}{s:>20}")

# for i in range(1, 21, 2):
#     asterisk = "*" * i
#     print(asterisk.center(20))
# merry = "merry christmas"
# print(merry.upper().center(19, "*"))
# student = 1
# if student == 30:
#     print("start class")
# elif student >= 20 or student <= 29:
#     print("start playing")
# else:
#     print("go home")
# to print string in word
#  for i in range(len(word):
# if word[1] == "b"
# print (word[i]) or to print index print (i)
# to print value in word
# for i, value in enumerate(word):
# if value == "b"
# print(v)

word = "Hello boss baby"
for i in range(len(word)):
    if word[i] == "b":
        print(word[i])
print(word)
for index, word in enumerate(word):
    if word != "b":
        print(word)
for index, word in enumerate(word):
    if word == "b":
        print(word)

# print(word)
# word = "Hello boss baby"
# for index, letter in enumerate(word):
#     print(f"{letter} --> {index}")