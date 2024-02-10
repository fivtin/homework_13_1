class Product:
    """Class to represent Product."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Method to initialize an instance of a class. Set values for the instance attributes."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
