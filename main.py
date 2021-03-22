import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import turtle
a = 5
a += 100


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# print(f"Your password is: {password}")

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for char in range(nr_letters)]
    symbol_list = [random.choice(symbols) for char in range(nr_symbols)]
    number_list = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SEARCH WEBSITE ______________________________ #

def search_website():
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Database is empty", message="Please fill the databse then search")
    else:
        try:
            data_dict = data[website_entry.get()]
        except KeyError:
            messagebox.showerror(title="Error", message="Website not found, please enter a valid website name.")
        else:
            messagebox.showinfo(title=website_entry.get(),
                                message=f"Email:{data_dict['email']}\nPassword:{data_dict['password']}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Fields left empty",
                            message="some fields are left empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Are you sure the details are entered correctly: \nEmail:{email}\nPassword:{password}")

        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)

                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pass")
window.config(padx=20, pady=20, bg="black")

canvas = Canvas(width=200, height=200)
# canvas.config(padx=20)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.config(bg="black", highlightthickness=0)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.config(bg="black", fg="white")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.config(bg="black", fg="white")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.config(bg="black", fg="white")
password_label.grid(column=0, row=3)

website_entry = Entry(width=21,bg="black", fg="white" )
website_entry.focus()
website_entry.grid(column=1, row=1)

email_username_entry = Entry(width=35, bg="black", fg="white")
email_username_entry.insert(0, "tanishyelgoe604@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21, show="*",bg="black", fg="white")
password_entry.grid(column=1, row=3)
import 
add_button = Button(text="Add", width=33, command=save_password,bg="black", fg="white" )
add_button.grid(column=1, row=4, columnspan=2)

generate_password_button = Button(
    text="Generate Pass", width=11, command=generate_password,bg="black", fg="white" )
generate_password_button.grid(column=2, row=3)

# Search Button
search_button = Button(text="Search", width=11, command=search_website, bg="black", fg="white")
search_button.grid(column=2, row=1)

window.mainloop()
