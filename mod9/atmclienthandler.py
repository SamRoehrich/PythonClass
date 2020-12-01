from atmserver import Server
from atmclient import Client
class Handler(Server, Client):
     
    def login(self):
        """Attempts to login the customer.  If successful,
        enables the buttons, including logout."""
        Server.loginCount += 1
        name = Client.nameField.getText()
        pin = Client.pinField.getText()
        Client.account = Client.bank.get(name, pin)
        if Client.account:
            Client.loginCount = 0
            Client.statusField.setText("Hello, " + name + "!")
            Client.balanceButton["state"] = "normal"
            Client.depositButton["state"] = "normal"
            Client.withdrawButton["state"] = "normal"
            Client.loginButton["text"] = "Logout"
            Client.loginButton["command"] = Server.logout
        elif Client.loginCount == 3:
            Client.messageBox(title = "DANGER",
                            message = "3 unsuccessful login attempts, so we're calling the cops!")
            Client.loginButton["state"] = "disabled"
            return

        else:
            Client.statusField.setText("Name and pin not found!")
            
    def logout(self):
        """Logs the cusomer out, clears the fields, disables the
        buttons, and enables login."""
        Client.account = None
        Client.nameField.setText("")
        Client.pinField.setText("")
        Client.amountField.setNumber(0.0)
        Client.statusField.setText("Welcome to the Bank!")
        Client.balanceButton["state"] = "disabled"
        Client.depositButton["state"] = "disabled"
        Client.withdrawButton["state"] = "disabled"
        Client.loginButton["text"] = "Login"
        Client.loginButton["command"] = Server.login