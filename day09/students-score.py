student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
for key in student_scores:
    # if (student_scores[key] > 91) and (student_scores[key] < 100):
    #     student_grades[key] = "Outstanding"
    # elif (student_scores[key] > 81) and (student_scores[key] < 90):
    #     student_grades[key] = "Exceeds Expectations"
    # elif (student_scores[key] > 71) and (student_scores[key] < 80):
    #     student_grades[key] = "Acceptable"
    # elif (student_scores[key] <= 70):
    #     student_grades[key] = "Fail"
    student_score = student_scores[key]
    if student_score > 90:
        student_grades[key] = "Outstanding"
    elif student_score > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_score > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)
