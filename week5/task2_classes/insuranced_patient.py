from .patient import Patient

class InsurancedPatient(Patient):
    insurance_company = ""
    insurance_percentage = 0.0

    def __init__(self, name, age, insurance_company, insurance_percentage):
        super().__init__(name, age)
        self.insurance_company = insurance_company
        self.insurance_percentage = insurance_percentage

    def charge_insu_company(self):
        self.bill -= self.bill * (self.insurance_percentage / 100)

    def print_info(self):
        super().print_info()
        print("Insurance company: " + self.insurance_company)
        print()