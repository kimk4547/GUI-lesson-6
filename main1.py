from tkinter import *

import tkinter.font as font

root = Tk()

root.geometry('500x250')

root.title("Celsius to Fahrenheit Converter")

def convert():
    celsius = (temp_entry.get())
    if(celsius.replace('.', "").isnumeric()):
        invalid_label.grid_forget()
        fahrenheit = (float(celsius) * 9/5) + 32
        output_label.config(text = "Temperature in Fahrenheit : " + str(fahrenheit))
    else:
        invalid_label.grid(row = 1, column = 1)


title = Label(root, text = "Celsius --> Fahrenheit", font = font.Font(size = 20), fg = 'grey')

title.pack()

frame = Frame(root)

frame.pack(pady = 20)

temp_label = Label(frame, text = "Enter Temperature in Celsius  :  ", font = font.Font(size = 10))

temp_label.grid(row = 0, column = 0)

temp_entry = Entry(frame, width = 10)

temp_entry.grid(row = 0, column = 1)

invalid_label = Label(frame, text = "-- please enter valid input --", font = font.Font(size = 6), fg = 'red')

output_label = Label(frame, font = font.Font(size = 12))

output_label.grid(row = 2, column = 0, columnspan = 2, pady = 10)

convert_btn = Button(frame, text = "Convert", width = 30, fg = 'black', bg = 'green', command = convert)

convert_btn.grid(row = 3, column = 0, columnspan = 2, pady = 10)

root.mainloop()