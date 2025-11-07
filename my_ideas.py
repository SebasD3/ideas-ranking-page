import csv

title = input("Enter your idea: ")

with open("ideas.txt", "a") as f:
  f.write(title + "\n")

with open("ideas.txt", "r") as f:
  print(f.read())

ideas =[
  {
    "id": "1",
    "title": "Cafeteria screens",
    "author": "Alice",
    "votes": "30"
  },
  {
    "id": "2",
    "title": "School event tracker",
    "author": "Bob",
    "votes": "20"
  },
  {
    "id": "3",
    "title": "Digital suggestion box",
    "author": "Charlie",
    "votes": "40"
  },
  {
    "id": "4",
    "title": "Digital boards instead of whiteboards",
    "author": "Dylan",
    "votes": "29"
  },
  {
    "id": "5",
    "title": "Digital Attendance System",
    "author": "Sebas",
    "votes": "26"
  },
  {
    "id": "6",
    "title": "Automatic sprinklers",
    "author": "Lana",
    "votes": "8"
  },
  {
    "id": "7",
    "title": "Dismissal screens",
    "author": "Pablo",
    "votes": "72"
  },
]

with open("ideas.csv", "w", newline="") as f:
  writer = csv.DictWriter(f, fieldnames=["id", "title", "author", "votes"])
  writer.writeheader()
  writer.writerows(ideas)
