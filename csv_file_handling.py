import csv as c
# from csv import DictWriter as dw

with open("C:/Users/Manav/Downloads/student_data.csv", "r") as file:
    reader = c.reader(file)
    for row in reader:
        print(row)

# with open("C:/Users/Manav/Downloads/student_data.csv", "r") as file:
#     reader = c.DictReader(file)
#     for row in reader:
#         print(row)

# with open("C:/Users/Manav/Downloads/student_data.csv", "w") as file:
#     writer = c.writer(file)
#     writer.writerow(['student_id', 'student_name', 'age', 'gender', 'course', 'marks'])
#     writer.writerow(['111', 'Manav J', '24', 'Male', 'Data Science', '90'])
#     writer.writerow(['112', 'John D', '25', 'Male', 'Data Engineering', '85'])
#     writer.writerow(['113', 'Jane S', '26', 'Female', 'Data Analytics', '95'])
#     writer.writerow(['114', 'Jim C', '27', 'Male', 'Data Science', '88'])
#     writer.writerow(['115', 'Jill K', '28', 'Female', 'Data Engineering', '92'])
#     writer.writerow(['116', 'Jack L', '29', 'Male', 'Data Analytics', '89'])
#     writer.writerow(['117', 'Jill M', '30', 'Female', 'Data Science', '91'])
#     writer.writerow(['118', 'Jill N', '31', 'Female', 'Data Engineering', '87'])
#     writer.writerow(['119', 'Jill O', '32', 'Female', 'Data Analytics', '93'])
#     writer.writerow(['120', 'Jill P', '33', 'Female', 'Data Science', '86'])
file.close()

