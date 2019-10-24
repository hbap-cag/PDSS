import csv
import sys


if len(sys.argv) != 2:
    sys.exit("Usage: Python3 employees.py FILE")

with open(sys.argv[1], "r") as file:
    reader = csv.DictReader(file)
    employees = [row for row in reader]

# print("Id, ManagerId, LastName, FirstName")
id = 0
employees2 = {}

for employee in employees:
    id += 1
    employees2 .update({"Id": id, "Manager": employee["Manager"], "LastName": employee["LastName"], "FirstName": employee["FirstName"]})
print(employees)
