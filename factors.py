user_input = int(input("enter number: "))
factor = 1
sum_of_factor = 0
while factor < user_input:
    if user_input % factor == 0:
        # sum_of_factor += factor
        print(factor)

    factor += 1
# if sum_of_factor < user_input:
#     print(user_input, "is deficient")
# elif sum_of_factor > user_input:
#     print(user_input, "is abundant")
# else:
#     print(user_input, "is a perfect number")
