import os

def rename_pdfs_in_current_directory():
    current_directory = r"D:\Desktop\Trash\ResultAuto\Results"
    print(f"Current directory: {current_directory}")
    
    print("All files in directory:")
    for file in os.listdir(current_directory):
        print(file)
    
    pdf_files = [f for f in os.listdir(current_directory) if f.startswith("result_") and f.endswith(".pdf")]
    print(f"PDF files to rename: {pdf_files}")
    
    for filename in pdf_files:
        new_name = filename.replace("result_", "", 1)
        old_file = os.path.join(current_directory, filename)
        new_file = os.path.join(current_directory, new_name)
        try:
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} to {new_file}')
        except Exception as e:
            print(f"Error renaming {old_file}: {str(e)}")

if __name__ == "__main__":
    rename_pdfs_in_current_directory()