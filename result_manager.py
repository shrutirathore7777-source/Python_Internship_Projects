class StudentManager:
    def __init__(self, filename = "students.txt"):
        self.filename = filename
        self.students = []
        self.load_from_file()

    def add_students(self ,name , marks):
        grade = self.calculate_grade(marks)
        student = {"name": name , "marks": marks , "grade": grade}
        self.students.append(student)
        self.save_to_file()
        print(f"{name} added successfully!")
    
    def calculate_grade(self , marks):
        if marks>= 90:
            return "A+"
        elif marks>=75:
            return "A"
        elif marks >= 60:
            return "B"
        elif marks >= 45:
            return "C"
        else:
            return "F"
    
    def view_students(self):
        print("------Students Records-------")
        for s in self.students:
            print(f"name: {s['name']}, marks: {s['marks']}, grade:{s['grade']}")
    print("--------------------\n")

    def save_to_file(self):
        with open(self.filename ,"w") as f:
            for s in self.students:
                f.write(f"NAME: {s['name']},MARKS: {s['marks']} ,GRADE: {s['grade']}")

    def load_from_file(self):
        try:
            with open (self.filename, "r") as f:
                for line in f:
                    name , marks , grade = line.strip().split(",")
        except:
            pass
    
def main():
    sm = StudentManager()
    while True:
        print("1. Add Student\n2. View Student\n3. Exit")
        ch = input("Enter your choice: ")
        if ch == "1":
            name = input("Enter Name: ")
            Marks = int(input("Enter marks: "))
            sm.add_students(name , Marks)
        elif ch == "2":
            sm.view_students()
        elif ch == "3":
            print("existing.....")
            break
        else:
            print("Invalid choice")
main()