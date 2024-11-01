student_scores = {
    "Argishti": 81,
    "Maldini": 78,
    "Baresi": 99,
    "Baggio": 74,
    "Olmo": 62
}

student_grades = {}

for student, score in student_scores.items():
    if 91 <= score <= 100:
        student_grades[student] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
        

print(student_grades.items())

