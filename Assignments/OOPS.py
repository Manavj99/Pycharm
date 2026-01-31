class myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, {self.name}! You are {self.age} years old.")

obj = myclass("Manav", 26)
obj.greet()