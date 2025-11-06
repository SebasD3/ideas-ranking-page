import csv
import json

with open("ideas.csv", newline="") as f:
  reader = csv.DictReader(f)
  ideas = list(reader)

sorted_ideas = sorted(ideas, key=lambda x: int(x["votes"]), reverse=True)

for idea in sorted_ideas:
  print(f'{idea["title"]} - {idea["votes"]} votes')

with open("ideas.csv") as f:
  reader = csv.DictReader(f)
  ideas = list(reader)

with open("ideas.json", "w") as f:
  json.dump(ideas, f, indent=2)

print("Export complete!")
