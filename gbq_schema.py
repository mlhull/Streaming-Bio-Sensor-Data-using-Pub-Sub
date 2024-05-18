# Create schema.json to use to define target GBQ table
import json
schema = [
    {
        "name": "timestamp",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "measure",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "message",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "user_id",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]

schema_file = 'schema.json'
with open(schema_file, 'w') as file:
    json.dump(schema, file, indent=2)