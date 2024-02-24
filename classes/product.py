from classes.abstract import AbstractProduct
from classes.mixins import MixinRepr


class Product(AbstractProduct):
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

    def __add__(self, other):
        """
        Implementation of the product addition method.
        Adding only elements of the same type.
        """
        if isinstance(self, other.__class__) and isinstance(other, self.__class__):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Elements must be of the same type.")

    def __len__(self):
        """Returns the quantity of a product."""
        return self.quantity

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
        """ Method for resetting the private attribute 'price'. """
        self.__price = 0.0


class SmartPhone(MixinRepr, Product):
    """The 'smartphone' class extends the base 'product' class."""

    performance: float
    model: str
    internal_memory: str
    colour: str

    def __init__(self, name, description, price, quantity, performance, model, internal_memory, colour):
        """ Extend the base class constructor. """
        self.performance = performance
        self.model = model
        self.internal_memory = internal_memory
        self.colour = colour
        super().__init__(name, description, price, quantity)


class LawnGrass(MixinRepr, Product):
    """ The 'lawn grass' class extends the base 'product' class. """

    country: str
    germination_period: str
    colour: str

    def __init__(self, name, description, price, quantity, country, germination_period, colour):
        """ Extend the base class constructor. """
        self.country = country
        self.germination_period = germination_period
        self.colour = colour
        super().__init__(name, description, price, quantity)
