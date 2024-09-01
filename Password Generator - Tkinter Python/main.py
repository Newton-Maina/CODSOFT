from tkinter import *
from tkinter import messagebox
import random
import string

def generate_password():
    password = length_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter your password length")
    length = int(length_entry.get())
    if length < 8:
        messagebox.showwarning('Warning', 'Password length must be at least 8 characters')
        return

    characters = ""
    if lower_var.get():
        characters += string.ascii_lowercase
    if upper_var.get():
        characters += string.ascii_uppercase
    if digits_var.get():
        characters += string.digits
    if special_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning('Generation Error', 'At least one character is required')
        return

    password = "".join(random.choice(characters) for _ in range(length))
    password_var.set(password)



def copy():
    password_window.clipboard_clear()
    password_window.clipboard_append(password_var.get())
    password_window.update()
    messagebox.showinfo('Copied', 'Password copied to clipboard')

password_window = Tk()
password_window.title('Password Generator')
password_window.geometry('500x500')
password_window.resizable(False, False)

header_frame = Frame(password_window, pady=20, bg="#2C3E50")
header_frame.pack(fill=X)
header_label = Label(header_frame, text='Password Generator', bg="#2C3E50", fg='white', font=('Helvetica', 20, 'bold'))
header_label.pack()

Label(password_window, text="Enter Desired Password Length:", font=("Helvetica",12, 'bold')).pack(pady=5)
length_entry = Entry(password_window, width=10, font=("Helvetica",12, 'bold ') ,bg="#ECF0F1", bd=2, relief=SUNKEN)
length_entry.pack(pady=10)

char_options_frame = Frame(password_window, bg="#34495E")
char_options_frame.pack()
char_options_label = Label(char_options_frame, text='Characters:', bg="#34495E", fg='white', font=("Helvetica",10, 'bold'))
char_options_label.grid(row=0, column=0, pady=7)

lower_var = BooleanVar(value=False)
Checkbutton(char_options_frame, text='Include Lowercase Letters', variable=lower_var, bg="#34495E", fg='white', selectcolor='#34495E', font=("Helvetica", 10)).grid(row=1, column=0, sticky=W)

upper_var = BooleanVar(value=False)
Checkbutton(char_options_frame, text='Include Uppercase Letters', variable=upper_var, bg="#34495E", fg='white', selectcolor='#34495E', font=("Helvetica", 10)).grid(row=2, column=0, sticky=W)

digits_var = BooleanVar(value=False)
Checkbutton(char_options_frame,text='Include Digits', variable=digits_var, bg="#34495E", fg='white', selectcolor='#34495E', font=("Helvetica", 10)).grid(row=3, column=0, sticky=W)

special_var = BooleanVar(value=False)
Checkbutton(char_options_frame,text='Include Special Characters', variable=special_var, bg="#34495E", fg='white', selectcolor='#34495E', font=("Helvetica", 10)).grid(row=4, column=0, sticky=W)

Button(password_window, text='Generate Password', command=generate_password, width=20, height=2, bg="#1ABC9C", fg='white', font=("Helvetica", 12, "bold"), bd=0, relief='ridge', activebackground="#16A085").pack(pady=10)

password_var = StringVar()
Entry(password_window, textvariable=password_var, width=40, font=("Helvetica",12), bg='#ECF0F1', bd=2, relief='sunken').pack(pady=10)

Button(password_window, text="Copy to Clipboard", command=copy, width=20, height=2, bg='#3498DB', fg='white',font=("Helvetica", 12, "bold"), bd=0, relief='ridge', activebackground="#2980B9").pack(pady=10)

password_window.mainloop()
