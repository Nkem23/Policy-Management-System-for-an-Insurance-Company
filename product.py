# Product Class
# Represents an insurance product (e.g., Health Insurance, Car Insurance).
# Each product has ID, Name, Price, Status (active/suspended)

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.status = "active"   
        
    # Update product details (name or price)
    def update_product(self, new_name=None, new_price=None):
        if new_name:
            self.name = new_name
        if new_price:
            self.price = new_price
        print(f"Product {self.product_id} updated successfully to Name: {self.name}, Price: {self.price}")
        
    # Suspend a product (e.g., stop selling it temporarily)
    def suspend_product(self):
        if self.status == "active":
            self.status = "suspended"
            print(f"Product {self.product_id} suspended.")
        else:
            print(f"Product {self.product_id} is already suspended.")
        
    # Reactivate a suspended product
    def reactivate_product(self):
        if self.status != "active":
            self.status = "active"
            print(f"Product {self.product_id} reactivated.")
        else:
            print(f"Product {self.product_id} is already active.")
            
    # Display product information
    def display_product(self):
        print(f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Status: {self.status}")