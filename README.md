**Python Programming Assessment – Conditions & Loops**

**Project Overview**

This repository contains two Python applications developed as part of the Python Programming Assessment. The projects demonstrate conditional statements, loops, input validation, counters, accumulators, and basic problem-solving through real-world business scenarios.

**Repository Information**

Repository Name: "python-conditions-loops-assessment"

**Programming Language:** Python 3

**Task 1: Student Scholarship Eligibility System**

**Description**

This application evaluates students' eligibility for university scholarships based on academic marks, attendance percentage, and monthly family income.

**Eligibility Criteria**

- Academic marks must be at least 80%.
- Attendance must be at least 85%.
- Monthly family income must be Rs. 50,000 or less.

**Scholarship Categories**

- Full Scholarship: Academic marks of 90% or above, provided all eligibility conditions are satisfied.
- Partial Scholarship: Academic marks between 80% and 89%, provided all eligibility conditions are satisfied.
- Not Eligible: If any eligibility condition is not satisfied, the program displays the reasons.

**Program Features**

- Collects student name, marks, attendance, and family income.
- Validates empty names and invalid numeric inputs.
- Checks marks and attendance percentages.
- Validates monthly family income.
- Determines scholarship eligibility.
- Displays appropriate ineligibility reasons.
- Generates a complete scholarship evaluation report.

**Python Concepts Used**

- input() and print()
- Variables and data types
- float() conversion
- if, elif, and else
- Logical operators (and, or)
- Nested conditional statements
- try and except
- Input validation

**Task 2: Smart Pharmacy Inventory & Sales Management System**

**Description**

This application manages medicine inventory and calculates daily pharmacy sales revenue. It processes multiple medicines using loops and calculates the remaining stock after each sale.

**Program Features**

- Accepts the number of medicines to process.
- Collects medicine name, available stock, price, and quantity sold.
- Uses a for loop to process each medicine.
- Checks whether the requested sales quantity is available.
- Rejects negative and invalid inputs.
- Calculates sales amount for each medicine.
- Calculates remaining stock after every sale.
- Displays a low-stock warning when remaining stock is below 10 units.
- Maintains total pharmacy revenue using an accumulator.
- Counts medicines requiring restocking.
- Generates a final pharmacy sales report.

**Python Concepts Used**

- input() and print()
- Variables and data types
- int() and float() conversion
- for loop
- range() function
- while loop for input validation
- if and else conditions
- try and except
- Arithmetic operators
- Accumulators
- Counters

**Project Structure**

python-conditions-loops-assessment/
│
├── student_scholarship_system.py
├── pharmacy_inventory_system.py
└── README.md

**How to Run the Programs**

**Requirements**

- Python 3 installed.
- Visual Studio Code or another Python code editor.

**Run Task 1: Scholarship System**

Open the project folder in VS Code and execute:

python student_scholarship_system.py

Enter the student's name, academic marks, attendance percentage, and monthly family income.

**Run Task 2: Pharmacy Inventory System**

**Execute:**

python pharmacy_inventory_system.py

Enter the number of medicines and provide the required details for each medicine.

Sample Execution Details

**Task 1: Scholarship System**

**Sample Input:**

Student Name: Ali
Academic Marks: 95
Attendance: 90
Monthly Family Income: 40000

**Expected Result:**

Eligibility Status: Eligible
Scholarship Awarded: Full Scholarship

**Task 2: Pharmacy Inventory System**

**Sample Input:**

Number of Medicines: 3

Medicine 1:
Name: Panadol
Stock: 50
Price: 20
Quantity Sold: 10

Medicine 2:
Name: Disprin
Stock: 15
Price: 10
Quantity Sold: 8

Medicine 3:
Name: Syrup
Stock: 5
Price: 100
Quantity Sold: 2

**Expected Final Report:**

Total Medicines Processed: 3
Total Pharmacy Revenue: Rs. 480
Medicines Requiring Restocking: 2

**Testing**

Both applications were tested with multiple input scenarios, including:

- Valid and invalid numeric inputs.
- Full and partial scholarship eligibility.
- Ineligible scholarship cases.
- Negative stock validation.
- Insufficient stock validation.
- Low-stock warning.
- Revenue and restocking calculations.

**Learning Outcomes**

After completing these projects, the student can:

- Apply conditional statements to real-world problems.
- Use loops to process multiple records.
- Validate user input.
- Perform arithmetic calculations.
- Use counters and accumulators.
- Generate meaningful reports.
- Organize and document Python projects using GitHub.

**Author**

Python Programming Assessment – Conditions & Loops

**Status: Completed**
