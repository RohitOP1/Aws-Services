import psycopg2

try:
    conn = psycopg2.connect(
        host="database-1.cwjeeqkectah.us-east-1.rds.amazonaws.com",
        database="Testdb",
        user="postgres",
        password="Yoyorohit"
    )
    print(" Connected to database!")
    conn.close()

except Exception as e:
    print(" An error occurred while connecting to the database:", e)
