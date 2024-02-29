class AddProductError(Exception):
    """An exception occurs if a product with zero quantity is added."""

    def __init__(self, *args, **kwargs):
        """Initialize an object with a default message."""
        self.message = args[0] if args else "Cannot add a product with zero quantity."

    def __str__(self):
        """A string representation of the object that returns an error message."""
        return self.message
