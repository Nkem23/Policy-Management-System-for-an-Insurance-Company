from datetime import datetime

# Payment Class
# Represents a payment made by a policyholder for a product.
# Each payment has:ID, Policy number, Amount, Due date, Payment date,Status (pending/paid/overdue),Penalty
# ===============================

class Payment:
    def __init__(self, payment_id, policy_number, amount, due_date=None):
        self.payment_id = payment_id
        self.policy_number = policy_number   
        self.amount = float(amount)
        self.due_date = due_date
        self.payment_date = None
        self.status = "pending"              
        self.penalty = 0.0                   

    # Mark payment as completed
    def process_payment(self):
        if self.status != 'paid':
            self.status = 'paid'
            self.payment_date = datetime.today().strftime("%Y-%m-%d")
            print(f"Payment ID {self.payment_id} for policy {self.policy_number} has been successfully processed.")
            return True
        else:
            print(f"Payment ID {self.payment_id} is already marked as 'paid'.")
            return False

    # Send a reminder if payment is overdue
    def send_reminder(self, today: str):
        if self.status == "paid":
            return None
        if self.due_date and today > self.due_date:
            return f"Reminder: Payment {self.payment_id} for policy {self.policy_number} is overdue!"
        return None

    # Apply penalty to overdue payments
    def apply_penalty(self, penalty_amount):
        if self.status != 'paid':
            self.amount += penalty_amount
            self.penalty += penalty_amount
            self.status = "overdue with penalty"
            print(f"Penalty of ₦{penalty_amount:.2f} applied to Payment ID {self.payment_id}.")
        else:
            print(f"Cannot apply penalty. Payment ID {self.payment_id} is already paid.")

    # Display payment details
    def display_payment(self):
        print(f"Payment ID: {self.payment_id}, Amount: ₦{self.amount:.2f}, "
              f"Penalty: ₦{self.penalty:.2f}, Status: {self.status}, "
              f"Paid on: {self.payment_date or 'Not paid'}")
