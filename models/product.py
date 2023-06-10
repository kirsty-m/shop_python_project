class Product:
    def __init__(self, name, description, stock_quantity, buying_cost, selling_price, category, id = None, manufacturer):
        self.name = name
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.category = category
        self.id = id
        self.manufacturer = manufacturer