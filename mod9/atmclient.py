from breezypythongui import EasyFrame
from atmclienthandler import Handler

class Client(EasyFrame, Handler):
    def __init__(self):
        """Initialize the frame and establish the data model."""
        EasyFrame.__init__(self, title = "ATM")
        # Create and add the widgets to the window."""
        self.nameLabel = self.addLabel(row = 0, column = 0,
                                       text = "Name")
        self.pinLabel = self.addLabel(row = 1, column = 0,
                                      text = "PIN")
        self.amountLabel = self.addLabel(row = 2, column = 0,
                                         text = "Amount")
        self.statusLabel = self.addLabel(row = 3, column = 0,
                                         text = "Status")
        self.nameField = self.addTextField(row = 0, column = 1,
                                           text = "")
        self.pinField = self.addTextField(row = 1, column = 1,
                                          text = "")
        self.amountField = self.addFloatField(row = 2, column = 1,
                                              value = 0.0)
        self.statusField = self.addTextField(row = 3, column = 1,
                                             text = "Welcome to the Bank!")
        self.balanceButton = self.addButton(row = 0, column = 2,
                                            text = "Balance",
                                            command = Handler.getBalance,
                                            state = "disabled")
        self.depositButton = self.addButton(row = 1, column = 2,
                                            text = "Deposit",
                                            command = Handler.deposit,
                                            state = "disabled")
        self.withdrawButton = self.addButton(row = 2, column = 2,
                                             text = "Withdraw",
                                             command = Handler.withdraw,
                                             state = "disabled")
        self.loginButton = self.addButton(row = 3, column = 2,
                                          text = "Login",
                                          command = Handler.login)
 