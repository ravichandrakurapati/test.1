user_database={"john":"Password123","jane":"abc123","smith":"pass45"}
print(type(user_database))

student_grades={"jhon":"85","rayn":"65"}
print(student_grades)

student_grades["jhon"]="100"
print(student_grades)
print(user_database.keys())
student_grades["ravi"]="99"
student_grades.setdefault("pooji")
student_grades["pooji"]="100"
student_grades["ravi"]="100"
student_grades.setdefault("akhil")
print(student_grades)
print(student_grades["ravi"])