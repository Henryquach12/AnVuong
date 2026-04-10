class Product:
    def __init__(self, ID, name, description, price, quantity=0):
        self.__ID = ID
        self.__name = name
        self.__description = description 
        self.__price = self.set_price(price)
        self.__quantity = quantity
    
    def get_ID(self):
        return self.__ID
    
    def get_name(self):
        return self.__name
    
    def get_description(self):
        return self.__description
    
    def get_price(self):
        return self.__price
    
    def get_quantity(self):
        return self.__quantity 
    
    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Invalid price")
    
    def increase_quantity(self):
        self.__quantity += 1
    
    def decrease_quantity(self):
        self.__quantity -= 1
    
    def __str__(self):
        return f"Product: {self.get_name()}\ndescription: {self.get_description()}\nprice: ${self.get_price()}\nquantity: {self.get_quantity()}"

class Store:
    
    def __init__(self, name, money):
        self.__name = name
        self.__money = self.set_money(money)
        self.__products = []
        
    def get_name(self):
        return self.__name

    def get_money(self):
        return self.__money

    def get_products(self):
        return self.__products
    
    def set_money(self, money):
        if money >= 0:
            self.__money = money
        else:
            print("Invalid money")
    
    def order(self, product):
        self.__products.append(product.get_name())
        product.increase_quantity()
        
    def find(self, ID):
        for product in self.__products:
            if product.get_ID() == ID:
                return product
            return None   

    def sell_product(self, ID, quantity):
        product = self.find(ID)
        if product is None:
            print("Product not found")
            return
        if product.get_quantity() == 0:
            print("Product is sold out")
            return
        if quantity > product.get_quantity():
            print("Not enough stock")
            return
        for sell in range(quantity):
            product.decrease_quantity()
        total_price = product.get_price() * quantity
        self.set_money(total_price)
    
    def markup_prices(self, multiplier):
        if multiplier <= 0:
            return
        for product in self.__products:
            new_price = product.get_price() * multiplier
            product.set_price(round(new_price, 2))
            
    def __str__(self):
        result = f"Store Name: {self.__name}\nMoney: ${self.__money}\n"
        if not self.__products:
            result += "No products in store"
        else:
            result += "Products:\n"
            for product in self.__products:
                result += str(product) + "\n"
        return result
                
product1 = Product(1, 'Pillow Set', 'Set of two bamboo material pillows.', 45.99, 2)
print(product1)

store1 = Store( 'Banana', 10)
store1.order(product1)
print(store1)

