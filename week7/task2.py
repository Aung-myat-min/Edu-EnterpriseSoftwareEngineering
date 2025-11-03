from enum import Enum

class ContractType(Enum):
    full_time = 0
    part_time = 1
    fixed_time = 2
    zero_hour = 3
    temporary = 4

class Employee():
    def __init__(self, name, salary, contract_type, start_date):
        self.name = name
        self.salary = salary
        self.contract_type = contract_type
        self.start_date = start_date

    def get_name(self):
        return self.name

    def set_name(self, name):
        if name == "":
            print("Name cannot be empty")
        else:
            self.name = name

    def calculate_salary(self):
        print("Salary is:", self.salary)

    def get_contract_type(self):
        return self.contract_type

    def set_contract_type(self, contract_type):
        if type(contract_type) == ContractType:
            self.contract_type = contract_type
        else:
            print("Invalid Contract Type")

class PartTimeEmployee(Employee):
    def __init__(self, name, salary, contract_type, start_date, hour_per_week, hourly_rate):
        super().__init__(name, salary,contract_type, start_date)
        self.hour_per_week = hour_per_week
        self.hourly_rate = hourly_rate

class FullTimeEmployee(Employee):
    def __init__(self, name, salary, contract_type, start_date, band):
        super().__init__(name, salary, contract_type, start_date)
        self.band = band

    def get_band(self):
        return self.band

    def set_band(self, band):
        if band <= 0:
            print("Band cannot be less than 0")
        self.band = band

# Create a few employees
emp1 = Employee("Alice", 45000, ContractType.full_time, "2022-01-15")
emp2 = PartTimeEmployee("Bob", 0, ContractType.part_time, "2023-03-20", 20, 25)
emp3 = FullTimeEmployee("Charlie", 60000, ContractType.full_time, "2020-07-01", 3)

# --- Testing Employee (base class) ---
print("--- Testing Employee ---")
print(f"Name: {emp1.get_name()}")
print(f"Contract Type: {emp1.get_contract_type().name}")
emp1.calculate_salary()

# Test set_name
emp1.set_name("")       # Invalid
emp1.set_name("Alicia") # Valid
print(f"Updated name: {emp1.get_name()}")

# Test set_contract_type
emp1.set_contract_type("InvalidType")       # Invalid
emp1.set_contract_type(ContractType.zero_hour)  # Valid
print(f"Updated contract type: {emp1.get_contract_type().name}")

# --- Testing PartTimeEmployee ---
print("\n--- Testing PartTimeEmployee ---")
print(f"Name: {emp2.name}")
print(f"Hourly Rate: {emp2.hourly_rate}")
print(f"Hours per week: {emp2.hour_per_week}")

# Calculate salary manually (optional logic demonstration)
weekly_salary = emp2.hour_per_week * emp2.hourly_rate
print(f"Weekly salary: {weekly_salary}")

# --- Testing FullTimeEmployee ---
print("\n--- Testing FullTimeEmployee ---")
print(f"Name: {emp3.name}")
print(f"Band: {emp3.get_band()}")
emp3.set_band(-2)  # Invalid
emp3.set_band(5)   # Valid
print(f"Updated band: {emp3.get_band()}")

emp3.calculate_salary()
