class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Employee name : {self.name}, Age = {self.age}")

    def __str__(self):
        return f"Employee(name={self.name}, age={self.age})"

emp1 = Employee("Alice", 30)
emp1.display_info()
print(emp1)  # Now prints a readable string