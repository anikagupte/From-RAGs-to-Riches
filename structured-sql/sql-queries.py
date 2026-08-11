import psycopg2

conn = psycopg2.connect(host='localhost', port=5432, user='postgres',
                         password='excel', dbname='mls_data')
cur = conn.cursor()

queries = {}

# 1. 5-bedroom detached under $1.1M, built after 2005
queries['q01'] = ("SELECT mls FROM property WHERE beds >= %s AND type ILIKE %s AND list_price < %s AND year_built > %s",
                   [5, '%Detached%', 1100000, 2005])

# 2. Condo with 2 beds and 2 baths, at least 1,000 sq ft
queries['q02'] = ("SELECT mls FROM property WHERE is_condo = true AND beds = %s AND full_baths = %s AND rms_sqft >= %s",
                   [2, 2, 1000])

# 3. Any bungalows with a walkout basement under $650K?
queries['q03'] = ("SELECT mls FROM property WHERE arch_style ILIKE %s AND basement ILIKE %s AND list_price < %s",
                   ['%Bungalow%', '%Walk-Out%', 650000])

# 4. Two-storey house, 4 bathrooms minimum, budget $950,000
queries['q04'] = ("SELECT mls FROM property WHERE arch_style ILIKE %s AND full_baths >= %s AND list_price < %s",
                   ['%2 Storey%', 4, 950000])

# 5. Townhouses built in the last five years, 3 bedrooms
queries['q05'] = ("SELECT mls FROM property WHERE type ILIKE %s AND year_built >= %s AND beds = %s",
                   ['%Townhouse%', 2021, 3])

# 6. Show me homes with three fireplaces over 2,500 sq ft
queries['q06'] = ("SELECT mls FROM property WHERE fireplaces >= %s AND rms_sqft > %s",
                   [3, 2500])

# 7. 1-bath apartment under $300K, anything post-2015
queries['q07'] = ("SELECT mls FROM property WHERE is_condo = true AND full_baths = %s AND list_price < %s AND year_built > %s",
                   [1, 300000, 2015])

# 8. Character-style homes built before 1940 (Victorian dropped — not a known arch_style)
queries['q08'] = ("SELECT mls FROM property WHERE year_built < %s AND arch_style ILIKE %s",
                   [1940, '%Character%'])

# 9. Semi-detached with a finished basement, under $700,000
queries['q09'] = ("SELECT mls FROM property WHERE type ILIKE %s AND basement ILIKE %s AND list_price < %s",
                   ['%Semi Detached%', '%Finished%', 700000])

# 10. Modern-style detached, 4+ beds, priced below $850K
queries['q10'] = ("SELECT mls FROM property WHERE type ILIKE %s AND beds >= %s AND list_price < %s AND arch_style ILIKE %s",
                   ['%Detached%', 4, 850000, '%Modern%'])

# 11. Duplex with an unfinished basement, 3 bedrooms, around $600K
queries['q11'] = ("SELECT mls FROM property WHERE type ILIKE %s AND basement ILIKE %s AND beds = %s AND list_price BETWEEN %s AND %s",
                   ['%Duplex%', '%Unfinished%', 3, 540000, 660000])

# 12. Something over 3,000 sq ft with at least two fireplaces
queries['q12'] = ("SELECT mls FROM property WHERE rms_sqft > %s AND fireplaces >= %s",
                   [3000, 2])

# 13. Row house, 2 bed 1.5 bath, under $425,000
queries['q13'] = ("SELECT mls FROM property WHERE type ILIKE %s AND beds = %s AND full_baths = %s AND half_baths = %s AND list_price < %s",
                   ['%Row%', 2, 1, 1, 425000])

# 14. Bungalow with a legal basement suite (Craftsman dropped — not a known arch_style;
queries['q14'] = ("SELECT mls FROM property WHERE arch_style ILIKE %s AND basement ILIKE %s",
                   ['%Bungalow%', '%Finished%'])

# 15. New construction only, single-family, 4 bedrooms and up
queries['q15'] = ("SELECT mls FROM property WHERE type ILIKE %s AND beds >= %s AND year_built >= %s",
                   ['%Detached%', 4, 2024])

# 16. Condo under 650 sq ft, one bathroom, built after 2019
queries['q16'] = ("SELECT mls FROM property WHERE is_condo = true AND rms_sqft < %s AND full_baths = %s AND year_built > %s",
                   [650, 1, 2019])

# 17. Split-level home, 3 baths, budget between $700K and $800K
queries['q17'] = ("SELECT mls FROM property WHERE arch_style ILIKE %s AND full_baths = %s AND list_price BETWEEN %s AND %s",
                   ['%Split Level%', 3, 700000, 800000])

# 18. Detached house with a fireplace, at least 2,200 sq ft, under $900,000
queries['q18'] = ("SELECT mls FROM property WHERE type ILIKE %s AND fireplaces >= %s AND rms_sqft >= %s AND list_price < %s",
                   ['%Detached%', 1, 2200, 900000])

for qid, (sql, params) in queries.items():
    cur.execute(sql, params)
    results = [row[0] for row in cur.fetchall()]
    print(f"{qid}: {len(results)} matches")
    with open(f'ground_truth/{qid}.txt', 'w') as f:
        for mls in results:
            f.write(mls + '\n')

conn.close()
