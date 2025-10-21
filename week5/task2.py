from task2_classes.patient import Patient
from task2_classes.insuranced_patient import InsurancedPatient

example_patient = Patient("AMM", 20)
example_patient.print_info()

example_patient.add_treatment(3)
example_patient.add_bill(400)
example_patient.print_info()

example_patient.pay_bill()
example_patient.print_info()

example_insu_patient = InsurancedPatient("NMKK", 20, "Alive7", 50)
example_insu_patient.print_info()

example_insu_patient.add_treatment(1)
example_insu_patient.add_bill(1000)
example_insu_patient.print_info()

example_insu_patient.charge_insu_company()
example_insu_patient.print_info()

example_insu_patient.pay_bill()
example_insu_patient.print_info()


