# https://submit.cs50.io/users/hbap-cag/cs50/labs/pdss/4/prices
import csv
import requests
import sys


if len(sys.argv) != 2:
    sys.exit("Usage: py quote.py SYMBOL")
symbol = sys.argv[1]

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=3E7O7UR9J03G6K1U&datatype=csv"

response = requests.get(url)

reader = csv.DictReader(response.text.splitlines())

row = next(reader)
dates = [row for row in reader]
for date in sorted(dates, key=lambda d: d["timestamp"], reverse=True):
    print(date["timestamp"] + " $" + date["close"])
