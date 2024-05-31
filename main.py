
import json

# Open the JSON file
with open("C:\\Users\\AKASH VISHWAKARMA\\Documents\\GitHub\\Moyas_chat\\data.json", "r") as f:
  # Load data from the opened file
  data = json.load(f)

print(data)
