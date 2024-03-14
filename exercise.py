students_list = []
students_dict = {}
students_list.append("Rinchen")
students_dict["Rinchen"] = "25"

students_list.append("Pema")
students_dict["Pema"] = "15"

students_list.append("Kinzang")
students_dict["Kinzang"] = "10"

students_name = input("Enter students name:")
if students_name in students_list:
    print(f"Student found! age:{students_dict[students_name]}")
else:
    print("Student not found")

print("List of students")
for students in students_list:
    print(students)

remove_student = input("Enter the students name to remove or else enter to skip:")
if remove_student in students_list:
    remove_age = students_dict[remove_student]
    students_list.remove(remove_student)
    students_dict.remove(remove_age)
    del students_dict[remove_student]
    print("Student removed successfully")
    print("Students available: ", students_list)
else:
    print("Student not found!")



