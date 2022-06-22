import json

database = {
    "computer_name": "Sharp MZ-700",
    "CPU": "Z80",
    "Speed": 3.4,
    "Year": 1980
}

print(json.dumps(database, indent=12))
