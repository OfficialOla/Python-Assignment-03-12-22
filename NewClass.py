class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def set_first_name(self, name):
        self.first_name = name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, name):
        self.last_name = name

    def get_last_name(self):
        return self.last_name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age



first_name = input("Enter first name ")
last_name = input("Enter last name ")
age = int(input("enter age "))
first_person = Person(last_name, first_name, age)
second_person = Person("Emmanuel", "Dabira", 30)
print(first_person.get_first_name(), first_person.get_last_name(), first_person.get_age())
print(second_person.get_first_name(), second_person.get_last_name(), second_person.get_age())
