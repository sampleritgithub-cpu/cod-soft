import tkinter as tk
from tkinter import simpledialog, messagebox

class SimpleContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Contact Book")
        self.contacts = {}
        self.create_widgets()

    def create_widgets(self):
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)
        
        self.view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=5)
        
        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)
        
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact's name:")
        if name:
            phone = simpledialog.askstring("Input", f"Enter {name}'s phone number:")
            if phone and phone.isdigit() and len(phone) == 10:
                self.contacts[name] = phone
                messagebox.showinfo("Info", f"Contact {name} added successfully!")
            else:
                messagebox.showwarning("Warning", "Phone number must be 10 digits long and contain only numbers!")
        else:
            messagebox.showwarning("Warning", "Name cannot be empty!")

    def view_contacts(self):
        if self.contacts:
            contacts_info = "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])
            messagebox.showinfo("Contacts", contacts_info)
        else:
            messagebox.showinfo("Contacts", "No contacts available!")

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter contact's name to delete:")
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Info", f"Contact {name} deleted successfully!")
        else:
            messagebox.showwarning("Warning", "Contact not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleContactBook(root)
    root.mainloop()
