class Publication():
    def __init__(self, title, price, copies) -> None:
        self.title = title
        self.price = price
        self.copies = copies

    def sell_copies(self, number_of_copies):
        if number_of_copies > 0 >= self.copies - number_of_copies:
            print("The number of copies are far exceed than the actual copies.")
        else:
            self.copies -= number_of_copies

class Book(Publication):
    def __init__(self, title, price, copies, author):
        super().__init__(title, price, copies)
        self.author = author

    def order_copies(self, number_of_copies):
        if number_of_copies <= 0:
            print("Order must be greater than 0.")
        else:
            self.copies += number_of_copies

class Magazine(Publication):
    def __init__(self, title, price, copies, order_quantity, current_issue):
        super().__init__(title, price, copies)
        self.order_quantity = order_quantity
        self.current_issue = current_issue

    def update_quantity(self, number_of_copies):
        if number_of_copies <= 0:
            print("Order must be greater than 0.")
        else:
            self.order_quantity = number_of_copies

    def receive_new_issue(self, new_issue):
        self.current_issue = new_issue

# Create a Book object
book1 = Book("The Art of AI", 29.99, 10, "Jane Doe")

# Create a Magazine object
mag1 = Magazine("Tech Weekly", 5.99, 20, 50, "Issue 45")

# --- Testing Book methods ---
print("--- Testing Book ---")
print(f"Initial copies of '{book1.title}': {book1.copies}")

# Sell some copies
book1.sell_copies(3)
print(f"Copies after selling 3: {book1.copies}")

# Try to sell too many copies
book1.sell_copies(20)  # exceeds available copies

# Order more copies
book1.order_copies(15)
print(f"Copies after ordering 15: {book1.copies}")

# Try to order invalid number
book1.order_copies(-5)

# --- Testing Magazine methods ---
print("\n--- Testing Magazine ---")
print(f"Initial quantity of '{mag1.title}': {mag1.order_quantity}")
print(f"Current issue: {mag1.current_issue}")

# Update order quantity
mag1.update_quantity(80)
print(f"Updated order quantity: {mag1.order_quantity}")

# Try to update with invalid number
mag1.update_quantity(-10)

# Receive new issue
mag1.receive_new_issue("Issue 46")
print(f"New issue received: {mag1.current_issue}")

# Sell some magazine copies
mag1.sell_copies(5)
print(f"Copies after selling 5: {mag1.copies}")

# Try to sell more than available
mag1.sell_copies(100)
