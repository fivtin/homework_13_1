class Category:
    """Class to represent product Categories."""
    name: str
    description: str = ''
    products: list = list()
    _number_categories: int = 0
    _unique_products: set = set()

    def __init__(self, name, description, products_list):
        """Method to initialize an instance of a class. Set values for the instance attributes."""
        self.name = name
        self.description = description

        for product in products_list:
            self.products.append(product)
            Category._unique_products.add(product.name)

        Category._number_categories += 1

    @staticmethod
    def get_number_categories():
        """Get the total number of categories."""
        return Category._number_categories

    @staticmethod
    def get_number_unique_products():
        """Get the number of unique products."""
        return len(Category._unique_products)
