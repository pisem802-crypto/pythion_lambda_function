#filter
records = [
    {"id": 1, "name": "Alice", "status": "active"},
    {"id": 2, "name": "Bob", "status": "inactive"},
    {"id": 3, "name": "Charlie", "status": "active"}
]

Active_records=list(filter(lambda record:record["status"]=="active",records))
print(Active_records)