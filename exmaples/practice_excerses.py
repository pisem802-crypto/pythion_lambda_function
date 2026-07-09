#ETL Scenario with lambda function
records = [
    {"name": "John", "salary": 50000},
    {"name": "Alice", "salary": 60000},
    {"name": "Bob", "salary": 45000}
]

updated = list(
    map(
        lambda r: {
            **r,
            "bonus": r["salary"] * 0.10
        },
        records
    )
)





#tranformation phase