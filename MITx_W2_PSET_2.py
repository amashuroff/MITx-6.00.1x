

# Problem 1, Paying Debt off in a Year
# Write a program to calculate the credit card balance after one year,
# if a person only pays the minimum monthly payment required by the credit card company each month.
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
updated_balance = 0
for month in range(1,13):
    m_pmt = (balance * monthlyPaymentRate)
    updated_balance = (balance - m_pmt) + ((annualInterestRate/12.0)*(balance - m_pmt))
    balance = updated_balance
print("Remaining balance: " + str(updated_balance.__round__(2)))


# Problem 2, Paying Debt Off in a Year round 2
# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not change each month,
# but instead is a constant amount that will be paid each month.
fxd_pmt = 0
monthly_i_r = annualInterestRate/12.0
test_balance = balance
while balance > 0:
    for month in range(1, 13):
        unpaid_balance = balance - fxd_pmt
        balance = unpaid_balance + unpaid_balance * monthly_i_r

    if balance <= 0:
        print('Lowest Payment: ' + str(fxd_pmt))
        break

    else:
        fxd_pmt += 10
        balance = test_balance


# Problem 3, Using Bisection Search to Make the Program Faster (based on problem 2)
monthly_i_rate = annualInterestRate / 12.0
lower_bound = balance / 12.0
upper_bound = (balance * (1 + monthly_i_rate) ** 12) / 12.0

epsilon = 0.05
while True:


    test_balance = balance
    guess_monthly_pmt = round(((lower_bound + upper_bound) / 2.0), 2)


    for i in range(12):
        test_balance -= guess_monthly_pmt
        test_balance += (monthly_i_rate * test_balance)
    test_balance = round(test_balance, 2)


    if (abs(test_balance) < epsilon) and test_balance <= 0:
        break


    if abs(upper_bound - lower_bound) <= .02:
        break


    if test_balance < epsilon:
        upper_bound = guess_monthly_pmt


    elif test_balance > epsilon:
        lower_bound = guess_monthly_pmt

print("Lowest Payment: " + str(guess_monthly_pmt))