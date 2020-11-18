from breezypythongui import EasyFrame

class Converter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Converter")

        self.addLabel(text = "Fahrenheit", row=0 ,column=0)
        self.fahrenheitDeg = self.addFloatField(
            value=0.0,
            row=1,
            column=0
        )

        self.addLabel(text="Celsius", row=0, column=3)
        self.celsiusDeg = self.addFloatField(
            value=0.0,
            row=1,
            column=3
        )

        self.addButton(
            text=">>>",
             row=3, 
             column=0, 
             columnspan=2, 
             command=self.convertToC
        )
        self.addButton(
             text="<<<",
             row=3,
             column=3,
             columnspan=2,
             command=self.convertToF
         )


    def convertToF(self):
        celsius = self.celsiusDeg.getNumber()
        fahrenheit = ((9*celsius)/5)+32
        self.fahrenheitDeg.setNumber(fahrenheit)
    
    def convertToC(self):
        fahrenheit = self.fahrenheitDeg.getNumber()
        celsius = ((fahrenheit-32)*5)/9
        self.celsiusDeg.setNumber(celsius)

Converter().mainloop()