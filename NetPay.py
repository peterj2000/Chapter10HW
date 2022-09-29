

from EmployeeClass import Employee

from PayrollDeductionClass import PD

person= Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800)


d1= PD('food court', '8/14/2022', 22.50, 39119)
d2= PD('gift contribution', '8/12/2022', 25.00, 58475)
d3= PD('food court', '8/17/2022', 15.25, 21547)
d4= PD('vending machine', '8/22/2022', 3.00, 58475)
d5= PD('vending machine', '8/5/2022', 2.75, 58475)




print("*** Employee Pay ***")
print("Name:", person.getName())
print("ID Number:", person.getID())
print("Department:", person.getDepartment())
print("Gross Pay: $", float(person.getSalary()))
print("Net Pay: $", person.getSalary()+ d2.getAmount()+ d4.getAmount()+ d5.getAmount())
