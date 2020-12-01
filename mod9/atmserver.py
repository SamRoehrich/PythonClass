from atmclient import Client

class Server():
    def __init__(self):
        self.bank = bank
        self.account = None
        self.loginCount = 0

    def getBalance(self):
        """Displays the current balance in the status field."""
        text = "Balance = $" + str(self.account.getBalance())
        self.statusField.setText(text)

    def deposit(self):
        amount = Client.amountField.getNumber()
        message = Client.account.deposit(amount)
        if not message:
            Client.statusField.setText("Deposit successful")
        else:
           Client.statusField.setText(message)
        
    def withdraw(self):
        """Attempts a withdrawal. If not successful, displays
        error message in statusfield; otherwise, announces
        success."""
        amount = Client.amountField.getNumber()
        message = Client.account.withdraw(amount)
        if not message:
            Client.statusField.setText("Withdrawal successful")
        else:
           Client.statusField.setText(message)
        