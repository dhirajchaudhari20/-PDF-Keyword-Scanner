import os
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2  # Assuming PyPDF2 for PDF reading

def browse_files():
    """Opens a file dialog to select multiple PDF files."""
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if file_paths:
        file_list.delete(0, tk.END)
        for file_path in file_paths:
            file_list.insert(tk.END, file_path)

def search_keyword():
    """Searches for keywords in selected PDFs and generates an Excel sheet."""
    keyword = keyword_entry.get().strip()  # Remove leading/trailing whitespace

    if not keyword:
        messagebox.showerror("Error", "Please enter a keyword.")
        return

    try:
        # Create an Excel workbook and worksheet
        import openpyxl
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(["PDF File", "Keyword Found?"])  # Header row

        for file_path in file_list.get(0, tk.END):
            try:
                with open(file_path, 'rb') as f:
                    pdf_reader = PyPDF2.PdfReader(f)
                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text()

                if keyword.lower() in text.lower():  # Case-insensitive search
                    match_found = "Yes"
                else:
                    match_found = "No"

                ws.append([file_path, match_found])

                # Save the Excel workbook (optional prompt for location)
                save_location = filedialog.asksaveasfilename(
                    defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")]
                )
                if save_location:
                    wb.save(save_location)
                    messagebox.showinfo("Success", f"Results saved to '{save_location}'.")
                else:
                    messagebox.showinfo("Information", "Results not saved. You can copy and paste them manually.")

            except Exception as e:
                messagebox.showerror("Error", f"Error processing PDF file '{file_path}': {e}")

    except ImportError:
        messagebox.showerror("Error", "Please install the 'openpyxl' library using 'pip install openpyxl'.")

# Create main window
root = tk.Tk()
root.title("PDF Keyword Scanner")

# Create widgets
file_label = tk.Label(root, text="Select PDF Files:")
file_list = tk.Listbox(root, width=50)
browse_button = tk.Button(root, text="Browse", command=browse_files)

keyword_label = tk.Label(root, text="Enter Keyword:")
keyword_entry = tk.Entry(root, width=50)

search_button = tk.Button(root, text="Search", command=search_keyword)

# Grid layout
file_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
file_list.grid(row=0, column=1, padx=5, pady=5)
browse_button.grid(row=0, column=2, padx=5, pady=5)

keyword_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
keyword_entry.grid(row=1, column=1, padx=5, pady=5)

search_button.grid(row=2, columnspan=3, padx=5, pady=10)

# Run the application
root.mainloop()
