import tkinter as tk
from tkinter import messagebox

class LibraryGUI:
    def __init__(self, master,file_name):

        self.file_name = file_name
        try:
            self.file = open(self.file_name, "a+")
        except FileNotFoundError:
            self.file = open(self.file_name, "a+")

        self.master = master
        master.title("Library Management System")
        master.geometry("1100x350+250+150")
        master.resizable(False, False)

        # Added Buttons 
        self.add_button = tk.Button(master,text="Add Book",width=12, height=1,fg="black",bg="#bdbdbd", font="Times 15 bold", command=self.add_book)
        self.add_button.place(x=50,y=50)

        self.remove_button = tk.Button(master, text="Remove Book",width=12, height=1,fg="black",bg="#bdbdbd", font="Times 15 bold", command=self.remove_book)
        self.remove_button.place(x=50,y=100)

        self.list_button = tk.Button(master, text="List Book",width=12, height=1,fg="black",bg="#bdbdbd", font="Times 15 bold", command=self.list_book)
        self.list_button.place(x=50,y=150)

        self.exit_button = tk.Button(master, text="Exit System",width=12, height=1,fg="black",bg="#bdbdbd", font="Times 15 bold", command=self.exit_system)
        self.exit_button.place(x=50,y=200)

        # Added  Text Fields and Entries
        self.book_entry_label_name = tk.Label(master, text="Enter Book Name",font=('Times', 10))
        self.book_entry_label_name.place(x=220,y=35)

        self.book_entry_name = tk.Entry(master, width=20, font=("Times",15))
        self.book_entry_name.place(x=220,y=55) 

        self.book_entry_label_author = tk.Label(master, text="Enter Book Author",font=('Times', 10))
        self.book_entry_label_author.place(x=430,y=35)

        self.book_entry_author = tk.Entry(master, width=20, font=("Times",15))
        self.book_entry_author.place(x=430,y=55) 

        self.book_entry_label_date = tk.Label(master, text="Enter Book Release Date",font=('Times', 10))
        self.book_entry_label_date.place(x=640,y=35)

        self.book_entry_date = tk.Entry(master, width=20, font=("Times",15))
        self.book_entry_date.place(x=640,y=55)

        self.book_entry_label_page = tk.Label(master, text="Enter Book Page",font=('Times', 10))
        self.book_entry_label_page.place(x=850,y=35)

        self.book_entry_page = tk.Entry(master, width=20, font=("Times",15))
        self.book_entry_page.place(x=850,y=55)

        self.book_entry_label_remove = tk.Label(master, text="Enter Book Name",font=('Times', 10))
        self.book_entry_label_remove.place(x=220,y=92)

        self.book_entry_remove = tk.Entry(master, width=20, font=("Times",15))
        self.book_entry_remove.place(x=220,y=113)


    def __del__(self):
        self.file.close()

    # Added  Function 
    def add_book(self):
        book_name = self.book_entry_name.get()
        book_author = self.book_entry_author.get()
        book_date = self.book_entry_date.get()
        book_page = self.book_entry_page.get()

        if book_name and book_author and book_date and book_page:
            control = False
            try:
                book_page = int(book_page)
                control = True
            except ValueError:
                self.book_entry_page.delete(0, tk.END)
                messagebox.showerror("Error","Page number must be an number")
            if control:
                book_data = f"{book_name}, {book_author}, {book_date}, {book_page}\n"
                with open("book.txt", "a+") as file:
                    file.write(book_data)
                messagebox.showinfo("Success", "Book added successfully!")
                self.book_entry_name.delete(0, tk.END)
                self.book_entry_author.delete(0, tk.END)
                self.book_entry_date.delete(0, tk.END)
                self.book_entry_page.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter information for book")

    def list_book(self):
        with open(self.file_name, "r") as file:
            book_list = file.read().splitlines()
        if book_list:
            book_info_list = ""
            for line in book_list:
                book_info = line.strip().split(",")
                book_name = book_info[0]
                author = book_info[1]
                book_date = book_info[2]
                book_page = book_info[3]
                book_info_list += f"Book name: {book_name}, Author name: {author} \n"
            messagebox.showinfo("Book List", book_info_list)
        else:
            messagebox.showinfo("Add Book!.")


    def remove_book(self):
        book_name = self.book_entry_remove.get()
        if book_name:
            with open(f"{self.file_name}", "r") as file:
                lines = file.readlines()
            with open(f"{self.file_name}", "w") as file:
                for line in lines:
                    if not line.strip("\n").startswith(f"{book_name}"):
                        file.write(line)
            messagebox.showinfo("Book removed successfully!")
            self.book_entry_name.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a book name.")

    def exit_system(self):
        self.master.destroy()

root = tk.Tk()
root.configure(bg='light blue')
lib = LibraryGUI(root,"book.txt")
root.mainloop()
