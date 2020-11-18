"""
File: bouncywithgui.py
Project 8.2

Determines the distance traveled by a bouncing ball.

Inputs: Initial height, bounciness index, and number of bounces
"""

from breezypythongui import EasyFrame

def computeDistance(height, index, bounces):
    """Computes the total distance traveled by the ball,
    given an initial height, bounciness index, and
    number of bounces."""
    pass

class BouncyGUI(EasyFrame):

    def __init__(self):
        """Set up the window and widgets."""
        EasyFrame.__init__(self,  title = "Bouncy")
        # Define the following fields:
        # * self.heightField (number entry)
        # * self.indexField (number entry)
        # * self.bouncesField (number entry)
        # * self.distanceField (result result)

    def computeDistance(self):
        """
        Event handler for the Compute button and set the
        distanceField.
        """
        pass

def main():
    """Instantiate and pop up the window."""
    BouncyGUI().mainloop()

if __name__ == "__main__":
    main()

