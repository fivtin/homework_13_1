from classes.category import Category
from fixtures import get_cat_1, get_cat_2


def test_create_category(get_cat_1):
    cat_1 = Category(*get_cat_1)
    assert len(cat_1.products) == 2
    assert cat_1.name == "TV"


def test_get_product_properties(get_cat_1):
    cat_1 = Category(*get_cat_1)
    assert cat_1.products[0].name == "Samsung UE32E5000"
    assert cat_1.products[0].description == "SmartTV with AMOLED screen and built-in WiFi adapter."
    assert cat_1.products[0].price == 25000
    assert cat_1.products[0].quantity == 3


def test_get_number_unique_products(get_cat_1, get_cat_2):
    Category.unique_products = 0
    assert Category(*get_cat_2).unique_products == 2


def test_get_number_categories(get_cat_1):
    Category.number_categories = 0
    assert Category(*get_cat_1).number_categories == 1


def test_products_list(get_cat_1):
    assert Category(*get_cat_1).products_list[0] == "Samsung UE32E5000, 25000 руб. Остаток: 3 шт."


def test_self_len(get_cat_1):
    assert len(Category(*get_cat_1)) == 5


def test_string_represent(get_cat_1):
    assert str(Category(*get_cat_1)) == "TV, количество продуктов: 5 шт."

