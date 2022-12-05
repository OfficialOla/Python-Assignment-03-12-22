hello = "Hello There!!!"
# print(hello.endswith("!!!"))

# this is a replacement metheod that replace l with q
# print(hello.replace("l", "q", 1))

# split will split into a list
# print(hello.split("e"))
# you can plit by character
# print(hello.split("e"))

# partition return
# print(hello.partition("e"))
# partition can be from the right or left
# print(hello.rpartition("e"))

# translate is not like replace
bin_ = "101100011001011110"
# print(bin_.replace("1", "x").replace("0", "1").replace("x", "0"))
print(bin_.translate(str.maketrans("01", "10")))

# imagine you have a useless character in you string and u want to remove them, u use maketrans. e.g
bin_ = "1011***01!!00#g1043"
print(bin_.translate(str.maketrans("10  ", "01", "*!#g3")))