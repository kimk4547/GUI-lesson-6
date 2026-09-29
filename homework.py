from tkinter import *

import tkinter.font as font

root = Tk()

root.geometry('500x250')

root.title("USD to INR Converter")

def convert():
    usd = (money_entry.get())
    if(usd.replace('.', "").isnumeric()):
        invalid_label.grid_forget()
        inr = (float(usd)*83.20) 
        output_label.config(text = " INR : " + str(inr))
    else:
        invalid_label.grid(row = 1, column = 1)


title = Label(root, text = "usd --> inr", font = font.Font(size = 20), fg = 'grey')

title.pack()

frame = Frame(root)

frame.pack(pady = 20)

money_label = Label(frame, text = "Enter money in USD  :  ", font = font.Font(size = 10))

money_label.grid(row = 0, column = 0)

money_entry = Entry(frame, width = 10)

money_entry.grid(row = 0, column = 1)

invalid_label = Label(frame, text = "-- please enter valid input --", font = font.Font(size = 6), fg = 'red')

output_label = Label(frame, font = font.Font(size = 12))

output_label.grid(row = 2, column = 0, columnspan = 2, pady = 10)

convert_btn = Button(frame, text = "Convert", width = 30, fg = 'black', bg = 'green', command = convert)

convert_btn.grid(row = 3, column = 0, columnspan = 2, pady = 10)

root.mainloop()