import os
import csv

folder_files = os.listdir("files-reference")

# TODO: Check if prefix is valid

def check_prefix(filename: str):
    try:
        int(filename[:5])
    except ValueError:
        return False
    else:
        return True

# TODO: Check if suffix is valid

def check_suffix(filename: str, suffix):
    if filename[-8:][:4] == f"{suffix}": # Will accept int or str input
        return True
    else:
        return False

# TODO: Concatenate filename from CSV

def concat(file):
    file_list = []
    with open(file, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvreader:
            file_list.append(f"{row[0]} - {row[1]} {row[2]} - {row[3]}.pdf")
    file_list = file_list[1:]
    return file_list

# TODO: Find matching sheet by file number

print(folder_files)

def check_against_csv(file_list, file_folder):
    for file in file_list:
        prefix = file[:5]
        for pdf_file in file_folder:
            if file == pdf_file:
                print(f"Match: {file}")
                break
            else:
                print(f"No match: {file}")

file_list = concat('reference.csv')
check_against_csv(file_list, folder_files)

