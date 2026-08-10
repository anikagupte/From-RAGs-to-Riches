import psycopg2

conn = psycopg2.connect(
    host='localhost', port=5432, user='postgres',
    password='excel', dbname='mls_data'
)
cur = conn.cursor()

cur.execute("SELECT DISTINCT type FROM property ORDER BY type")
print("Distinct 'type' values:")
for row in cur.fetchall():
    print(" ", row[0])

conn.close()
