import pytest

from classes.category import Category, CategoryProductIter
from classes.exceptions import AddProductError
from classes.product import Product, SmartPhone, LawnGrass
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


def test_category_list(get_cat_1):
    category_list = CategoryProductIter(Category(*get_cat_1))
    assert [len(product) for product in category_list] == [3, 2]


def test_append_right_product(get_cat_1):
    cat = Category(*get_cat_1)
    new_prod = Product("p1", "", 1000, 10)
    new_phone = SmartPhone("phone", "", 5000, 5, 0, "", "", "")
    new_grass = LawnGrass("grass", "", 600, 10, "", "", "")
    try:
        cat.add_product(new_prod)
        cat.add_product(new_phone)
        cat.add_product(new_grass)
        assert True
    except:
        assert False


def test_append_wrong_product(get_cat_1):
    cat = Category(*get_cat_1)
    new_prod = Product("p1", "", 1000, 10)
    try:
        # cat.add_product(new_prod)
        cat.add_product(0)
    except TypeError as err:
        if str(err) == "You can only add an element of the Product class or its subclasses.":
            assert True
        else:
            assert False
    else:
        assert False


def test_get_average_price(get_cat_1):
    assert Category(*get_cat_1).get_avg_price() == 27500.0


def test_get_avg_price_zero():
    assert Category("category_name", "", []).get_avg_price() == 0


def test_append_product_zero():
    with pytest.raises(AddProductError, match="Cannot add a product with zero quantity."):
        Category("cat", "", []).add_product(Product("prod", "", 100, 0))
