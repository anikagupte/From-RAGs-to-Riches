import psycopg2

conn = psycopg2.connect(host='localhost', port=5432, user='postgres',
                         password='excel', dbname='mls_data')
cur = conn.cursor()

queries = {}

queries['q01'] = ("SELECT mls FROM property WHERE beds >= %s AND type ILIKE %s AND list_price < %s AND year_built > %s",
                   [5, '%Detached%', 1100000, 2005])

queries['q02'] = ("SELECT mls FROM property WHERE is_condo = %s AND beds = %s AND full_baths = %s AND rms_sqft >= %s",
                   ['Y', 2, 2, 1000])

queries['q03'] = ("SELECT mls FROM property WHERE arch_style ILIKE %s AND basement ILIKE %s AND list_price < %s",
                   ['%Bungalow%', '%Walk Out%', 650000])

queries['q04'] = ("SELECT mls FROM property WHERE arch_style ILIKE %s AND full_baths >= %s AND list_price < %s",
                   ['%2 Storey%', 4, 950000])

queries['q05'] = ("SELECT mls FROM property WHERE type ILIKE %s AND year_built >= %s AND beds = %s",
                   ['%Townhouse%', 2021, 3])

queries['q06'] = ("SELECT mls FROM property WHERE fireplaces >= %s AND rms_sqft > %s",
                   [3, 2500])

queries['q07'] = ("SELECT mls FROM property WHERE is_condo = %s AND full_baths = %s AND list_price < %s AND year_built > %s",
                   ['Y', 1, 300000, 2015])

queries['q08'] = ("SELECT mls FROM property WHERE year_built < %s AND arch_style ILIKE %s",
                   [1940, '%Character%'])

queries['q09'] = ("SELECT mls FROM property WHERE type ILIKE %s AND basement ILIKE %s AND list_price < %s",
                   ['%Semi Detached%', '%Finished%', 700000])

queries['q10'] = ("SELECT mls FROM property WHERE type ILIKE %s AND beds >= %s AND list_price < %s AND arch_style ILIKE %s",
                   ['%Detached%', 4, 850000, '%Modern%'])

queries['q11'] = ("SELECT mls FROM property WHERE type ILIKE %s AND basement ILIKE %s AND beds = %s AND list_price BETWEEN %s AND %s",
                   ['%Duplex%', '%Unfinished%', 3, 540000, 660000])

queries['q12'] = ("SELECT mls FROM property WHERE rms_sqft > %s AND fireplaces >= %s",
                   [3000, 2])

queries['q13'] = ("SELECT mls FROM property WHERE type ILIKE %s AND beds = %s AND full_baths = %s AND list_price < %s",
                   ['%Row%', 2, 1, 425000])

queries['q14'] = ("SELECT mls FROM property WHERE arch_style ILIKE %s AND basement ILIKE %s",
                   ['%Bungalow%', '%Finished%'])

queries['q15'] = ("SELECT mls FROM property WHERE type ILIKE %s AND beds >= %s AND year_built >= %s",
                   ['%Detached%', 4, 2024])

queries['q16'] = ("SELECT mls FROM property WHERE is_condo = %s AND rms_sqft < %s AND full_baths = %s AND year_built > %s",
                   ['Y', 650, 1, 2019])

queries['q17'] = ("SELECT mls FROM property WHERE arch_style ILIKE %s AND full_baths = %s AND list_price BETWEEN %s AND %s",
                   ['%Split%', 3, 700000, 800000])

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
