from classes.product import Product
from fixtures import get_prod_1


def test_create_product(get_prod_1):
    prod_1 = Product(*get_prod_1)
    assert prod_1.name == "Samsung UE32E5000"
    assert prod_1.price == 25000
    assert prod_1.description == "SmartTV with AMOLED screen and built-in WiFi adapter."
    assert prod_1.quantity == 3
