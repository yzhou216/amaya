import paydeductions

def fDeductNetpay(gross_pay: float) -> float:
    return (paydeductions.fFedTax(gross_pay) +
            paydeductions.fStateTax(gross_pay) +
            paydeductions.fOASDI(gross_pay))

print("Welcome to the net paycheck calculator")
gross_pay = input("Enter gross pay: ")
deductions = fDeductNetpay(float(gross_pay))
net_pay = float(gross_pay) - deductions
print("Gross pay = $" + gross_pay)
print("Deductions = $" + str(deductions))
print("Net pay = $" + str(net_pay))
