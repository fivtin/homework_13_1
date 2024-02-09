import json

from classes.category import Category
from classes.product import Product


def load_from_file(filename: str):
    """Load categories with products list from json file."""
    categories_list = list()
    with open(filename, encoding='utf-8') as f:
        items = json.load(f)
    for item in items:
        category = Category(item['name'], item['description'], [])
        for product in item['products']:
            category.products.append(
                Product(product['name'], product['description'], product['price'], product['quantity'])
            )
        categories_list.append(category)
    return categories_list
