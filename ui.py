from tkinter import Tk, Label, Text, Button

FONT = ("Courier", 12)

root = Tk()

root.configure(padx=20, pady=20)
root.title("Naminator")

# Labels
suffix_label = Label(text="Suffix: ", font=FONT, width=15, anchor="w")
suffix_label.grid(row=0, column=0)

csv_path_label = Label(text="CSV File Path: ", width=15, font=FONT, anchor="w")
csv_path_label.grid(row=1, column=0)

folder_path_label = Label(text="Folder Path: ", width=15, font=FONT, anchor="w")
folder_path_label.grid(row=2, column=0)

# Textboxes - Add functionality
suffix_text = Text(font=FONT, height=1, width=5)
suffix_text.grid(row=0, column=1, sticky="w")

csv_path_text = Text(font=FONT, height=1, width=30)
csv_path_text.grid(row=1, column=1, sticky="w")

folder_path_text = Text(font=FONT, height=1, width=30)
folder_path_text.grid(row=2, column=1, sticky="w")

# Buttons - Add functionality
csv_path_browse = Button(text="Browse...", font=FONT, width=8, command=lambda: print("Browse for CSV"))
csv_path_browse.grid(row=1, column=2)

folder_path_browse = Button(text="Browse...", font=FONT, width=8, command=lambda: print("Browse for folder"))
folder_path_browse.grid(row=2, column=2)

run_button = Button(text="Run", font=FONT, anchor="center", width=10, command=lambda: print("Button"))
run_button.grid(row=3, column=0, columnspan=2)

root.mainloop()
