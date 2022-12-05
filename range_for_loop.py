user_input = int(input("Enter a number from 1 - 100: "))
for count in range(1, user_input + 1):
        # print(i, end=" ")
        if count % 15 == 0:
            print("FIZZBUZZ")
        elif count % 5 == 0:
            print("FIZZ")
        elif count % 3 == 0:
         print("BUZZ")
        else:
         print(count)
