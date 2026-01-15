nums = [10, 20, 30, 40, 50, 60]
# print(nums[-3:])
# #Replace 30 with 35
# # nums[2] = 35
# if 30 in nums:
#     index= nums.index(30)
#     nums[index] = 35
#     print(nums)

# nums.append(70)
# print(nums)

# if 20 in nums:
#     index= nums.index(20)
#     nums.pop(index)
#     print(nums)
# else:
#     print("20 is not in the list")

# prices = [100, 200, 300, 400]
# price=[price*0.1 + price for price in prices]
# print(price)


# prices = [100, 200, 300, 400]
# price=[price*0.1 + price for price in prices]
# int_list = [int(x) for x in price]
# print(int_list)

# orders = [500, 200, 900, 400, 700]
# orders.sort()
# print(orders)

# orders.sort(reverse=True)
# print(orders)

# data = [1, 2, 3, 4, 5]
# for i in data:
#     if i % 2 == 0:
#         print(i)

# employee = ("Manav", "Data Engineer", 85000)
# print(employee[0])
# print(employee[1])
# # employee[2] = 90000
# # print(employee)

# cities = ("Tampa", "Miami", "Orlando", "Tampa", "Miami")
# print(cities.count("Tampa"))
# print(cities.index("Miami"))

# skills = {"Python", "SQL", "AWS", "Python", "SQL"}
# print(skills)

# data_science = {"Python", "SQL", "Pandas", "ML"}
# data_engineering = {"Python", "SQL", "Spark", "AWS"}
# print(data_science & data_engineering)
# print(data_science)
# print(data_engineering | data_science)


# emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com"]
# email_set = set(emails)
# print(email_set)
# email=list(email_set)
# print(email)

# student = {
#     "name": "Manav",
#     "major": "Computer Science",
#     "gpa": 3.88
# }
# print(student["gpa"])
# student.update({"University": "Kent State University"})
# print(student)
# student.update({"gpa": 3.90})
# print(student)

# sales = {
#     "Jan": 5000,
#     "Feb": 7000,
#     "Mar": 6000
# }
# total_sales = 0
# for sale in sales.values():
#     total_sales += sale
# print(total_sales)


# employees = {
#     "E01": {"name": "Amit", "salary": 70000},
#     "E02": {"name": "Priya", "salary": 90000},
#     "E03": {"name": "Rahul", "salary": 85000}
# }
# print(employees["E03"]["salary"])

# Max_salary = 0
# for employee in employees.values():
#     if employee["salary"] > Max_salary:
#         Max_salary = employee["salary"]
#         max_employee = employee["name"]
# print(max_employee, Max_salary)

# orders = [
#     {"order_id": 1, "amount": 500, "customer": "A"},
#     {"order_id": 2, "amount": 800, "customer": "B"},
#     {"order_id": 3, "amount": 500, "customer": "A"},
#     {"order_id": 4, "amount": 1000, "customer": "C"}
# ]


# print(orders[0].keys())
# print(orders[0].values())
# print(orders[0].items())


# revenue = 0
# for order in orders:
#     revenue += order["amount"]
# print(revenue)

# #Find total spending per customer
# customer_spending = {}
# for order in orders:
#     customer = order["customer"]
#     amount = order["amount"]
#     if customer in customer_spending:
#         customer_spending[customer] += amount
#     else:
#         customer_spending[customer] = amount
# print(customer_spending)

# #print all customers
# for order in orders:
#     print(order["amount"])


# test_dict={
#   "metric": "revenue",
#   "breakdown": "plan",
#   "bars": [
#     { "label": "Free", "value": 1200 },
#     { "label": "Pro",  "value": 48200 },
#     { "label": "Ent",  "value": 91000 }
#   ]
# }
# print(test_dict["metric"])
# print(test_dict["breakdown"])
# print(test_dict["bars"])
# print(test_dict["bars"][0]["label"])
# print(test_dict["bars"][0]["value"])
# print(test_dict["bars"][1]["label"])
# print(test_dict["bars"][1]["value"])
# print(test_dict["bars"][2]["label"])



ecommerce_data = {
    "platform": "ShopNow",
    "country": "USA",
    "generated_at": "2026-01-15",

    "customers": {
        "C001": {
            "name": "Manav Jaiswal",
            "email": "manav@gmail.com",
            "city": "Tampa",
            "loyalty_points": 1250,

            "orders": {
                "O1001": {
                    "date": "2026-01-10",
                    "status": "Delivered",
                    "payment": {
                        "method": "Credit Card",
                        "transaction_id": "TXN9001",
                        "amount": 1200
                    },
                    "items": {
                        "P01": {"name": "Laptop", "price": 1000, "quantity": 1},
                        "P02": {"name": "Mouse", "price": 100, "quantity": 2}
                    }
                },

                "O1002": {
                    "date": "2026-01-12",
                    "status": "Shipped",
                    "payment": {
                        "method": "PayPal",
                        "transaction_id": "TXN9002",
                        "amount": 500
                    },
                    "items": {
                        "P03": {"name": "Keyboard", "price": 500, "quantity": 1}
                    }
                }
            }
        },

        "C002": {
            "name": "Amit Sharma",
            "email": "amit@gmail.com",
            "city": "Mumbai",
            "loyalty_points": 700,

            "orders": {
                "O1003": {
                    "date": "2026-01-11",
                    "status": "Delivered",
                    "payment": {
                        "method": "UPI",
                        "transaction_id": "TXN9003",
                        "amount": 800
                    },
                    "items": {
                        "P04": {"name": "Tablet", "price": 800, "quantity": 1}
                    }
                }
            }
        }
    }
}

print(ecommerce_data["customers"].keys())
print(ecommerce_data["customers"]["C001"].keys())
