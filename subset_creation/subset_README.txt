GraphRAG/LightRAG evaluation subset
Frozen: 05/08/2026
Method: Random sample of 200 listings from `property` table (mls_data DB),
generated via pick_subset.py, ORDER BY RANDOM() LIMIT 200.
Coverage verified across:
  - property type x bedroom count combinations
  - price bands ($500k increments)
  - year-built bands
  - subdivision clustering
One underrepresented combination found (4-bed semi-detached, n=1);
supplemented with 5 additional matching listings via topup.py.
Final subset size: 205 listings.
File: subset_mls_list_FROZEN_05-08-2026.txt
