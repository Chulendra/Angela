student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def mapper(value):
    if 91 <= value <= 100:
        return "Outstanding"
    elif 81 <= value <= 90:
        return "Exceeds Expectations"
    elif 71 <= value <= 80:
        return "Acceptable"
    else:
        return "Fail"

student_grades = {key: mapper(value) for key, value in student_scores.items()}