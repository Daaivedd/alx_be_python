income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
Monthly_Savings = income - expenses  
print("your momnthly savings are {} " .format(Monthly_Savings))

Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)

print("Projected savings after one year, with interest, is: {} " .format(Projected_Savings) )