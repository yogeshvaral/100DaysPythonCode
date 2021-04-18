from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project


def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = [random.choice(letters) for _ in range(nr_letters)] + \
                    [random.choice(symbols) for _ in range(nr_symbols)] + \
                    [random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    password_input.insert(0,password)
    print(f"Your password is: {password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(250, 250)
window.config(padx=50, pady=50)


def add_entry():
    website = website_input.get()
    email_id = email_input.get()
    password = password_input.get()
    output = f"{website} | {email_id} | {password}\n"
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("Please do not leave any of the fields empty")
    else:
        is_it_ok = messagebox.askyesno(title=website,message=f"These are the details entered: \n Email:{email_id} "
                                       f"\npassword :{password} \n is it ok to save?")
        if is_it_ok:
            with open("data.txt", mode="a") as file:
                file.write(output)
                website_input.delete(0, END)
                password_input.delete(0, END)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "yogeshvaralhdp@gmail.com")

password_label = Label(text="password")
password_label.grid(column=0, row=3)

password_input = Entry(width=17)
password_input.grid(column=1, row=3)

generate = Button(text="Generate Password", width=15,command=generate_password)
generate.grid(column=2, row=3)

add = Button(text="Add", width=30,command=add_entry)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
