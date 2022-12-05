import string
user_input = input("Enter the word to decode: ")
key = int(input("What key would you like to use: "))
lower_letters = string.ascii_lowercase
upper_case = string.ascii_uppercase
decoded_lower_letters = lower_letters[key:] + lower_letters[:key]
decoded_upper_letters = upper_case[key:] + upper_case[:key]

letters = lower_letters + upper_case + string.whitespace
decoded_letters = decoded_lower_letters + decoded_upper_letters + string.whitespace
encoded = user_input.translate(str.maketrans(letters, decoded_letters))
decoded = encoded.translate(str.maketrans(decoded_letters, letters))
# print(user_input.translate(str.maketrans(lower_letters +" ", decoded_lower_letters +" ")))
print(encoded)
print(decoded)
