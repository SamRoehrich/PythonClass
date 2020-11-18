"""
File: taxformwithgui.py
Project 8.6
A GUI-based tax calculator.

Computes and prints the total tax, given the income and
number of dependents (inputs), and a standard deduction of
$10,000, an exemption amount of $3,000, and tax rates of
20% for Single
15% for Married
10% for Divorced
"""

from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):
    """Application window for the tax calculator."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Tax Calculator")

        # Label and field for the income
        # (self.incomeField)
        self.addLabel(text="Yearly income", row=0, column=0)
        self.income = self.addFloatField(
            value=0.0,
            row=1,
            column=0
        )

        # Label and field for the number of dependents
        # (self.depField)
        self.addLabel(text="Dependants", row=0, column=3)
        self.dependants = self.addIntegerField(
            value=0,
            row=1,
            column=3
        )
        # Radio buttons for filing status
        # Button group (self.statusGroup)
        # Option for single (self.single)
        # Option for married (self.married)
        # Option for divorced (self.divorced)
        self.group = self.addRadiobuttonGroup(
            row=2,
            column=0,
            columnspan=4,
            orient = "HORIZONTAL"
        )
        defaultRB = self.group.addRadiobutton("Single")
        self.group.addRadiobutton("Married")
        self.group.addRadiobutton("Divorced")
        self.group.setSelectedButton(defaultRB)
        # The compute button

        self.addButton("Calculate Tax", row=3, column=0, command=self.computeTax)
        # Label and field for the tax
        # (self.taxField)
        self.taxField = self.addFloatField("", row=4, column=2)

    # The event handler method for the button
    def computeTax(self):
        """Obtains the data from the input field and uses
        them to compute the tax, which is sent to the
        output field (taxField)."""
        rates = {
            "Single": .20,
            "Married": .15,
            "Divorced": .10
        }
        income = self.income.getNumber()
        dependants = self.dependants.getNumber()
        exemption = 10000
        status = self.group.getSelectedButton()["value"]
        rate = rates[status]
        tax = (income - dependants * exemption) * rate
        self.taxField.setNumber(tax)
        pass
        
        
def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()

