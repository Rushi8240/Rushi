### problem : 1
#  i)
import requests
import sqlite3

API_URL = "https://fakerapi.it/api/v1/books?_quantity=5"

response = requests.get(API_URL)

if response.status_code == 200:
    data = response.json()
    books = data["data"]  
else:
    print("Failed :", response.status_code)
    books = []

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id int PRIMARY KEY ,
    title TEXT,
    author TEXT,
    year int
)
""")

for book in books:
    cursor.execute("""
        INSERT INTO books (title, author, year)
        VALUES (?, ?, ?)
    """, (book["title"], book["author"], book["published"]))

conn.commit()

cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()

print("\nBooks Stored in Database:")
for row in rows:
    print(row)

conn.close()

#  ii)

import requests
import matplotlib.pyplot as plt

API_URL = "https://jsonplaceholder.typicode.com/users"

response = requests.get(API_URL)
data = response.json()  

names = []
scores = []

for i in data[:5]:
    names.append(i["name"])
    scores.append(len(i["username"]) * 10)

average_score = sum(scores) / len(scores)
print("Average score:", average_score)

plt.bar(names, scores)
plt.axhline(average_score)
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Test Scores")
plt.show()


#  iii) 


import csv
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users")

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
""")


file = open("C:/Users/Rushirajsinh/Downloads/Book 1(Sheet1).csv", "r")
reader = csv.reader(file)
next(reader)

for row in reader:
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (row[0], row[1])
    )
conn.commit()
conn.close()
