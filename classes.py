class Pizza:
    def __init__(self):
        self.size = None
        self.style = None
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def print_order(self):
        toppings_str = ", ".join(self.toppings)
        print(f"I would like a {self.size}-inch, {self.style} pizza with {toppings_str}.")


# Creating two instances of Pizza
meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "deep-dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.print_order()

veggie_lovers = Pizza()
veggie_lovers.size = 12
veggie_lovers.style = "thin-crust"
veggie_lovers.add_topping("Mushrooms")
veggie_lovers.add_topping("Bell peppers")
veggie_lovers.add_topping("Onions")
veggie_lovers.print_order()
