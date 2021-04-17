from tkinter import *

window = Tk()
window.minsize(500, 500)
window.config(padx=10, pady=20)


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_lable.config(text=new_text)


# Lable
my_lable = Label(text="I am a lebel", font=("Arial", 24, "bold"))
my_lable.config(text="new Text")
my_lable.grid(column=0, row=0)

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# Button
button2 = Button(text="Click me2", command=button_clicked)
button2.grid(column=2, row=0)

# Ebntry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()
