class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
 
# --- List of Objects ---
students = [
    Student("Ali", 15), 
    Student("Sara", 9), 
    Student("Reza", 20)
]
 
with open("passed.txt", "w") as file:
    for s in students:
        if s.grade > 10:
            file.write(s.name + "\n")
