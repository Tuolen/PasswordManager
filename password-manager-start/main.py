import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- DATABASE ----------------------------------------#
def search_pressed():
    website = first_entry.get().title()
    if len(website) == 0:
        messagebox.showerror(title="Empty", message="Website entry shouldn't be empty")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                email_info = data[website]["Email"]
                password_info = data[website]["Password"]
        except FileNotFoundError:
            messagebox.showwarning(title="Oops", message="There is not data added yet")
        except KeyError:
            messagebox.showwarning(title="Error", message="Sorry, there is no data for this website")
        else:
            messagebox.showinfo(title=website, message=f"Email: {email_info}\n\nPassword:{password_info}")
            pyperclip.copy(password_info)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generator():
    third_entry.delete(0, tkinter.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = []

    password_list.extend(password_letters)
    password_list.extend(password_symbols)
    password_list.extend(password_numbers)

    random.shuffle(password_list)

    generated_password = "".join(password_list)

    third_entry.insert(tkinter.END, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def delete():
    first_entry.delete(0, tkinter.END)
    third_entry.delete(0, tkinter.END)


def save():
    website = first_entry.get().title()
    email = second_entry.get()
    password = third_entry.get()
    new_data = {website: {
        "Email": email,
        "Password": password
    }}
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Entry field should not be empty")
    try:
        with open("data.json", "r") as the_file:
            data = json.load(the_file)
    except FileNotFoundError:
        the_file = open("data.json", "w")
        data = json.load(the_file)
        if website in data:
            change = messagebox.askyesno(title="Error", message="Are you sure you want to change the password")
            if change:
                try:
                    with open("data.json", "r") as the_file:
                        data = json.load(the_file)
                except FileNotFoundError:
                    the_file = open("data.json", "w")
                    json.dump(new_data, the_file, indent=4)
                    the_file.close()
                else:
                    with open("data.json", "w") as the_file:
                        data.update(new_data)
                        json.dump(data, the_file, indent=4)
        else:
            try:
                with open("data.json", "r") as the_file:
                    data = json.load(the_file)
            except FileNotFoundError:
                the_file = open("data.json", "w")
                json.dump(new_data, the_file, indent=4)
                the_file.close()
            else:
                with open("data.json", "w") as the_file:
                    data.update(new_data)
                    json.dump(data, the_file, indent=4)
    delete()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("My Pass")
window.config(padx=50, pady=50)

image = tkinter.PhotoImage(file="logo.png")
canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 95, image=image)
canvas.grid(row=0, column=2)

website_label = tkinter.Label(text="Website:", font=("Arial", 12))
website_label.grid(row=1, column=1)

email_label = tkinter.Label(text="Email/Username:", font=("Arial", 12))
email_label.grid(row=2, column=1)

password_label = tkinter.Label(text="Password:", font=("Arial", 12))
password_label.grid(row=3, column=1)

first_entry = tkinter.Entry(width=32)
first_entry.grid(row=1, column=2)
first_entry.focus()

second_entry = tkinter.Entry(width=45)
second_entry.insert(tkinter.END, "Yazan_Masalha@yahoo.com")
second_entry.grid(row=2, column=2, columnspan=2)

third_entry = tkinter.Entry(width=30)
third_entry.grid(row=3, column=2)

generate_button = tkinter.Button(text="Generator", width=9, command=generator)
generate_button.grid(row=3, column=3)

add_button = tkinter.Button(text="Add", width=38, command=save)
add_button.grid(row=4, column=2, columnspan=2)

search_button = tkinter.Button(text="Search", width=10, command=search_pressed)
search_button.grid(row=1, column=3)

window.mainloop()
