class Patient:
    name = ""
    age = 0
    bill = 0.0
    number_of_treatment = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_treatment(self, no_of_treatment):
        self.number_of_treatment += no_of_treatment

    def add_bill(self, bill):
        self.bill += bill

    def pay_bill(self):
        self.bill = 0

    def print_info(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Bill: " + str(self.bill))
        print("Number of treatment: " + str(self.number_of_treatment))
        print()