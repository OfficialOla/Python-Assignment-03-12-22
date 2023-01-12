set_val = {"hi" "hello" }
user_input = input("Enter a number ")
count = 0
for i in range(len(user_input)):
    if user_input[i] != set_val[i]:
        set_val.add(user_input[i])
    else:
        count +=1
        print(user_input[i])