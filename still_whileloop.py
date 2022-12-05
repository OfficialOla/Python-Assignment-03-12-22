# counter controlled loop
count = 0
largest_so_far = float("-inf")
smallest_number = float("+inf")
while count < 5:
    num = int(input("Enter a number: "))
    if num > largest_so_far:
        largest_so_far = num
    if num < smallest_number:
        smallest_number = num

    count += 1
print()
print("The largest number is", largest_so_far)
print("The smallest number is", smallest_number)
