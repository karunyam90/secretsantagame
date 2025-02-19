Secret Santa Assignment

Overview

This project implements a Secret Santa assignment system in Python. It reads employee details from a CSV file, assigns each employee a Secret Santa (without repeating last year’s pairings), and writes the assignments to an output CSV file.

Features

Reads employee details from a CSV file.

Ensures no employee is assigned themselves.

Avoids assigning the same pair as the previous year.

Writes the new assignments to an output CSV file.

Includes unit tests to validate functionality.

Installation & Requirements

Prerequisites

Ensure you have Python installed (>=3.6).

Install Dependencies

No external dependencies are required apart from Python’s standard library.

How to Use

Place your employee details in Employee_details.csv.

Place last year's Secret Santa assignments in Last_year_employee.csv.

Run the script:

python secretsantagame.py

The new assignments will be saved in output.csv.

File Structure

.
├── secretsanta.py  # Main script
├── Employee_details.csv  # Employee details input file
├── Last_year_employee.csv  # Last year’s assignments
├── output.csv  # Output file with new assignments
├── test_secretsanta.py  # Unit tests
└── README.md  # Project documentation

CSV File Formats

Employee Details (Employee_details.csv)

Employee_name	Employee_email
John Doe	john@example.com
Jane Doe	jane@example.com

Last Year’s Assignments (Last_year_employee.csv)

employee_name	child_name
John Doe	Jane Doe

Output File (output.csv)

employee_name	employee_emailid	secret_child_name	secret_child_email
John Doe	john@example.com	Alice	alice@example.com

Running Unit Tests

To run the unit tests, use:
 python -m unittest secretsantagame.py
