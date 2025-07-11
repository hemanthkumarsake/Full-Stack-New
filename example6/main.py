if __name__ == '__main__':
    from grade_utils import calculate_average, get_grade, validate_marks
    student_name = input("Enter student name: ")
    raw_marks = input("Enter marks separated by space: ")
    try:
        marks = [float(m) for m in raw_marks.split()]
    except ValueError:
        print("Invalid input. Please enter numbers only, separated by spaces.")
        exit(1)
    if not validate_marks(marks):
        print("Error: All marks must be between 0 and 100.")
        exit(1)
    avg = calculate_average(marks)
    grade = get_grade(avg)
    print(f"\nStudent: {student_name}")
    print(f"Marks: {marks}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")