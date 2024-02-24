from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    """An abstract class for implementing all product classes."""

    @abstractmethod
    def __init__(self):
        """The method must initialize an instance of a class."""
        ...

    @abstractmethod
    def __len__(self):
        """The method must return the quantity of the product."""
        ...

    @abstractmethod
    def __add__(self, other):
        """Here you need to implement a method for adding products."""
        ...

    @abstractmethod
    def __str__(self):
        """Here you need to implement a method for string represent products."""
        ...
