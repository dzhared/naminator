from tkinter import Tk, filedialog, END
from tkinter.ttk import Label, Entry, Button

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_path_text.delete(0, END)
    folder_path_text.insert(0, folder_path)

def browse_csv():
    csv_path = filedialog.askopenfilename()
    csv_path_text.delete(0, END)
    csv_path_text.insert(0, csv_path)

root = Tk()

root.configure(padx=20, pady=20)
root.title("Naminator")

# Labels
suffix_label = Label(text="Suffix: ", width=15, anchor="w")
suffix_label.grid(row=0, column=0)

csv_path_label = Label(text="CSV File Path: ", width=15, anchor="w")
csv_path_label.grid(row=1, column=0)

folder_path_label = Label(text="Folder Path: ", width=15, anchor="w")
folder_path_label.grid(row=2, column=0)

# Textboxes - Add functionality
suffix_text = Entry(width=5)
suffix_text.grid(row=0, column=1, sticky="w")

csv_path_text = Entry(width=30)
csv_path_text.grid(row=1, column=1, sticky="w")

folder_path_text = Entry(width=30)
folder_path_text.grid(row=2, column=1, sticky="w")

# Buttons - Add functionality
csv_path_browse = Button(text="Browse...", width=8, command=browse_csv)
csv_path_browse.grid(row=1, column=2)

folder_path_browse = Button(text="Browse...", width=8, command=browse_folder)
folder_path_browse.grid(row=2, column=2)

run_button = Button(text="Run", width=10, command=lambda: print("Button"))
run_button.grid(row=3, column=0, columnspan=2)

root.mainloop()
