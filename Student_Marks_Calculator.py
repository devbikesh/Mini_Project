marks = []

for subject_number in range(1, 6):
    mark = int(input(f"Enter marks for subject {subject_number}: "))
    marks.append(mark)


def calculate_total(marks):
    total_marks = sum(marks)
    print("Total Marks:", total_marks)


def calculate_average(marks):
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    print("Average Marks:", average_marks)


def calculate_grade(marks):
    total_marks = sum(marks)
    maximum_marks = len(marks) * 100
    percentage = (total_marks / maximum_marks) * 100

    print("Percentage:", percentage, "%")

    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 80:
        print("Grade: B")
    elif percentage >= 70:
        print("Grade: C")
    elif percentage >= 60:
        print("Grade: D")
    else:
        print("Grade: F")


calculate_total(marks)
calculate_average(marks)
calculate_grade(marks)