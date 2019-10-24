import csv
import requests
import sys
import os
from dotenv import load_dotenv
load_dotenv()


if len(sys.argv) != 2:
    sys.exit("Usage: py quote.py SYMBOL")
symbol = sys.argv[1]
API_KEY = os.getenv('API_KEY')
if not API_KEY:
    sys.exit("Missing API_KEY")
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}&datatype=csv"
response = requests.get(url)

reader = csv.DictReader(response.text.splitlines())

row = next(reader)
print(f"${row['close']}")
