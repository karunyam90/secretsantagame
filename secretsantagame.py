import csv
import random
from pathlib import Path
import unittest
from unittest.mock import mock_open, patch

class Employee:
    def __init__(self,employee_name,employee_email):
        self.employee_name = employee_name
        self.employee_email = employee_email
 
    
class Secretsanta:
    def __init__(self,employeecsv,previouscsv):
        self.employees =[]
        self.newassignments =[]
        self.prevloademployees = {}
        self.employeecsv = employeecsv
        self.previouscsv = previouscsv
    #################################
    def __str__(self):
        return f"{self.employees[{self.employee_name},{self.employee_email}]}"
    # function to load the csv and parse them
    def load_csv(self):
        with open(self.employeecsv, mode='r') as file:
            reader = csv.DictReader(file,delimiter='\t')
            for row in reader:
                self.employees.append(Employee(row['Employee_name'],row['Employee_email']))
                
    #loading previous year csv
    def load_prev_csv(self):
        with open(self.previouscsv, mode='r') as file:
            reader = csv.DictReader(file,delimiter='\t')
            for row in reader:
                employee_name = row['employee_name']  # Extract employ
                child_name = row['child_name']  # Extract child name
                self.prevloademployees[employee_name] = child_name
            print(self.prevloademployees)
    #Assigning secret santa
    def assign_secret_santa(self):
        assignments = self.employees[:]
        for employee in self.employees:
            potential_canditates = [ e for e in assignments if e.employee_name != employee.employee_name and 
                                    e.employee_name != self.prevloademployees.get(employee.employee_name,None) ]
            if not potential_canditates:
                raise ValueError('Error rasied because of no valuable candidates')
            secret_child = random.choice(potential_canditates)
            assignments.remove(secret_child)

            self.newassignments.append({
                'employee_name':employee.employee_name,
                'employee_emailid':employee.employee_email,
                'secret_child_name':secret_child.employee_name,
                'secret_child_email':secret_child.employee_email
            })
    #write the assignment into a csv
    def writeintocsv(self):
        with open('output.csv',mode='w',newline='')as file:
            fieldnames = self.newassignments[0].keys()
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.newassignments)


#calling the class for the root directory
script_dir = Path(__file__).parent

# Construct the full path to the CSV file
csv_file_path = script_dir / "Employee_details.csv"
last_csv_file_path = script_dir / "Last_year_employee.csv"
# print(file_path)
secretsanta = Secretsanta(csv_file_path,last_csv_file_path)
secretsanta.load_csv()
secretsanta.load_prev_csv()
secretsanta.assign_secret_santa()
secretsanta.writeintocsv()


class TestSecretSanta(unittest.TestCase):
    
    def setUp(self):
        self.mock_employee_csv = "Employee_name\tEmployee_email\nJohn Doe\tjohn@example.com\nJane Doe\tjane@example.com\n"
        self.mock_previous_csv = "employee_name\tchild_name\nJohn Doe\tJane Doe\n"
    
    @patch("builtins.open", new_callable=mock_open, read_data="Employee_name\tEmployee_email\nJohn Doe\tjohn@example.com\nJane Doe\tjane@example.com\n")
    def test_load_csv(self, mock_file):
        secret_santa = Secretsanta("mock_employees.csv", "mock_previous.csv")
        secret_santa.load_csv()
        self.assertEqual(len(secret_santa.employees), 2)
        self.assertEqual(secret_santa.employees[0].employee_name, "John Doe")
        self.assertEqual(secret_santa.employees[0].employee_email, "john@example.com")
    
    @patch("builtins.open", new_callable=mock_open, read_data="employee_name\tchild_name\nJohn Doe\tJane Doe\n")
    def test_load_prev_csv(self, mock_file):
        secret_santa = Secretsanta("mock_employees.csv", "mock_previous.csv")
        secret_santa.load_prev_csv()
        self.assertEqual(secret_santa.prevloademployees["John Doe"], "Jane Doe")
        

    def test_assign_secret_santa(self):
        santa = Secretsanta("mock_employees.csv", "mock_previous.csv")
        santa.employees = [Employee("Alice", "alice@example.com"), Employee("Bob", "bob@example.com")]
        santa.previous_assignments = {}
        santa.assign_secret_santa()
        self.assertEqual(len(santa.newassignments), 2)
        
if __name__ == "__main__":
    unittest.main()
