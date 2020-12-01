"""
File: atm.py
Project 9.4
This module defines the ATM class, which provides a window
for bank customers to perform deposits, withdrawals, and check
balances.
Allows at most 3 login attempts, then calls the cops!
"""

from breezypythongui import EasyFrame
from bank import SavingsAccount, Bank, createBank
from atmclient import Client

class ATM(EasyFrame, Client):
    """Represents an ATM window.
    The window tracks the bank and the current account.
    The current account is None at startup and logout.
    """

    def __init__(self, bank):
        """Initialize the frame and establish the data model."""
        Client.__init__()
        
def main(fileName = None):
    """Creates the bank with the optional file name,
    wraps the window around it, and opens the window.
    Saves the bank when the window closes."""
    if not fileName:
        bank = createBank(5)
    else:
        bank = Bank(fileName)
    print(bank)
    atm = ATM(bank)
    atm.mainloop()

if __name__ == "__main__":
    main()
