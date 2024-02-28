# Домашняя работа 16.1

Выполнены задания: 1, 2, частично *

---


___Задание 1___:

В методе __Category.add_product__ добавлен вызов исключения __ValueError__, если в переданном объекте класса ___Product___ количество товара меньше или равно нулю.

---

___Задание 2___:

В классе __Category__ добавлен метод __get_avg_price()__, возвращающий среднюю стоимость продуктов: _СуммаВсехЦен / КоличествоПродуктов_.

При этом в конструкции __try/except__ проверяется исключение _ZeroDivisionError_, возникающее в случае деления на ноль, если продуктов в списке нет.

В этом случае устанавливаем возвращаемое значение равным __0.0__

Добавлены тесты метода __get_avg_price()__ для пустого и непустого списка продуктов.

---

__Задание *__:

ВЫПОЛНЕНО ЧАСТИЧНО

В файле ___classes/exceptions.py___ создан отдельный класс исключения __AddProductException__, унаследованный от _Exception_.

В методе __Category.add_product__ вызов исключения __ValueError__ заменён на вызов __AddProductException__.

Добавлены тест вызова исключения __AddProductException__ при добавления продукта с нулевым количеством товара.

---
__TODO__: Переименовать исключение __AddProductException__ в __AddProductError__.
