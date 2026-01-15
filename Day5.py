# def squares(x):
#     return x*x
# num = 10
# print(squares(num))


# def greet_student(name,score):
#     # print(f"Hello {name}, your score is {score}")
#     print("Hello,",name,"!")
#     print("Your score is",score)
#     if score >= 90:
#         print("Excellent job!")
#     elif score >= 80:
#         print("Good job!")
#     else:
#         print("You need to work harder!")

# greet_student("Alice", 90)
# greet_student("Bob", 80)
# greet_student("Charlie", 70)


# list=["Alice", "Bob", "Charlie", "Manav"]
# def greet(name):
#     for name in list:
#         print("Hello,",name,"!")
# greet(list)

# def add_numbers(*args):
#     return sum(args)
# print(add_numbers(1, 2, 3, 4, 5))

# def print_numbers(*args):
#     for num in args:
#         print(num)
# print_numbers(1, 2, 3, 4, 5)

# def print_numbers(*args):
#         print(args)
# print_numbers(1, 2, 3, 4, 5)


# def create_user_profile(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
# create_user_profile(name="Manav", age=26, location="Tampa")
# create_user_profile(name="John", age=25, location="New York")
# create_user_profile(name="Jane", age=24, location="Los Angeles")

def create_user_profile(**kwargs):
    profile={}
    for key, value in kwargs.items():
        profile[key] = value    
    return profile
print(create_user_profile(name="Manav", age=26, location="Tampa"))
print(create_user_profile(name="John", age=25, location="New York"))
print(create_user_profile(name="Jane", age=24, location="Los Angeles"))
user_1=create_user_profile(name="Manav", age=26, location="Tampa")
user_2=create_user_profile(name="John", age=25, location="New York")
user_3=create_user_profile(name="Jane", age=24, location= None)
print(user_1)
print(user_2)
print(user_3)


