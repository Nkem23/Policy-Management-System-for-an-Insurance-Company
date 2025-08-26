# MAIN DEMONSTRATION SCRIPT
# Here, we will:
# 1. Create products
# 2. Create policyholders
# 3. Assign products to them
# 4. Make payments
# 5. Display full account details


from product import Product
from policyholder import PolicyHolder
from payment import Payment

# Step 1: Create insurance products
product1 = Product(101, "Health Insurance", 50000)
product2 = Product(102, "Car Insurance", 75000)

# Step 2: Create policyholders (customers)
holder1 = PolicyHolder(1, "Alice Johnson")
holder2 = PolicyHolder(2, "Michael Smith")

# Step 3: Assign insurance products to policyholders
holder1.assign_product(product1)
holder2.assign_product(product2)

# Step 4: Create payment records for each policyholder
payment1 = Payment(201, policy_number=holder1.holder_id, amount=product1.price, due_date="2025-09-01")
payment2 = Payment(202, policy_number=holder2.holder_id, amount=product2.price, due_date="2025-09-01")

# Step 5: Process (mark as paid)
payment1.process_payment()
payment2.process_payment()

# Step 6: Link payments to the policyholders' accounts
holder1.payments.append(payment1)
holder2.payments.append(payment2)

# Step 7: Display final account details
print("\n--- Policyholder 1 Account Details ---")
holder1.display_details()
for pay in holder1.payments:
    pay.display_payment()

print("\n--- Policyholder 2 Account Details ---")
holder2.display_details()
for pay in holder2.payments:
    pay.display_payment()
