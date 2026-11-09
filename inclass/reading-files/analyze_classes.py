def convert_grade(grade):    
    if grade == "A":
        return 4.0
    elif grade == "A-":
        return 3.7
    elif grade == "B+":
        return 3.3
    elif grade == "B":
        return 3.0
    elif grade == "B-":
        return 2.7
    elif grade == "C+":
        return 2.3
    elif grade == "C":
        return 2.0
    elif grade == "C-":
        return 1.7
    elif grade == "D+":
        return 1.3 
    elif grade == "D":
        return 1.0
    elif grade == "D-":
        return 0.7
    else:
        return 0.0

def read_csv(filename):
    contents = []
    # TODO Implement together
    return contents

def get_students_by_course(courses, course_id):
    students = []
    for course in courses:
        if course[3] == course_id:
            students.append(course)
    return students

def get_student_by_name(courses, name):
    for course in courses:
        if course[1] + " " + course[2] == name:
            return course 
    return None

def format_student(student):
    id, first_name, last_name, course, grade = student 
    return f"[{id}]: {first_name} {last_name}, {course}: {grade}"

def find_available_courses(courses):
    available_courses = []
    for course in courses:
        if course[3] not in available_courses:
           available_courses.append(course[3]) 
    return available_courses

def get_course_performance_average(courses, course_name):
    course_performance = []
    total = 0.0
    # TODO  Implement me
    return total

def get_all_course_averages(courses, available_courses):
    course_averages = {}
    # TODO  Implement me
    return course_averages

def find_best_course_average(course_averages):
    best_course = {"name": "", "score": 0.0}
    for course, average in course_averages.items():
        if average > best_course["score"]:
            best_course["score"] = average 
            best_course["name"] = course
    return best_course

    
def main():
    courses = read_csv("classes.csv")
    course_averages = get_all_course_averages(courses, find_available_courses(courses))
    print(find_best_course_average(course_averages))

if __name__ == "__main__":
    main()
