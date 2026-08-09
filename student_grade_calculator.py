import csv
import os

# Configuration Constants
PASSING_SCORE = 50
GRADE_SCALE = {
    'A': 90,
    'B': 80,
    'C': 70,
    'D': 60,
    'F': 0
}

def calculate_letter_grade(average):
    """Maps a numerical average to a letter grade based on scale."""
    for grade, threshold in GRADE_SCALE.items():
        if average >= threshold:
            return grade
    return 'F'

def process_student_grades(file_path):
    """Reads student data, computes metrics, and generates a report."""
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        return

    print("\n" + "="*60)
    print("      STUDENT GRADE CALCULATOR & ACADEMIC REPORT")
    print("="*60)
    print(f"{'Student Name':<15} | {'Average':<7} | {'Grade':<5} | {'Status':<6}")
    print("-"*60)

    total_class_average = 0
    student_count = 0
    highest_avg = 0
    top_student = ""

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            name = row['Student_Name']
            
            # Extract scores and convert them to integers dynamically
            try:
                scores = [int(row[subject]) for subject in reader.fieldnames if subject != 'Student_Name']
            except ValueError:
                print(f"Skipping row for {name} due to invalid score formatting.")
                continue

            # Calculate metrics
            average = sum(scores) / len(scores) if scores else 0
            letter_grade = calculate_letter_grade(average)
            status = "PASS" if average >= PASSING_SCORE else "FAIL"
            
            # Update class aggregates
            total_class_average += average
            student_count += 1
            
            if average > highest_avg:
                highest_avg = average
                top_student = name

            # Print individual row
            print(f"{name:<15} | {average:<7.2f} | {letter_grade:<5} | {status:<6}")

    # Print summary metrics
    if student_count > 0:
        class_final_avg = total_class_average / student_count
        print("="*60)
        print(f"Total Students Processed : {student_count}")
        print(f"Class Overall Average    : {class_final_avg:.2f}%")
        print(f"Top Performing Student  : {top_student} ({highest_avg:.2f}%)")
        print("="*60 + "\n")
    else:
        print("No student records were successfully processed.")

if __name__ == "__main__":
    # Target file path
    csv_filename = "grades.csv"
    process_student_grades(csv_filename)
