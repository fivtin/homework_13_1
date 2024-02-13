from classes.product import Product


class Category:
    """Class to represent product Categories."""
    name: str
    description: str = ''
    number_categories: int = 0
    unique_products: int = 0

    def __init__(self, name, description, products_list):
        """Method to initialize an instance of a class. Set values for the instance attributes."""
        self.name = name
        self.description = description
        self.__products = products_list
        Category.unique_products += len(products_list)
        Category.number_categories += 1

    def __str__(self):
        """Returns a string representation of the 'category' instance."""
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __len__(self):
        """Returns the total quantity of all products in the 'category' instance."""
        return sum([product.quantity for product in self.__products])

    @property
    def products(self):
        """Return the hidden value of the product list."""
        return self.__products

    def add_product(self, product: Product):
        """Adds a product to the list"""
        self.__products.append(product)
        Category.unique_products += 1

    @property
    def products_list(self):
        """Return a list of strings with information about products."""
        return [str(product) for product in self.__products]
