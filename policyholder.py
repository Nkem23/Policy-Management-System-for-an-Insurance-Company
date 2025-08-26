# PolicyHolder Class
# Represents a customer who owns one or more insurance policies.
# Each policyholder has:ID,Name,Status (active/suspended,Products (list of assigned products), Payments (list of associated payments)

class PolicyHolder:
    def __init__(self, holder_id, name):
        self.holder_id = holder_id  
        self.name = name
        self.status = "active"     
        self.products = []
        self.payments = []         

    # Register a policyholder 
    def register(self):  
        self.status = "active"
        print(f"Policyholder {self.holder_id} registered successfully.")

    # Suspend a policyholder 
    def suspend(self):  
        if self.status == "active":
            self.status = "suspended"
            print(f"Policyholder '{self.name}' has been suspended.")
        else:
            print(f"Policyholder '{self.name}' is already {self.status}.")

    # Reactivate a suspended policyholder
    def reactivate(self):  
        if self.status != "active":
            self.status = "active"
            print(f"Policyholder '{self.name}' has been reactivated.")  
        else:
            print(f"Policyholder '{self.name}' is already {self.status}.")

    # Assign a product (insurance plan) to the policyholder
    def assign_product(self, product):  
        # Policyholder must be active
        if self.status != "active":
            print(f"Cannot assign product. Policyholder {self.holder_id} is suspended.")
            return False
        # Product must also be active
        if product.status != "active":
            print(f"Cannot assign product. Product {product.product_id} is suspended.")
            return False  
        # Avoid duplicates
        if product in self.products:
            print(f"Product {product.product_id} already assigned.")
            return True  
        # If all checks pass, assign product
        self.products.append(product)
        print(f"Product {product.product_id} assigned to policyholder {self.holder_id}.")
        return True  
    
    # Display policyholder details, including products and payments
    def display_details(self):  
        print(f"\nPolicyholder ID: {self.holder_id}, Name: {self.name}, Status: {self.status}")