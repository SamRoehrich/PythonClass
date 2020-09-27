# 10% down payment
# 12% interest rate
# 5% monthly payment

basePrice = float(input("Enter the base purchase price: "))
endingBalance = basePrice * .9
payment = endingBalance * .05
month = 1
interestToPay = 0.0
principleToPay = 0.0

print("Month    Starting Balance    Interest to Pay    Principal to Pay    Payment    Ending Balance")
while endingBalance != 0:
    interestToPay = (endingBalance * .12) / 12
    principleToPay = payment - interestToPay
#     print(str(month) + str(basePrice) + str(interestToPay) +
#           str(principleToPay) + str(payment) + str(endingBalance))

    print('{:d}           {:f}          {:01.2f}             {:01.2f}                 {:01.2f}        {:01.2f}'.format(
        month, endingBalance, interestToPay, principleToPay, payment, endingBalance))
    month += 1
    endingBalance = endingBalance - (interestToPay + principleToPay)
