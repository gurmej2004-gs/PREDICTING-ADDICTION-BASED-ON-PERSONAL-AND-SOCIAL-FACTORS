import openpyxl
import matplotlib.pyplot as plt

excel_file_path = 'C:/Users/singh/Desktop/Book1.xlsx'

workbook = openpyxl.load_workbook(excel_file_path)

sheet = workbook['Sheet1']

start_row = int(input("Enter the starting row: "))
end_row = int(input("Enter the ending row: "))

categories = []
values = []

for row in sheet.iter_rows(min_row=start_row, max_row=end_row, values_only=True):
    category = row[0]
    numeric_values = [value for value in row[1:] if isinstance(value, (int, float))]
    value = sum(numeric_values) if numeric_values else 0

    categories.append(category)
    values.append(value)

plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='purple')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph from Excel Data')
plt.xticks(rotation=45) 
plt.tight_layout()

plt.show()
