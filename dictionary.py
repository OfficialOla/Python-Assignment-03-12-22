value = dict(name="Mr sam", age=30)
# print(value)
value = {
    'name': "James Carragher",
    'age': 30,
    'skill': {
        'soft': ["Barbing", "Communication"],
        'tech': ["Backend", "Frontend", "Content writing"],}
}
a = value['skill']["tech"][1]
print(a)
print(value["skill"]["soft"][0])
# print(value['skill']["tech"])
# print(value['age'])
# print(value['skill']['tech'])
