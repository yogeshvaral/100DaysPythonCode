from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(500, 500)
window.config(padx=10, pady=20)


def miles_to_km():
    new_text = str(int(input.get()) * 1.6)
    result_lable.config(text=new_text)

# Lable
my_lable = Label(text="is equal to ", font=("Arial", 24))
my_lable.grid(column=0, row=1)

miles_lable = Label(text="Miles ", font=("Arial", 24))
miles_lable.grid(column=2, row=0)

km_lable = Label(text="KM ", font=("Arial", 24))
km_lable.grid(column=2, row=1)

result_lable = Label(text="0", font=("Arial", 24))
result_lable.grid(column=1, row=1)

# Button
button = Button(text="Calculate ", command=miles_to_km)
button.grid(column=1, row=2)

# Ebntry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)



window.mainloop()
