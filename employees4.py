import csv
import sys


def birthdate(e):
    return e["BirthDate"]


if len(sys.argv) != 2:
    sys.exit("Usage: Python3 employees4.py FILE")

with open(sys.argv[1], "r") as file:
    reader = csv.DictReader(file)
    employees = [row for row in reader]

for employee in sorted(employees, key=birthdate):
    print(employee["FirstName"], employee["LastName"], employee["BirthDate"])
