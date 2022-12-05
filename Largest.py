count = 0
largest = 0
larger = 0
smallest = 0

while count < 5:
    num = int(input("Enter a number: "))
    if num > largest:
        larger = largest
        largest = num
    elif num < smallest:
        smallest = num

    count += 1
print("The largest number is", largest)
print("The second largest number is", larger)
