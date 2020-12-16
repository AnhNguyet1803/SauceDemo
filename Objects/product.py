class Product:
    def __init__(self, name, desc, price, quantity=1):
        self.name = name
        self.desc = desc
        self.price = price
        self.quantity = quantity

    @property
    def __str__(self):
        return "name is '%s', desc is '%s', price is '%s', quantity is '%s'" % (self.name, self.desc, self.price,
                                                                                self.quantity)
