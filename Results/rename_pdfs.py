import os
import openpyxl

def list_files_to_excel(directory_path):
    # Create a new workbook and select the active sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "File List"

    # Add a header
    sheet['A1'] = "File Name"

    # Get all files in the directory
    files = os.listdir(directory_path)

    # Write file names to Excel
    for index, file_name in enumerate(files, start=2):  # Start from row 2
        sheet[f'A{index}'] = file_name

    # Save the workbook
    excel_file_name = "file_list.xlsx"
    workbook.save(excel_file_name)
    print(f"File list has been saved to {excel_file_name}")

# Replace this with your directory path
directory_path = r"D:\Desktop\Trash\ResultAuto\Results"

list_files_to_excel(directory_path)