class MyClass:
    def __init__(self):
        self.name = "John"

    def create_age(self, age):
        self.age = age


# Create an object of MyClass
my_object = MyClass()

# Call create_age() method to create the age object variable
my_object.create_age(25)

# add a new object variable
my_object.sex = "Helicopter"

# Access the age object variable
print(my_object.age)  # Output: 25
# print the sex object variable
print(my_object.sex)  # Output: Helicopter
