from project.product import Product


class Food(Product):
    DEFAULT_QUANTITY: int = 15

    def __init__(self, name):
        super().__init__(name, self.DEFAULT_QUANTITY)

