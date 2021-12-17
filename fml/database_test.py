from __future__ import annotations

import os
import csv
import atexit
import sqlite3

import urllib.request

from socket import gethostname

def cleanup() -> None:
    con.close()
atexit.register(cleanup)

con = sqlite3.connect("C:\\Users\\agent\\OneDrive\\Documents\\databázy\\weather.db" if gethostname()=="DESKTOP-RKOSLVI" else input("Database path? > "))

def select_operation() -> None:
    operation = int(input("1) Fetch data\n2) Display data\n> "))
    if operation == 1:
        fetch_data()
    else:
        display_data()

def fetch_data() -> None:
    date = input("Date? (DD.MM.YYYY) > ")
    urllib.request.urlretrieve(f"http://meteo.shmu.sk/customer/home/opendata/?observations;date={date}:00","temp.csv")
    csv_file = open("temp.csv","r")
    loaded_csv = csv.DictReader(csv_file, delimiter = ";")
    cur = con.cursor()
    for row in loaded_csv:
        row = {k.strip(): v.strip() for k, v in row.items()}
        cur.execute(f"INSERT INTO weather (name, ta_2m, date) VALUES (\"{row['name']}\", \"{row['ta_2m']}\", \"{row['date'].split('T')[0]}\")")
    con.commit()
    csv_file.close()
    os.remove("temp.csv")
    return select_operation()

def display_data() -> None:
    date = input("Date? (YYYY-MM-DD) > ")
    city = input("City? > ")
    cur = con.cursor()
    cur.execute(f"SELECT name, ta_2m, date FROM weather WHERE name LIKE \"{city}%\" AND date LIKE \"{date}%\"")
    for row in cur.fetchall():
        print(f"City: {row[0]}; Temperature: {row[1]}°C")

select_operation()
