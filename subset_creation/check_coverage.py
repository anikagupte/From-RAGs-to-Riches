import psycopg2

with open('subset_mls_list.txt') as f:
    subset = [line.strip() for line in f]

conn = psycopg2.connect(
    host='localhost', port=5432, user='postgres',
    password='excel', dbname='mls_data'
)
cur = conn.cursor()
placeholders = ','.join(['%s'] * len(subset))

print("=== TYPE + BEDROOMS ===")
type_bed_combinations = [
    ("Semi Detached", 3, "%Semi Detached%"),
    ("Semi Detached", 4, "%Semi Detached%"),
    ("Detached", 3, "%Detached%"),
    ("Detached", 4, "%Detached%"),
    ("Detached", 5, "%Detached%"),
    ("Apartment", 1, "%Apartment%"),
    ("Apartment", 2, "%Apartment%"),
    ("Row/Townhouse", 2, "%Townhouse%"),
    ("Row/Townhouse", 3, "%Townhouse%"),
]

for label_type, beds, type_pattern in type_bed_combinations:
    cur.execute(
        f"SELECT COUNT(*) FROM property WHERE mls IN ({placeholders}) AND type ILIKE %s AND beds = %s",
        subset + [type_pattern, beds]
    )
    count = cur.fetchone()[0]
    flag = "  <-- LOW, needs topping up" if count < 3 else ""
    print(f"{label_type}, {beds}-bed: {count}{flag}")

print("\n=== PRICE BANDS ===")
price_bands = [
    (0, 500000, "under $500k"),
    (500000, 750000, "$500k-$750k"),
    (750000, 1000000, "$750k-$1M"),
    (1000000, 999999999, "over $1M"),
]

for low, high, label in price_bands:
    cur.execute(
        f"SELECT COUNT(*) FROM property WHERE mls IN ({placeholders}) AND list_price >= %s AND list_price < %s",
        subset + [low, high]
    )
    count = cur.fetchone()[0]
    flag = "  <-- LOW, needs topping up" if count < 3 else ""
    print(f"{label}: {count}{flag}")

print("\n=== YEAR BUILT ===")
year_bands = [
    (0, 2000, "before 2000"),
    (2000, 2010, "2000-2010"),
    (2010, 2020, "2010-2020"),
    (2020, 2100, "after 2020"),
]

for low, high, label in year_bands:
    cur.execute(
        f"SELECT COUNT(*) FROM property WHERE mls IN ({placeholders}) AND year_built >= %s AND year_built < %s",
        subset + [low, high]
    )
    count = cur.fetchone()[0]
    flag = "  <-- LOW, needs topping up" if count < 3 else ""
    print(f"{label}: {count}{flag}")
