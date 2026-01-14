# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])
# print(fruits[2])
# fruits.append("date")
# print(fruits)
# # print(fruits[10])

# fruits[1] = "blueberry"
# print(fruits)
# fruits.insert(1, "mango")
# print(fruits)

# numbers = (1, 2, 3, 4, 5)
# print(numbers[0:2])

# nums=[1,1, 2, 2, 3, 3, 4, 4, 5, 5]
# print(nums)
# nums=set(nums)
# print(nums)
# print(type(nums))

person=dict(name="Sam", age=14, city="Delhi")
print(person)
print(person["name"])
print(person["age"])
print(person["city"])
print(person.get("name"))
print(person.get("age"))
print(person.get("number"))

person["email"]="abc@gmail.com"
print(person)
person["age"]=26
print(person)
person.pop("email")
print(person)
person["email"]="abc@gmail.com"
print(person)
person.popitem()
print(person)
person["email"]="abc@gmail.com"
print(person)
del person["email"]
print(person)
print(person.keys())
print(person.values())

for key, value in person.items():
    print(key, value)

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

