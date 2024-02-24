class MixinRepr:
    """The class extends the descendant class by displaying information about the instance when it is created."""

    def __init__(self, *args, **kwargs):
        """Initialize using the parent's __init__ method and display the instance data."""
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self):
        """Return the class name and a list of attributes."""
        attributes = [f"{attr}={self.__dict__[attr]}" for attr in self.__dict__]
        return f"{self.__class__.__name__}({', '.join(attributes)})"
