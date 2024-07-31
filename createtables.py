import os
import pandas as pd
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Read environment variables
secure_connect_bundle_path = os.getenv('ASTRA_DB_SECURE_CONNECT_BUNDLE')
application_token = os.getenv('ASTRA_DB_TOKEN')

# Debug prints to check environment variables
print(f"Secure Connect Bundle Path: {secure_connect_bundle_path}")
print(f"Application Token: {application_token}")

# Check if the environment variables are loaded correctly
if not secure_connect_bundle_path or not os.path.exists(secure_connect_bundle_path):
    raise FileNotFoundError(f"Secure connect bundle not found at path: {secure_connect_bundle_path}")

if not application_token:
    raise ValueError("Application token not found in environment variables")

# Connect to the Cassandra database using the secure connect bundle
session = Cluster(
    cloud={"secure_connect_bundle": secure_connect_bundle_path},
    auth_provider=PlainTextAuthProvider("token", application_token),
).connect()


# Use the keyspace
session.set_keyspace('ecommerce')

# Create a table
session.execute("CREATE TABLE IF NOT EXISTS test3 (id int PRIMARY KEY, name text, age int);")

# Insert data
session.execute("INSERT INTO test3 (id, name, age) VALUES (1, 'Alice', 30);")

# Select data
results = session.execute("SELECT * FROM test3 WHERE id = 1;")
for row in results:
    print(row)

# df = pd.read_sql_query(results, session)
# print(df)



# Delete data
session.execute("DELETE FROM test WHERE id = 1;")