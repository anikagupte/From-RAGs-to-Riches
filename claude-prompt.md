You are helping generate realistic search queries for evaluating a real-estate search system. I need natural-language queries that a genuine home buyer might type into a search box, sorted into five categories below. For each category, I've given you a definition and one example — generate queries that match the definition, in the spirit of the example, but varied in phrasing, specificity, and style. Do not just lightly reword the example.

Important constraints:
•	Write like a real person searching, not a formal specification. Vary sentence length and structure — some queries can be short and blunt, others longer and more conversational.
•	Do not use overly clinical or repetitive phrasing across queries in the same category.
•	Each query should belong clearly to ONE category — avoid queries that could easily be sorted into two categories at once.
•	Do not invent property IDs, listing numbers, or specific addresses.
•	Assume the housing market is Calgary, Canada (typical price ranges, property types, and terminology for that market).

Generate 18 queries per category (90 total).

Category 1: Structured (SQL-extractable)
Definition: Every factor in the query maps to one of nine structured filters: price, bedrooms, bathrooms, square footage, year built, fireplaces, property type, architectural style, or basement type.
Example: "4-bedroom detached house under $750,000, built after 2010"

Category 2: VLM-generated image captions
Definition: Query describes a visual attribute using vocabulary similar to what a property-photo captioning system would typically describe (e.g. general room features, windows, style, layout).
Example: "High ceilings and large glass windows"

Category 3: CLIP image search
Definition: Query describes a specific, fine-grained visual detail (colour scheme, decor style, specific finishes) that a general captioning system would likely NOT explicitly describe.
Example: "Black and gold décor kitchen"

Category 4: Graph-structured / cross-listing
Definition: Query requires comparing or aggregating data across multiple listings — it cannot be answered by evaluating a single listing in isolation.
Example: "Compare the price per square foot of 3-bedroom semi-detached houses"

Category 5: Compound queries
Definition: Mixes two or more of the mechanisms above into one realistic query.
Example: "Find a 2-bedroom city apartment that has high ceilings and is relatively cheap compared to others in the area"
Output as a numbered list grouped under each category heading, so I can easily copy them into a table.
