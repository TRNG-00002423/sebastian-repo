from collections import deque

from exceptions import ProductNotFoundError, InsufficientStockError
from product import Product


class Inventory:
    """A collection of products with search, filter, and transaction tracking.

    Internal Data Structures:
        products (dict):      {product_id (int): Product}
        categories (set):     Unique category strings — auto-maintained
        history (deque):      Recent transactions, maxlen=50
        _next_id (int):       Auto-incrementing product ID counter

    Key Constraints:
        - sell() must raise InsufficientStockError if stock < quantity
        - get_product() and remove_product() must raise ProductNotFoundError if ID missing
        - All query methods (search, by_category, in_stock, price_range) use comprehensions
    """

    def __init__(self):
        self.products: dict[int, Product] = {}
        self.categories: set[str] = set()
        self.history: deque[str] = deque(maxlen=50)
        self._next_id: int = 1

    # ── CRUD ─────────────────────────────────────────────────────────────────

    def add_product(self, product: Product) -> int:
        self.products[self._next_id] = product
        self.categories.add(product.category)
        self.history.append(f"ADD: {product.name} (ID={self._next_id})")
        self._next_id += 1
        return self._next_id-1
        
    def remove_product(self, product_id: int) -> Product:
        try:
            removed_product = self.products.pop(product_id)
            self.history.append(f"REMOVE: {removed_product.name} (ID={product_id})")
            return removed_product
        except IndexError:
            raise ProductNotFoundError(product_id)
       
    def get_product(self, product_id: int) -> Product:
        try:
            product = self.products[product_id]
            return product
        except KeyError:
            raise ProductNotFoundError(product_id)

    def sell(self, product_id: int, quantity: int) -> None:
        try:
            product = self.get_product(product_id)
        except KeyError:
            raise ProductNotFoundError(product_id)
        
        if product.stock < quantity:
            raise InsufficientStockError(product.name, quantity, product.stock)
        product.stock -= quantity
        self.history.append(f"SELL: {quantity}x {product.name} (ID={product_id})")
        
    def restock(self, product_id: int, quantity: int) -> None:
        try:
            product = self.get_product(product_id)
        except KeyError:
            raise ProductNotFoundError(product_id)
        finally:
            product.stock += quantity
            self.history.append(f"RESTOCK: +{quantity} {product.name} (ID={product_id})")

    # ── Comprehension-Powered Queries ─────────────────────────────────────────

    def search(self, keyword: str) -> list[Product]:
        """Return products whose name contains keyword (case-insensitive).

        Hint: Use __contains__ dunder on Product — "keyword" in product
        Use a list comprehension over self.products.values().
        """
        return [product for product in self.products.values() if (keyword in product)]

    def by_category(self, category: str) -> list[Product]:
        """Return all products in the given category (case-insensitive).

        Use a list comprehension. Compare category.lower() to product.category.lower().
        """
        return [product for product in self.products.values() if product.category.lower() == category.lower()]

    def in_stock(self) -> list[Product]:
        """Return all products with stock > 0.

        Hint: Use __bool__ dunder on Product — bool(product) is True if in stock.
        Use a list comprehension with the bool() check.
        """
        return [product for product in self.products.values() if bool(product)]

    def price_range(self, min_price: float, max_price: float) -> list[Product]:
        """Return products priced between min_price and max_price (inclusive).

        Use a list comprehension.
        """
        return [product for product in self.products.values() if product >= min_price and product <= max_price]

    def summary(self) -> dict:
        """Return a summary dictionary of the inventory.

        Returns:
            {
                "total_products":   int — number of products,
                "total_value":      float — sum of (price * stock) for each product,
                "categories":       list[str] — sorted list of unique category names,
                "out_of_stock_count": int — products where stock == 0,
            }

        Use dict/list/generator comprehensions — avoid raw for loops.
        """
        total_products = len(self.products)
        total_value = sum(product.price * product.stock for product in self.products.values()) 
        categories = sorted(set(self.products))
        out_of_stock_count = [product for product in self.products.values() if not bool(product)]
        
        return {
            "total_products" : total_products,
            "total_value" : total_value,
            "categories" : categories,
            "out_of_stock_count" : out_of_stock_count
        }

    def __len__(self) -> int:
        """Return the number of products in the inventory."""
        return len(self.products)

    def __repr__(self) -> str:
        return f"Inventory({len(self)} products, categories={sorted(self.categories)})"
