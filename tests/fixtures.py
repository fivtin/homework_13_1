from pytest import fixture

from classes.product import Product


def get_data_prod_1():
    return "Samsung UE32E5000", "SmartTV with AMOLED screen and built-in WiFi adapter.", 25000, 3


def get_data_prod_2():
    return "LG 32LM576BPLD", '32" (80 см) Телевизор LED LG 32LM576BPLD черный', 30000, 2


@fixture
def get_prod_1():
    return get_data_prod_1()


@fixture
def get_cat_1():
    return "TV", "", [Product(*get_data_prod_1()), Product(*get_data_prod_2())]


@fixture
def get_cat_2():
    return "SmartTV", "", [Product(*get_data_prod_2()), Product(*get_data_prod_1())]
