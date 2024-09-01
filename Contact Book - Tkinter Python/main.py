import os
from tkinter import *
from tkinter import messagebox, simpledialog

CONTACT_FILE = "contacts.txt"
contacts = []
next_id = 1


contact_window = Tk()
contact_window.title('Contact Book')
contact_window.geometry('500x600')
contact_window.resizable(False, False)


def load_contacts():
    global next_id
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'r') as file:
            for line in file:
                contact_id, name, email, phone, address = line.strip().split('|')
                contacts.append({'id':int(contact_id), 'name':name, 'email':email, 'phone':phone, 'address':address })
                next_id = int(contact_id) +1
            refresh()

def save_contacts():
    with open(CONTACT_FILE, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['id']}|{contact['name']}|{contact['email']}|{contact['phone']}|{contact['address']}\n")


def refresh():
    contact_listbox.delete(0, END)
    for contact in contacts:
        contact_listbox.insert(END, f"{contact['id']}: {contact['name']}, {contact['email']}, {contact['phone']}, {contact['address']}")

def add_contact():
    global next_id
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name and not phone:
        messagebox.showwarning('Input Error', 'Please fill all fields - Name and Phone number required')
        return

    if name in contacts:
        messagebox.showwarning('Warning', 'Contact already exists')
        return

    contacts.append({'id': next_id, 'name': name, 'email': email, 'phone': phone, 'address': address})
    next_id += 1
    refresh()
    save_contacts()
    clear_entries()

def clear_entries():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)

def search_contact():
    query = search_entry.get().strip().lower()
    results = [contact for contact in contacts if query in contact['name'].lower() or query in contact['phone']]
    if results:
        result_text = "\n".join([f"{c['id']}: {c['name']}, {c['phone']}, {c['email']}, {c['address']} " for c in results])
        messagebox.showinfo('Contact Found', result_text)
    else:
        messagebox.showwarning('Error', 'Contact not found')
    search_entry.delete(0, END)

def delete_contact():
    selected_contact = contact_listbox.get(ACTIVE)
    if not selected_contact:
        messagebox.showwarning('Error', 'Select contact first')
        return

    contact_id = int(selected_contact.split(" - ")[0])
    if messagebox.askyesno('Confirm Delete', 'Are you sure you want to delete this contact?'):
        for contact in contacts:
            if contact['id'] == contact_id:
                contacts.remove(contact)
                refresh()
                save_contacts()
                break

def update_contact():
    selected_contact = contact_listbox.get(ACTIVE)
    if not selected_contact:
        messagebox.showwarning('Error', 'Select contact first')
        return

    contact_id = int(selected_contact.split(" - ")[0])
    for contact in contacts:
        if contact['id'] == contact_id:
            phone_update = simpledialog.askstring("Update Phone", f"Enter new phone number for {contact['name']}:")
            email_update = simpledialog.askstring('Update Email', f'Enter new email address for {contact['name']}:')
            address_update = simpledialog.askstring('Update Address', f'Enter new address for {contact['name']}:')

            if phone_update and email_update and address_update:
                contact['phone'] = phone_update
                contact['email'] = email_update
                contact['address'] = address_update

            refresh()
            save_contacts()
            break


header_section = Frame(contact_window , pady=10, bg="#4A90E2")
header_section.pack(fill="x")

header_label = Label(header_section, text="Contact Book", bg="#4A90E2", fg="white", font=("Helvetica", 10, "bold"))
header_label.pack(side="left")

form_frame = Frame(contact_window , padx=20, pady=20)
form_frame.pack(pady=10)

Label(form_frame, text="Name").grid(row=0, column=0, sticky=W)
name_entry = Entry(form_frame, bg="#4A90E2")
name_entry.grid(row=0, column=1,pady=5)

Label(form_frame, text="Phone").grid(row=1, column=0, sticky=W)
phone_entry = Entry(form_frame, bg="#4A90E2")
phone_entry.grid(row=1, column=1, pady=5)

Label(form_frame, text="Email").grid(row=2, column=0, sticky=W)
email_entry = Entry(form_frame, bg="#4A90E2")
email_entry.grid(row=2, column=1, pady=5)

Label(form_frame, text="Address").grid(row=3, column=0, sticky=W)
address_entry = Entry(form_frame, bg="#4A90E2")
address_entry.grid(row=3, column=1,pady=5)


button_frame = Frame(contact_window , pady=10)
button_frame.pack()

add_button = Button(button_frame, text="Add Contact", command=add_contact , width=15, bg="#4A90E2", fg="white", font=("Helvetica", 10, "bold"))
add_button.grid(row=0, column=0, padx=5, pady=5)

delete_button = Button(button_frame, text="Delete Contact", command=delete_contact, width=15, bg="#4A90E2", fg="white", font=("Helvetica", 10, "bold"))
delete_button.grid(row=0, column=1, padx=5, pady=5)

update_button = Button(button_frame, text="Update Contact", command=update_contact, width=15, bg="#4A90E2", fg="white", font=("Helvetica", 10, "bold"))
update_button.grid(row=0, column=2, padx=5, pady=5)


search_frame = Frame(contact_window , pady=20)
search_frame.pack()

Label(search_frame, text="Search By Name:", font=("Helvetica", 10)).pack(side="left", padx=10)
search_entry = Entry(search_frame, bg="#4A90E2", width=30, font=("Helvetica", 10))
search_entry.pack(side='left', padx=10)
Button(search_frame, text="Search", command=search_contact, width=10, bg="#2196F3", fg='white', font=('Helvetica',10,"bold")).pack(side='left')


listbox_frame = Frame(contact_window ,pady=10)
listbox_frame.pack(expand=True)

contact_listbox = Listbox(listbox_frame, width=60, height=15, bd=0, font=("Helvetica", 10))
contact_listbox.pack(pady=10, expand=True)

load_contacts()

contact_window.mainloop()