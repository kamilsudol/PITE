import sys
import logging as log
import json


def log_settings():
    console = log.getLogger()
    console.setLevel(log.NOTSET)
    file = log.FileHandler("students_dir.log")
    console.addHandler(file)


def save(data):
    log.info("Saving data.")
    file = open("students_dir.json", 'w')
    file.write(json.dumps(data))


def load():
    log.info("Loading data.")
    try:
        file = open("students_dir.json", 'r')
        return json.loads(file.read())
    except IOError:
        log.info("There's no such a file")
        return 0


def new_diary():
    log.info("Creating new students diary.")
    diary = {
        "Pite": {
            "supervisor": "John Kowalski",
            "students": []
        },
        "Computer graphics": {
            "supervisor": "Mike Wazowsky",
            "students": []
        },
        "Physics labs": {
            "supervisor": "Tony Hawk",
            "students": []
        },
        "Object oriented programming": {
            "supervisor": "Peter Łuszcz",
            "students": []
        },
        "Numerical methods": {
            "supervisor": "Kurt Cobain",
            "students": []
        }
    }
    save(diary)
    return diary


def new_student(name, attendance, grd):
    log.info("Adding new student: " + name)
    student = {
        "name": name,
        "attendance": attendance,
        "grades": []
    }
    add_grades(student, grd)
    return student


def add_grades(student, grd):
    log.info("Adding grades for student  " + student["name"])
    for x in grd:
        student["grades"].append(x)


def add_student_to_course(dict, course, student):
    course["students"].append(student)
    save(dict)


def compute_total_average(dict):
    result = 0
    j = 0
    for x in dict:
        result += compute_course_average(dict, x)
        j += 1
    if j == 0:
        return 0
    else:
        return result / j


def compute_student_average(student):
    result = sum(student["grades"]) / len(student["grades"])
    return result


def compute_course_average(dict, course):
    result = 0
    j = 0
    for x in dict[course]["students"]:
        result += compute_student_average(x)
        j += 1
    if j == 0:
        return 0
    else:
        return result / j


def print_supervisor(dict, course):
    log.info("Course: " + course + " Supervisor: " + dict[course]["supervisor"])


def print_students_info(dict):
    for x in dict:
        for i in dict[x]["students"]:
            log.info("Name: " + i["name"] + " Attendance: " + str(i["attendance"] / 300) + "% Average: " + str(
                compute_student_average(i)))


def print_courses(dict):
    log.info("All courses:")
    for x in dict:
        log.info(x)


def print_course_info(dict, course):
    print_supervisor(dict, course)
    log.info("Students: ")
    for x in dict[course]["students"]:
        log.info(x["name"])


def average_of_courses(dict):
    for x in dict:
        log.info("Course: " + x + " Average of course: " + str(compute_course_average(dict, x)))


def print_total_average(dict):
    log.info("Average of all courses: " + str(compute_total_average(dict)))


def print_student_info_filter(dict, course, stud_name):
    log.info("Looking for data.")
    stud = list(filter(lambda stud_in: stud_in["name"] == stud_name, dict[course]["students"]))
    for x in stud:
        log.info(x)


if __name__ == '__main__':
    log_settings()
    load()
    student_dict = new_diary()

    add_student_to_course(student_dict, student_dict["Pite"], new_student("Lilo", 276, [5, 5, 5, 3, 3, 3, 4, 5]))
    add_student_to_course(student_dict, student_dict["Pite"],
                          new_student("John", 300, [5, 5, 5, 3, 2, 2, 2, 4, 3, 3, 4, 5]))
    add_student_to_course(student_dict, student_dict["Pite"], new_student("Kamil", 151, [5, 5, 5, 3, 4, 3, 3, 4, 5]))
    add_student_to_course(student_dict, student_dict["Pite"], new_student("Adrian", 199, [5, 5, 3, 2, 4, 3, 3, 4, 5]))
    add_student_to_course(student_dict, student_dict["Computer graphics"],
                          new_student("Jacob", 211, [5, 5, 5, 3, 2, 4, 3, 3, 5]))
    add_student_to_course(student_dict, student_dict["Computer graphics"],
                          new_student("Peter", 270, [5, 5, 5, 3, 2, 4, 3, 3, 4, 4, 5]))
    add_student_to_course(student_dict, student_dict["Computer graphics"],
                          new_student("Patric", 280, [5, 5, 5, 3, 3, 4, 5]))
    add_student_to_course(student_dict, student_dict["Computer graphics"],
                          new_student("Julia", 256, [5, 5, 5, 2, 4, 3, 3, 4, 5]))
    add_student_to_course(student_dict, student_dict["Physics labs"],
                          new_student("Alex", 250, [5, 5, 5, 3, 2, 2, 2, 4, 3, 3, 4, 5]))
    add_student_to_course(student_dict, student_dict["Physics labs"],
                          new_student("Bobi", 233, [5, 5, 5, 3, 2, 3, 3, 4, 5]))
    add_student_to_course(student_dict, student_dict["Physics labs"],
                          new_student("Iris", 235, [5, 5, 5, 3, 5, 5, 3, 3, 4, 5]))
    add_student_to_course(student_dict, student_dict["Physics labs"],
                          new_student("Borys", 241, [5, 5, 5, 3, 2, 4, 3, 2, 4, 5]))
    add_student_to_course(student_dict, student_dict["Object oriented programming"],
                          new_student("John", 247, [2, 2, 5, 3, 2, 4, 3, 3, 4, 5]))
    add_student_to_course(student_dict, student_dict["Object oriented programming"],
                          new_student("Karol", 201, [5, 3, 4, 3, 2, 4, 3, 3, 4, 5]))
    add_student_to_course(student_dict, student_dict["Object oriented programming"],
                          new_student("Michael", 263, [5, 3, 3, 3, 2, 4, 3, 3, 4, 5]))
    add_student_to_course(student_dict, student_dict["Object oriented programming"],
                          new_student("Elliot", 261, [2, 5, 5, 3, 2, 4, 3, 3, 4, 5]))
    add_student_to_course(student_dict, student_dict["Numerical methods"],
                          new_student("Adam", 271, [5, 5, 5, 3, 2, 3, 3, 4, 5]))
    add_student_to_course(student_dict, student_dict["Numerical methods"],
                          new_student("Raphael", 232, [1, 5, 3, 2, 4, 3, 3, 4, 5]))
    add_student_to_course(student_dict, student_dict["Numerical methods"],
                          new_student("Mike", 266, [5, 5, 5, 3, 2, 4, 4, 4, 4, 5]))
    add_student_to_course(student_dict, student_dict["Numerical methods"],
                          new_student("Lily", 288, [5, 5, 5, 3, 3, 3, 4, 5]))

    # print(compute_total_average(student_dict))
    # print(compute_course_average(student_dict,"Numerical methods"))
    # print(compute_student_average(student_dict["Numerical methods"]["students"][1]))
    print_supervisor(student_dict, "Object oriented programming")
    print_students_info(student_dict)
    print_course_info(student_dict, "Physics labs")
    print_courses(student_dict)
    average_of_courses(student_dict)
    print_total_average(student_dict)
    print_student_info_filter(student_dict,"Pite","Lilo")
