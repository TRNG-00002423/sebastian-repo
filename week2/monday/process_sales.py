"""
Week 2 Exercise — CSV processing with context managers.

TODO:
1. Read starter_code/data/sales.csv using csv.DictReader and with open(\n).
2. Compute rows count, grand total (sum of units * unit_price), average line revenue.
3. Find SKU with max line revenue (tie: first in file).
4. Write output/summary.txt using with open(\n, "w", encoding="utf-8").
'''



'''
Task 1 — Read and parse (30 min)
In starter_code/process_sales.py (create this file):

Open data/sales.csv with csv.DictReader, encoding="utf-8", newline="" on write if you also write CSV later.
Parse units and unit_price as numbers (int / float as appropriate).
Skip or fail gracefully on malformed rows (optional stretch: log count of bad rows to stderr).

Task 2 — Write report (25 min)
Use a second with open(\n, "w", encoding="utf-8") targeting output/summary.txt (path relative to starter_code/ or project root—pick one and document it in a comment).
Write plain text, human-readable lines, for example:
#
rows=\n
grand_total=\n
average_line_revenue=\n
top_sku=\n
top_line_revenue=\n


Task 3 — Self-check (10 min)
Run your script; open output/summary.txt.
Manually verify grand total for at least the first two rows with a calculator.
"""

from __future__ import annotations
import csv

def main() -> None:
    rows = 0
    seen_sku = {}
    with open("data/sales.csv", "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['sku'] not in seen_sku:
                seen_sku[row['sku']] = int(row['units'])*float(row['unit_price'])

            else:
                seen_sku[row['sku']] += int(row['units'])*float(row['unit_price'])

            rows+=1
            
    with open("output/summary.txt", "w",encoding="utf-8") as file:
        grand_total = sum(seen_sku.values())
        output=f"rows={rows}\ngrand_total=${grand_total}\naverage_line_revenue={(grand_total/rows):.2f}\ntop_sku={max(seen_sku, key=seen_sku.get)}\ntop_line_revenue=${max(seen_sku.values())}"
        file.write(output)


if __name__ == "__main__":
    main()
