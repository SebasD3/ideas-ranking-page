import csv

title = input("Enter your idea: ")

with open("ideas.txt", "a") as f:
  f.write(title + "\n")

with open("ideas.txt", "r") as f:
  print(f.read())

ideas = [{
    "id": 1,
    "title": "Solar-Powered Charger",
    "author": "Alice",
    "votes": 0
}, {
    "id": 2,
    "title": "Homework Helper App",
    "author": "Bob",
    "votes": 0
}, {
    "id": 3,
    "title": "Smart Mirror",
    "author": "Charlie",
    "votes": 0
}]

with open("ideas.csv", "w", newline="") as f:
  writer = csv.DictWriter(f, fieldnames=["id", "title", "author", "votes"])
  writer.writeheader()
  writer.writerows(ideas)
