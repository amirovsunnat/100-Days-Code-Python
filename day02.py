print('Welcome to the tip calculator')
totalBill = float(input('What was the total bill? $'))
totalPeople = int(input('How many people to split the bill? '))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
tipCost = totalBill * tip / 100
payment = (tipCost + totalBill)/totalPeople
finalPayment = "{:.2f}".format(payment)
print(f'Each person should pay: ${finalPayment}')
