import openpyxl
import matplotlib.pyplot as plt

# Specify the path to your Excel file
excel_file_path = 'C:/Users/singh/Desktop/Book1.xlsx'

# Load the Excel workbook
workbook = openpyxl.load_workbook(excel_file_path)

# Assuming your Excel sheet is named 'Sheet1'
sheet = workbook['Sheet1']

# Take input from the user for the starting and ending rows
start_row = int(input("Enter the starting row: "))
end_row = int(input("Enter the ending row: "))

# Initialize lists to store data for the line plot
x_values = list(range(1, end_row - start_row + 2))
y_values = []

# Iterate through rows and append values to the y_values list
for row_num in range(start_row, end_row + 1):
    # Assuming the first column contains the y-axis values for the line plot
    y_values.append(sheet.cell(row=row_num, column=1).value)

# Check if x_values and y_values have the same size
if len(x_values) != len(y_values):
    print("Error: x_values and y_values must have the same size.")
else:
    # Plotting a line graph
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, color='blue', linestyle='-', marker='o')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('Line Graph from Excel Data')
    plt.grid(True)
    plt.tight_layout()

    # Show the plot
    plt.show()

taversal
insertion
UPDTION 
DELETION
