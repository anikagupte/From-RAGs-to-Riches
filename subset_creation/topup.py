import psycopg2

with open('subset_mls_list.txt') as f:
    subset = set(line.strip() for line in f)

conn = psycopg2.connect(
    host='localhost', port=5432, user='postgres',
    password='excel', dbname='mls_data'
)
cur = conn.cursor()

# Pull extra 4-bed semi-detached listings not already in the subset
placeholders = ','.join(['%s'] * len(subset)) if subset else "''"
cur.execute(
    f"SELECT mls FROM property WHERE type ILIKE %s AND beds = %s AND mls NOT IN ({placeholders}) LIMIT 5",
    ['%Semi Detached%', 4] + list(subset)
)
extra = [row[0] for row in cur.fetchall()]
print(f"Found {len(extra)} extra listings to add:", extra)

subset.update(extra)
with open('subset_mls_list.txt', 'w') as f:
    for mls in subset:
        f.write(mls + '\n')

print(f"Subset now has {len(subset)} listings")
conn.close()
