import pymysql

# Database connection settings
endpoint = "localhost"
username = "root"
password = "admin"
database = "TenantGuard"

# Connect to the database
connection = pymysql.connect(
    host=endpoint,
    user=username,
    password=password,
    database=database
)

# Create a cursor object
cursor = connection.cursor()

# Execute a query
cursor.execute("SELECT VERSION()")

# Fetch one result
result = cursor.fetchone()
print("Database version:", result)

# Close the cursor and connection
cursor.close()
connection.close()
