# given wage, regular hours and overtime hours calculate the weekly pay
# overtime pay is 1.5 wage

wage = float(input("Enter your wage: "))
regularHours = float(input("Enter the regular work hours: "))
overtime = float(input("Enter overtime hours: "))


def calculatePay(wage, hours, overtime):
    if hours + overtime > 168:
        raise ValueError("There are not that many hours in a week.")
    res = (wage * hours) + ((wage * 1.5) * overtime)
    return res


result = calculatePay(wage, regularHours, overtime)
print("The total weekly pay is $" + str(result))
