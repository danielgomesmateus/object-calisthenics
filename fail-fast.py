class Product:
    def __init__(self, name: str, price: float):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Product price must be non-negative.")

        self.name = name
        self.price = price


p = Product("Café", 15.0)

p = Product("", -20.0)
