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

        Label(self,
              text="Select an actor from each column",
              font=("Helvetica", 16),
              highlightbackground='#3E4149',
              ).grid(row=0, column=0, columnspan=2, sticky=W, pady=4)

        self.leftValue = tk.IntVar()
        self.rightValue = tk.IntVar()

        self.rdioOne = tk.Radiobutton(self, text='Scarlett Johansson',
                                      variable=self.leftValue, value=1)
        self.rdioTwo = tk.Radiobutton(self, text='Seth Rogen',
                                      variable=self.leftValue, value=2)
        self.rdioThree = tk.Radiobutton(self, text='Jennifer Lawrence',
                                        variable=self.leftValue, value=3)
        self.rdioFour = tk.Radiobutton(self, text='Mark Whalberg',
                                       variable=self.leftValue, value=4)
        self.rdioFive = tk.Radiobutton(self, text='Chis Evans',
                                       variable=self.leftValue, value=5)
        self.rdioSix = tk.Radiobutton(self, text='Tom Hanks',
                                      variable=self.leftValue, value=6)
        self.rdioSeven = tk.Radiobutton(self, text='Kate Hudson',
                                        variable=self.rightValue, value=7)
        self.rdioEight = tk.Radiobutton(self, text='Matthew McConaughey',
                                        variable=self.rightValue, value=8)
        self.rdioNine = tk.Radiobutton(self, text='Johnny Depp',
                                       variable=self.rightValue, value=9)
        self.rdioTen = tk.Radiobutton(self, text='Adam Sandler',
                                      variable=self.rightValue, value=10)
        self.rdioEleven = tk.Radiobutton(self, text='Bradley Cooper',
                                         variable=self.rightValue, value=11)
        self.rdioTwelve = tk.Radiobutton(self, text='Emma Stone',
                                         variable=self.rightValue, value=12)

        self.rdioOne.grid(column=0, row=1, sticky=W)
        self.rdioTwo.grid(column=0, row=2, sticky=W)
        self.rdioThree.grid(column=0, row=3, sticky=W)
        self.rdioFour.grid(column=0, row=4, sticky=W)
        self.rdioFive.grid(column=0, row=5, sticky=W)
        self.rdioSix.grid(column=0, row=6, sticky=W)

        self.rdioSeven.grid(column=1, row=1, sticky=W)
        self.rdioEight.grid(column=1, row=2, sticky=W)
        self.rdioNine.grid(column=1, row=3, sticky=W)
        self.rdioTen.grid(column=1, row=4, sticky=W)
        self.rdioEleven.grid(column=1, row=5, sticky=W)
        self.rdioTwelve.grid(column=1, row=6, sticky=W)

        Button(self,
               text='Submit',
               font=("Helvetica", 16),
               command=self.processRequest
               ).grid(row=9, column=0, sticky=NSEW, pady=4)

        self.msg2show = StringVar()
        Label(self,
              textvariable=self.msg2show
              ).grid(row=10, column=0, sticky=NSEW, pady=4)

    def processRequest(self):

        if self.leftValue.get() == 1:
            print("You selected Scarlet Johansson")
        elif self.leftValue.get() == 2:
            print("You selected Seth Rogan")
        elif self.leftValue.get() == 3:
            print("You selected Jennifer Lawrence")
        elif self.leftValue.get() == 4:
            print("You selected Mark Whalberg")
        elif self.leftValue.get() == 5:
            print("You selected Chis Evans")
        elif self.leftValue.get() == 6:
            print("You selected Tom Hanks")
        elif self.rightValue.get() == 7:
            print("You selected Kate Hudson")
        elif self.rightValue.get() == 8:
            print("You selected Matthew McConaughey")
        elif self.rightValue.get() == 9:
            print("You selected JohnnyDepp")




def main():
    root = Tk()
    root.title("BSSD 5410 Homework 5.2 MovieDB")
    root.geometry('350x300')
    app = Application(root)

    root.mainloop()


if __name__ == "__main__":
    main()
