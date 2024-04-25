
PDF Keyword Scanner

This Python script scans multiple PDFs for a specified keyword and generates an Excel sheet with the results.

Features:

Selects multiple PDF files using a file dialog.
Prompts the user to enter a keyword for searching.
Performs case-insensitive searches for the keyword within each PDF.
Creates an Excel sheet with columns for "PDF File" and "Keyword Found?"
Optionally prompts the user to save the results to an Excel file with a chosen location.
Requirements:

Python 3.x
PyPDF2 (pip install PyPDF2)
openpyxl (pip install openpyxl)
Instructions:

Clone or download this repository.
Install the required libraries:
Bash
pip install PyPDF2 openpyxl
Use code with caution.
content_copy
Run the script:
Bash
python pdf_keyword_scanner.py
Use code with caution.
content_copy
Usage:

The script will open a GUI window.

Click "Browse" to select multiple PDF files.

Enter the keyword you want to search for in the "Enter Keyword" box.

Click "Search" to start the search.

The script will process the selected PDFs and create an Excel sheet with the results.

If you choose to save the results, you will be prompted for a location.

Example Usage:

Select three PDFs containing different text.
Enter a keyword that exists in two of the PDFs.
Click "Search".
The script will generate an Excel sheet with entries like:

PDF File	Keyword Found?
/path/to/first_pdf.pdf	No
/path/to/second_pdf.pdf	Yes
/path/to/third_pdf.pdf	Yes

drive_spreadsheet
Export to Sheets
Contribution:

Feel free to fork this repository and make improvements!

License:

This script is provided under the MIT License (see LICENSE file for details).
