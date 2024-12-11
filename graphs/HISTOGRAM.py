import openpyxl
import matplotlib.pyplot as plt

excel_file_path = 'C:/Users/singh/Desktop/Book1.xlsx'

workbook = openpyxl.load_workbook(excel_file_path)

sheet = workbook['Sheet1']

start_row = int(input("Enter the starting row: "))
end_row = int(input("Enter the ending row: "))

data = []

for row in sheet.iter_rows(min_row=start_row, max_row=end_row, values_only=True):
    data.extend(row)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram from Excel Data')
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()

plt.show()
