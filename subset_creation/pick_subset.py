import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    user='postgres',
    password='excel',
    dbname='mls_data'
)
cur = conn.cursor()

# Step 1: pull the random subset
cur.execute("SELECT mls FROM property ORDER BY RANDOM() LIMIT 200")
subset = [row[0] for row in cur.fetchall()]

print(f"Pulled {len(subset)} listings")

# Save to file for reuse
with open('subset_mls_list.txt', 'w') as f:
    for mls in subset:
        f.write(mls + '\n')

print("Saved to subset_mls_list.txt")

conn.close()
