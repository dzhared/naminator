import os
import pandas

PROJECT_SUFFIX = "6935"

df = pandas.read_csv("reference.csv")
folder_files = os.listdir("files-reference")
csv_prefixes = df['prefix'].values
# print(csv_prefixes)
# print(folder_files)

# Check if prefix (e.g. 1234) is valid
def check_prefix(filename: str):
    try:
        int(filename[:5])
    except ValueError:
        return False
    else:
        return True

# Check if suffix (e.g. 10310) is valid
def check_suffix(filename: str):
    if filename[-8:][:4] == PROJECT_SUFFIX:
        return True
    else:
        return False

# FORMAT: 00000 - 00-NN000 NNNNNNNNNN - 0000.pdf
# Retrieve data row by prefix value. Do this for sheets
# that have been verified to have "12345 - " prefix and
# " - 6789.pdf" suffix.

# Retrieves, returns row from dataframe by sheet prefix
def row_by_prefix(prefix: int):
    return df.loc[df['prefix'] == prefix]

# Constructs, returns correct file name from row (combine w/ row_by_prefix?)
def concat(row):
    prefix = row['prefix'].values[0]
    sheet_num = row['sheet_num'].values[0]
    sheet_name = row['sheet_name'].values[0]
    suffix = row['suffix'].values[0]

    full_name = f"{prefix} - {sheet_num} {sheet_name} - {suffix}.pdf"
    return full_name

# Checks if file's name matches with correct filename according to CSV
def check_against_csv(filename: str):
    file_prefix = int(filename[:5])
    csv_row = row_by_prefix(file_prefix)
    csv_name = concat(csv_row)
    if filename == csv_name:
        return True
    else:
        return False

def sort(folder_files: list):
    # Retrieve all filenames from given folder
    for filename in folder_files:
        # Check if prefix and suffix both match
        if check_prefix(filename) and check_suffix(filename) and check_against_csv(filename):
            print(f"OK:         {filename}")
            # Check against CSV
            # check_against_csv(file)
        elif not check_prefix(filename) and not check_suffix(filename):
            print(f"BAD PF/SF:  {filename}")
        elif not check_prefix(filename):
            print(f"BAD PREFIX: {filename}")
        elif not check_suffix(filename):
            print(f"BAD SUFFIX: {filename}")
        else:
            print(f"BAD OTHER:  {filename}")

# Import list of files from folder
# Check 1: prefix formatting
# Check 2: suffix formatting
# If clears both checks:

sort(folder_files)

