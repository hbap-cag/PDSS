import csv
import sys

# Check for 2 inputs
if len(sys.argv) != 3:
    sys.exit("Usage: Python3 employees3.py SOURCE DEST")

# Read rows from SOURCE
rows = []
with open(sys.argv[1], "r", newline='') as file:

    # Initialize reader
    reader = csv.reader(file)

    # Read Header
    header = next(reader)

    # Insert into header EmployeeID
    header.insert(0, "EmployeeID")

    # Remember new Header
    rows.append(header)

    # Initialize EnployeeID
    id = 0

    # Iterate over rows
    for row in reader:
        id += 1

        # Add EmployeeID to row
        row.insert(0, id)

        # Remember new rows
        rows.append(row)

# Write rows to DEST
with open(sys.argv[2], "w", newline='') as file:
    writer = csv.writer(file)
    for row in rows:
        writer.writerow(row)

# Initialize some variables
rows2 = []
mid = 0

# Read rows from DEST
with open(sys.argv[2], "r", newline='') as file2:

    # Initialize reader
    reader = csv.reader(file2)

    # Read Header
    header = next(reader)

    # Delete Manager from Header
    # del header[0]
    del header[1]

    # Prepend ManagerId to header
    header.insert(1, "ManagerId")

    # Remember new Header
    # rows2.append(header2)
    print(header[0] + "," + header[1] + "," + header[2])

    # Iterate over rows
    for row in reader:
        # Split manager's name into first and last variables to check later
        try:
            first, last = row[1].split(" ")
        except:
            first, last = "", ""
        print(first + " " + last)
##############################################################################
        # Find ManagerID as mid
        for row in reader:
             print(row[1] + first + "/" + last)
            if row[1] == "":
                rows.insert(1, "")
                rows.append(row)
                print("1")
            elif row[1] == first + " " + last:
                mid = row[0]
                rows.insert(1, mid)
                rows.append(row)
                print("2")
            else:
                print("3")
