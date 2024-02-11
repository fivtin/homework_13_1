from classes.product import Product
from fixtures import get_prod_1


def test_create_product(get_prod_1):
    prod_1 = Product(*get_prod_1)
    assert prod_1.name == "Samsung UE32E5000"
    assert prod_1.price == 25000
    assert prod_1.description == "SmartTV with AMOLED screen and built-in WiFi adapter."
    assert prod_1.quantity == 3


def test_create_new_product():
    prod_1 = Product("name_1", "", 1000, 1)
    prod_2 = Product.create_product("name_2", "", 2000, 2)
    assert id(prod_1) != id(prod_2)


def test_create_same_product():
    Product._Product__all_products = list()
    prod_1 = Product("name_1", "", 1000, 1)
    prod_2 = Product.create_product("name_1", "", 2000, 2)
    assert id(prod_1) == id(prod_2)
    assert prod_1.price == 2000
    assert prod_1.quantity == 3


def test_reset_price():
    prod_1 = Product("name_1", "", 1000, 1)
    del prod_1.price
    assert prod_1.price == 0.0


def test_price_increase():
    prod_1 = Product("name_1", "", 1000, 1)
    prod_1.price = 2000
    assert prod_1.price == 2000


def test_price_reduction():
    prod_1 = Product("name_1", "", 1000, 1)
    prod_1.price = -200
    assert prod_1.price == 1000
