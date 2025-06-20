subject = input("Enter the subject: ")
max_marks = int(input("Enter the maximum marks: "))
marks_obtained = int(input("Enter the marks obtained: "))

if marks_obtained < 0 or max_marks > 100:
    print("Invalid input! Maximum marks should be between 0 and 100.")
elif 90 <= marks_obtained <= 100:
    print("Grade: A")
    print("Remarks: Excellent")
elif 80 <= marks_obtained < 90:
    print("Grade: B")
    print("Remarks: Good")
elif 70 <= marks_obtained < 80:
    print("Grade: C")
    print("Remarks: Fair")
elif 60 <= marks_obtained < 70:
    print("Grade: D")
    print("Remarks: Needs Improvement")
elif 50 <= marks_obtained < 60:
    print("Grade: E")
    print("Remarks: Poor")
else:
    print("Grade: F")
    print("Remarks: Fail")

print("Percentage: ", (marks_obtained / max_marks) * 100)