from product import Product
from inventory import Inventory
from exceptions import ProductNotFoundError, InsufficientStockError

def section(title: str) -> None:
    print(f"\n{'─' * 55}")
    print(f"  {title}")
    print(f"{'─' * 55}")


def main():
    inv = Inventory()

    # ── 1. Add at least 8 products across 3+ categories ───────────────────
    section("1. Loading Inventory")
    
    categories = ["electronics", "accessories", "software", "kitchen"]
    products =[ 
        Product("Laptop", 999.99, stock=15, category="electronics"),
        Product("Laptop", 1099.99, stock=5, category="electronics"),
        Product("Mouse", 29.99, stock=50, category="electronics")  ,

        Product("keychain", 9.99, stock=105, category="accessories"),
        Product("flash drive", 19.99, stock=5, category="accessories"),
        Product("Turbo Tax", 299.99, stock=599, category="software")  ,

        Product("Adobe Photoshop", 9999.99, stock=1, category="software"),
        Product("Pressure Pot", 99.99, stock=5, category="kitchen"),
        Product("Microwave", 19.99, stock=50, category="kitchen")  ,

    ]

    for p in products:
        print(f"  Added: {p.name} → ID={inv.add_product(p)}")

    # ── 2. Display all products sorted by price ────────────────────────────
    section("2. All Products (sorted by price)")
   
    print(sorted(inv.products.values()))
    
    # ── 3. Search products by keyword ─────────────────────────────────────
    section("3. Search: 'pro'")

    print(inv.search("pro"))

    # ── 4. Filter by category ─────────────────────────────────────────────
    section("4. Category: 'electronics'")
    
    print(inv.by_category("electronics"))

    # ── 5. Sell products — one should succeed, one should fail ────────────
    section("5. Sell Operations")
    try:
        inv.sell(1, 20)
    except InsufficientStockError as e:
        print(e)

    # ── 6. Access a non-existent product ID ───────────────────────────────
    section("6. Non-Existent Product Lookup")
    try:
        inv.get_product(9999)
    except ProductNotFoundError as e:
        print(e)

    # ── 7. Transaction history ────────────────────────────────────────────
    section("7. Recent Transaction History")

    for h in inv.history:
        print(h)

    # ── 8. Inventory summary ──────────────────────────────────────────────
    section("8. Inventory Summary")
    '''
    "total_products":   
    "total_value":  
    "categories":       
    "out_of_stock_count"    
    '''
    summary = inv.summary()
    print(f"Total Products: {summary["total_products"]}\nTotal Value: {summary["total_value"]}\nCategories: {summary["categories"]}\nOut Of Stock Count: {summary["out_of_stock_count"]}\n")

    # ── 9. Set operations on categories ───────────────────────────────────
    section("9. Set Operations on Categories")

    my_wishlist = {"electronics", "gaming", "software"}
    print(inv.categories | my_wishlist)
    print(inv.categories & my_wishlist)
    print(inv.categories - my_wishlist)

    # ── 10. Tuple-based product configurations ────────────────────────────
    section("10. Product Configs as Tuples")
    configs = [
           ("Monitor", 349.99, 8, "electronics"),
           ("USB Hub",  24.99, 30, "accessories"),
            ("USB-C Hub",  34.99, 30, "accessories")
       ]
    for c in configs:
        inv.add_product(Product(c[0],c[1],c[2],c[3]))

    print(len(inv))
    
    # ── 11. Additional Error Tests ────────────────────────────
    section("11. Additional Error Tests")
    try:
        inv.get_product(-1)
    except ProductNotFoundError as e:
        print(e)
        
    try:
        inv.sell(0, -1)
    except InsufficientStockError as e:
        print(e)

if __name__ == "__main__":
    main()
