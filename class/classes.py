class Farmer:
    def __init__(self, name, district, produce, quantity):
        self.name = name
        self.district = district
        self.produce = produce
        self.quantity = quantity


class Produce:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ProfitCalculator:
    @staticmethod
    def calculate(quantity, price, transport):
        return (quantity * price) - transport