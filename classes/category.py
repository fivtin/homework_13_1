from classes.product import Product, LawnGrass, SmartPhone


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
        return sum([len(product) for product in self.__products])

    @property
    def products(self):
        """Return the hidden value of the product list."""
        return self.__products

    def add_product(self, product):
        """
        Adds a product to the list.
        Checking the element type. There must be a "Product" or its subclasses.
        """
        if issubclass(product.__class__, Product):
            if product.quantity <= 0:
                raise ValueError("Сannot add a product with zero quantity.")
            self.__products.append(product)
            Category.unique_products += 1
        else:
            raise TypeError("You can only add an element of the Product class or its subclasses.")

    @property
    def products_list(self):
        """Return a list of strings with information about products."""
        return [str(product) for product in self.__products]

    def get_avg_price(self):
        """Returns the average price of all products, or zero if the list of products is empty."""
        try:
            total_price = sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            total_price = 0
        return total_price


class CategoryProductIter:
    """The class implements iterating over objects in the list of “products”."""

    def __init__(self, category):
        """Initializing a class with a "Category" object."""
        self.category = category

    def __iter__(self):
        """Return an iterator object."""
        self.index = -1
        return self

    def __next__(self):
        """Getting the next object from the "Products" list."""
        self.index += 1
        if self.index < len(self.category.products):
            return self.category.products[self.index]
        else:
            raise StopIteration
