import openpyxl

# Specify the path to your Excel file
excel_file_path = 'C:/Users/singh/Desktop/DATABASE.xlsx'

# Open the workbook
workbook = openpyxl.load_workbook(excel_file_path)

# Select the active sheet (assuming it's the first sheet)
sheet = workbook.active

# Iterate through rows and print values in columns A and B
for row in sheet.iter_rows(min_row=4, max_row=5, values_only=True):
    for value in row:
        print(value, end=' ')
    print()  # Move to the next line for the next row
