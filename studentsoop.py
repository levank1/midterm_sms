import json
import os

class Student:

    def __init__(self,name: str, student_number: int, grade):
        self.name = name
        self.student_number = student_number
        self.grade = grade

    def __str__(self):
        return f'Name: {self.name}, Student Number: {self.student_number}, Grade: {self.grade}'




class StudentManagementSystem:

    def __init__(self):
        self.students = []
        self.import_data_from_json()




    def import_data_from_json(self):
        if os.path.exists("students.json"):
            with open('students.json') as json_file:
                data = json.load(json_file)
                for student in data:
                    self.students.append(Student(student['name'], student['student_number'], student['grade']))




    def save_data_in_json(self):
        def costum_serializer(obj):
            if isinstance(obj, Student):
                return {'name': obj.name, 'student_number': obj.student_number, 'grade': obj.grade}
            raise TypeError("invalid object type")

        with open("students.json", "w") as json_file:
            json.dump(self.students, json_file, default=costum_serializer, indent=4)




    def add_student(self, name: str, student_number: int, grade):
        if not any(student_number == student.student_number for student in self.students):
            self.students.append(Student(name, student_number, grade))
            self.save_data_in_json()

            print("Student added successfully.")
        else:
            print("Student with the same number already exists")




    def renew_grade_of_student(self,student_number: int, grade):
        if any(student_number == student.student_number for student in self.students):
            for student in self.students:
                if student.student_number == student_number:
                    student.grade = grade
                    self.save_data_in_json()
        else:
            print("there is no student with the same number")


    def delete_student(self, student_number):
        if any(student_number == student.student_number for student in self.students):
            for i in range(0, len(self.students)):
                if self.students[i].student_number == student_number:
                    self.students.pop(i)
                    self.save_data_in_json()
                    print("Student deleted successfully.")

        else:
            print("there is no student with the same number")



    def menu(self):
      while True:
       print("\n1: Add a new Student")
       print("2: View all students")
       print("3: Search student by her student number")
       print("4: Renew the grade of student")
       print("5: Delete Student by her student number")
       print("6: Exit\n")
       choice = input("Enter your choice: ")


       if choice == "1":
         name = input("Enter student name: ")
         student_number = input("Enter student number: ")
         grade = input("Enter student grade: ")
         if student_number.isdigit():
             self.add_student(name, int(student_number), grade)

         else:
             print("Invalid input.")



       elif choice == "2":
           if len(self.students) > 0:
                for student in self.students:
                    print(student)
           else:
                print("No students available.")


       elif choice == "3":
           s_number = int(input("Enter student number: "))
           if any(s_number == student.student_number for student in self.students):
              for student in self.students:
                  if student.student_number == s_number:
                      print(student)
           else:
               print("there is no stundet with the same stundet number")

       elif choice == "4":
           s_number = int(input("Enter student number: "))
           new_grade = input("Enter new grade: ")
           self.renew_grade_of_student(s_number, new_grade)


       elif choice == "5":
           s_number = int(input("Enter student number: "))
           self.delete_student(s_number)


       elif choice == "6":
         print("You logged out from the student management system. Thank you!")
         break





if __name__ == "__main__":
    s_management = StudentManagementSystem()
    s_management.menu()