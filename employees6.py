import numpy as np
import pandas as pd
import sys


from datetime import datetime

# Check for filename
if len(sys.argv) != 2:
    sys.exit("Usage: py employees6.py FILE")

# Import employees
df = pd.read_csv(sys.argv[1])

# Get today's date
now = datetime.now()

# Convert birthdate to ages
ages = []
for birthdate in df.loc[:, "BirthDate"]:
    age = now - datetime.strptime(birthdate, "%Y-%m-%d %H:%M:%S")
    ages.append(age.days // 365)

# Print average age
print(int(np.round(np.mean(ages))))
