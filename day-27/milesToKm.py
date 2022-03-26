from tkinter import *

window = Tk()
window.title("Mile to KM converter")
window.minsize(width=500, height=500)

def calculate():
  milesInputValue = milesInput.get()
  km = int(milesInputValue) * 1.60934
  kmCalculated["text"] = km
  
milesInput = Entry(text="0")
isEqualTo = Label(text="is equal to")
milesLabel = Label(text = "Miles")
kmLabel = Label(text = "KM")
kmCalculated = Label(text = "0")
calculateButton = Button(text="Calculate", command = calculate)

milesInput.grid(column=2, row=1)
milesLabel.grid(column=3, row=1)

isEqualTo.grid(column=1, row=2)

kmCalculated.grid(column=2, row=2)
kmLabel.grid(column=3, row=2)

calculateButton.grid(column=2, row=34)

window.mainloop()