import openpyxl

# Specify the path to your Excel file
excel_file_path = 'C:/Users/singh/Desktop/Book1.xlsx'

# Load the Excel workbook
workbook = openpyxl.load_workbook(excel_file_path)

# Assuming your Excel sheet is named 'Sheet1'
sheet = workbook['Sheet1']

# Take input from the user for the starting and ending rows
start_row = int(input("Enter the starting row: "))
end_row = int(input("Enter the ending row: "))

# Iterate through rows and print values in all columns
for row_num, row in enumerate(sheet.iter_rows(min_row=start_row, max_row=end_row, values_only=True), start=1):
    for value in row:
        print(value, end=' ')
    print()  # Move to the next line for the next row
