from tkinter import *
import tkinter as tk
from tkinter import ttk


# class RadioButtonDemo(Frame):
class Application(Frame):
    """When the Display button is pressed, shows the label
    of the selected radio button.  The button group has a
    horizontal alignment."""

    # def __init__(self):
    #     """Sets up the window and widgets."""
    #     #Frame.__init__(self, "Radio Button Demo")
    #     Frame.__init__(self)
    #     #super(Application, self).__init__(master)

    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Add the button group

        # SCARLETT_ID = "1245"  # Scarlett Johansson
        # BRADLEY_ID = "51329"  # Bradley Cooper
        # JENNIFER_ID = "72129"  # Jennifer Lawrence
        # WHALB_ID = "13240"  # Mark Whalberg
        # CHRIS_ID = "16828"  # Chis Evans
        # TOM_ID = "31"  # Tom Hanks
        # KATE_ID = "11661"  # Kate Hudson
        # MATTHEW_ID = "10297"  # Matthew McConaughey
        # JOHNNY_ID = "85" # Johnny Depp
        # ADAM_ID = "19292" # Adam Sandler
        # SETH_ID = "19274  # Seth Rogen
        # EMMA_ID = "53693" # Emma Stone

        leftValue = tk.IntVar()
        rightValue = tk.IntVar()

        self.rdioOne = tk.Radiobutton(self, text='Scarlett Johansson',
                                      variable=leftValue, value=1)
        self.rdioTwo = tk.Radiobutton(self, text='Bradley Cooper',
                                      variable=leftValue, value=2)
        self.rdioThree = tk.Radiobutton(self, text='Jennifer Lawrence',
                                        variable=leftValue, value=3)
        self.rdioFour = tk.Radiobutton(self, text='Mark Whalberg',
                                       variable=leftValue, value=4)
        self.rdioFive = tk.Radiobutton(self, text='Chis Evans',
                                       variable=leftValue, value=5)
        self.rdioSix = tk.Radiobutton(self, text='Tom Hanks',
                                      variable=leftValue, value=6)
        self.rdioSeven = tk.Radiobutton(self, text='Kate Hudson',
                                        variable=rightValue, value=7)
        self.rdioEight = tk.Radiobutton(self, text='Matthew McConaughey',
                                        variable=rightValue, value=8)
        self.rdioNine = tk.Radiobutton(self, text='Johnny Depp',
                                       variable=rightValue, value=9)
        self.rdioTen = tk.Radiobutton(self, text='Adam Sandler',
                                      variable=rightValue, value=10)
        self.rdioEleven = tk.Radiobutton(self, text='Seth Rogen',
                                         variable=rightValue, value=11)
        self.rdioTwelve = tk.Radiobutton(self, text='Emma Stone',
                                         variable=rightValue, value=12)

        self.rdioOne.grid(column=0, row=0)
        self.rdioTwo.grid(column=0, row=1)
        self.rdioThree.grid(column=0, row=2)
        self.rdioFour.grid(column=0, row=3)
        self.rdioFive.grid(column=0, row=4)
        self.rdioSix.grid(column=0, row=5)

        self.rdioSeven.grid(column=1, row=0)
        self.rdioEight.grid(column=1, row=1)
        self.rdioNine.grid(column=1, row=2)
        self.rdioTen.grid(column=1, row=3)
        self.rdioEleven.grid(column=1, row=4)
        self.rdioTwelve.grid(column=1, row=5)


# main
def main():
    root = Tk()
    root.title("BSSD 5410 Homework 5.2 Scott Bing")
    root.geometry('350x300')
    app = Application(root)

    root.mainloop()


if __name__ == "__main__":
    main()
