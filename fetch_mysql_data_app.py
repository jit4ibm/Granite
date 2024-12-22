# Assisted by watsonx Code Assistant 
import mysql.connector

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  password="test",
  database="test_db"
)

# Create a cursor object using the cursor() method
mycursor = mydb.cursor()

# Execute a SQL query to retrieve data from a table
mycursor.execute("SELECT * FROM yourtable")

# Fetch all the rows returned by the query
rows = mycursor.fetchall()

# Print the retrieved data
for row in rows:
  print(row)

# Close the cursor and database connection
mycursor.close()
mydb.close()
