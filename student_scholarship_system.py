# Student Scholarship Eligibility System
# Topic: Conditional Statements (if, elif, else)

print("==============================================")
print("     STUDENT SCHOLARSHIP ELIGIBILITY SYSTEM")
print("==============================================")

# Step 1: Collect Student Information

student_name = input("Enter student name: ").strip()

# Step 2: Input Validation

if student_name == "":
    print("Invalid input! Student name cannot be empty.")

else:
    try:
        marks = float(input("Enter academic marks percentage: "))
        attendance = float(input("Enter attendance percentage: "))
        family_income = float(input("Enter monthly family income (Rs.): "))

        # Step 3: Validate Input Values

        if marks < 0 or marks > 100:
            print("Invalid marks! Enter percentage between 0 and 100.")

        elif attendance < 0 or attendance > 100:
            print("Invalid attendance! Enter percentage between 0 and 100.")

        elif family_income < 0:
            print("Invalid income! Income cannot be negative.")

        else:
            # Step 4: Check Scholarship Eligibility

            print("\n===== SCHOLARSHIP EVALUATION =====")

            print("Student Name:", student_name)
            print("Academic Marks:", marks, "%")
            print("Attendance:", attendance, "%")
            print("Monthly Family Income: Rs.", family_income)

            # Check all eligibility conditions

            if marks >= 80 and attendance >= 85 and family_income <= 50000:

                if marks >= 90:
                    scholarship = "Full Scholarship"

                elif marks >= 80:
                    scholarship = "Partial Scholarship"

                print("\nEligibility Status: Eligible")
                print("Scholarship Awarded:", scholarship)

            else:
                print("\nEligibility Status: Not Eligible")
                print("Reason for Ineligibility:")

                if marks < 80:
                    print("- Academic marks are below 80%.")

                if attendance < 85:
                    print("- Attendance is below 85%.")

                if family_income > 50000:
                    print("- Monthly family income exceeds Rs. 50,000.")

            print("\n==============================================")
            print("       SCHOLARSHIP EVALUATION COMPLETED")
            print("==============================================")

    except ValueError:
        print("Invalid input! Please enter numeric values for marks, attendance and income.")