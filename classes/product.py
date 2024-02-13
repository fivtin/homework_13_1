class Product:
    """Class to represent Product."""
    name: str
    description: str
    __price: float
    quantity: int
    __all_products: list = list()

    def __init__(self, name: str, description, price, quantity):
        """Method to initialize an instance of a class. Set values for the instance attributes."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.__all_products.append(self)

    def __str__(self):
        """Returns a string representation of the 'product' instance."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def create_product(cls, name, description, price, quantity):
        """
        The method returns an instance of the class if a product with the same name has not been created previously.
        Otherwise, returns the existing instance.
        """
        for product in cls.__all_products:
            if product.name == name:
                product.quantity += quantity
                if price > product.price:
                    product.price = price
                return product

        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Method for accessing the private attribute 'price'."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Method for changing the private attribute 'price'."""
        if new_price > 0:
            if new_price < self.__price:
                if input("Снизить цену? (y/n): ").strip().lower() == "y":
                    self.__price = new_price
            else:
                self.__price = new_price
        else:
            print("Некорректная цена.")

    @price.deleter
    def price(self):
        """Method for resetting the private attribute 'price'."""
        self.__price = 0.0
