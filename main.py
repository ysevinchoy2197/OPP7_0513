#3-misol
class Phone:
    factory = "China"
    charger_type = "Type-C"

    def __init__(self, brand, model, memory, price):
        self.brand = brand
        self.model = model
        self.memory = memory
        self.price = price

    def show_employee(self):
        print(f"Brendi: {self.brand}")
        print(f"Modeli: {self.model}")
        print(f"memory: {self.memory}")
        print(f"price: {self.price}")


    def change_price(self, new_price):
        self.new = new_price

    def update_memory(self, new_memory):
        self.memory = new_memory


p1 = Phone(f"Samsung", "galaxy s10", "128gb", 400)
p2 = Phone(f"Phone", "iphone 15 pro max", "128gb", 200)
