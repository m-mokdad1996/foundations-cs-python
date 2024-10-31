class Course:
    def __init__(self, code, name, credit_hours, is_core):
        self.code = code
        self.name = name
        self.credit_hours = credit_hours
        self.is_core = is_core

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.courses = {}

    def enroll_course(self, course):
        if course.code in self.courses:
            print(f"Already enrolled in course: {course.code}")
        else:
            self.courses[course.code] = course
            print(f"Enrolled in course: {course.code}")

    def drop_course(self, course_code):
        if course_code in self.courses:
            del self.courses[course_code]
            print(f"Dropped course: {course_code}")
        else:
            print(f"Course {course_code} not found in enrollment")

    def list_courses(self):
        if not self.courses:
            print("No courses enrolled")
        else:
            for course in self.courses.values():
                print(f"{course.code}: {course.name}, {course.credit_hours} credits, Core: {course.is_core}")

class CourseCatalog:
    def __init__(self):
        self.courses = {}

    def add_course(self, course):
        self.courses[course.code] = course

    def get_course(self, course_code):
        return self.courses.get(course_code, None)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for course in self.courses.values():
                file.write(f"{course.code},{course.name},{course.credit_hours},{course.is_core}\n")

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                code, name, credit_hours, is_core = line.strip().split(',')
                self.courses[code] = Course(code, name, int(credit_hours), is_core == 'True')

students = []

def find_student_by_id(student_id):
    for student in students:
        if student.student_id == student_id:
            return student
    return None

def main():
    catalog = CourseCatalog()

    while True:
        print("\nMenu:")
        print("1. Add Course")
        print("2. Enroll Student in Course")
        print("3. Drop Course for Student")
        print("4. List Student Courses")
        print("5. Save Course Catalog")
        print("6. Load Course Catalog")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            code = input("Enter course code: ")
            name = input("Enter course name: ")
            credit_hours = int(input("Enter credit hours: "))
            is_core = input("Is it a core course? (yes/no): ").lower() == 'yes'
            catalog.add_course(Course(code, name, credit_hours, is_core))
            print("Course added successfully.")

        elif choice == "2":
            student_id = input("Enter student ID: ")
            student = find_student_by_id(student_id)
            if not student:
                student_name = input("Enter student name: ")
                student = Student(student_id, student_name)
                students.append(student)
            course_code = input("Enter course code: ")
            course = catalog.get_course(course_code)
            if course:
                student.enroll_course(course)
            else:
                print("Course not found")

        elif choice == "3":
            student_id = input("Enter student ID: ")
            student = find_student_by_id(student_id)
            if student:
                course_code = input("Enter course code: ")
                student.drop_course(course_code)
            else:
                print("Student not found")

        elif choice == "4":
            student_id = input("Enter student ID: ")
            student = find_student_by_id(student_id)
            if student:
                student.list_courses()
            else:
                print("Student not found")

        elif choice == "5":
            filename = input("Enter filename to save catalog: ")
            catalog.save_to_file(filename)
            print("Course catalog saved successfully.")

        elif choice == "6":
            filename = input("Enter filename to load catalog: ")
            catalog.load_from_file(filename)
            print("Course catalog loaded successfully.")

        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
