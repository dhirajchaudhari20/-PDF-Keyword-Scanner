import tkinter as tk
from tkinter import filedialog, messagebox
import pdfreader

def browse_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if file_paths:
        file_list.delete(0, tk.END)
        for file_path in file_paths:
            file_list.insert(tk.END, file_path)

def search_keyword():
    keyword = keyword_entry.get()

    if not keyword:
        messagebox.showerror("Error", "Please enter a keyword.")
        return

    for file_path in file_list.get(0, tk.END):
        try:
            with open(file_path, 'rb') as f:
                pdf_reader = pdfreader.PdfReader(f)
                text = pdf_reader.pages[0].extract_text()

            if keyword in text:
                messagebox.showinfo("Success", f"Keyword '{keyword}' found in {file_path}.")
            else:
                messagebox.showinfo("No Results", f"Keyword '{keyword}' not found in {file_path}.")

        except Exception as e:
            messagebox.showerror("Error", f"Error processing PDF file: {e}")

# Create main window
root = tk.Tk()
root.title("PDF Keyword Search")

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
