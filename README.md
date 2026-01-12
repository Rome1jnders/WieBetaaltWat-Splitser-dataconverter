# Splitser/WieBetaaltWat HTML to CSV Converter

This tool extracts transaction data from a **Splitser (WieBetaaltWat)** GDPR data export and saves it as a CSV file.

When you request your data under the GDPR (AVG), Splitser provides a `.zip` file containing an `index.html` file. While this file is readable in a browser, it is not structured for data analysis. This script parses the HTML and converts it into a clean spreadsheet.

## How to obtain your data for free

You do not need a Premium subscription to export your data. Under the GDPR, you have the right to access your data free of charge.

1.  **Request:** Contact [Splitser Support](support.wiebetaaltwat.nl) and request a full export of your personal data (GDPR/AVG request).
2.  **Download:** You will receive a link to a `.zip` file.
3.  **Extract:** Unzip the folder to find the `index.html` file.

## Usage

### 1. Install dependencies
This script requires `BeautifulSoup4` for parsing the HTML:

```bash
pip install beautifulsoup4
```

### 2. Configure the File Path
Before running the script, you must point it to the location of your index.html. Open the Python file and update the FILE_PATH variable:
python
#### Change this to the actual location of your index.html file
```bash
FILE_PATH = r'C:\vscodeProjects\klresearchtbvpotentiaal\models\base\index.html'
```

### 3. Run the script
bash
python converter.py
Wees voorzichtig met code.

### 4. Result
The script will generate a .csv file in the same directory, which can be opened in Excel or Google Sheets.
## How it works
The script targets the specific HTML table structures used in the Splitser export. It identifies rows and columns containing dates, descriptions, and amounts, ensuring that the data is flattened correctly into a CSV format.

## Disclaimer
This project is independent and not affiliated with Splitser or WieBetaaltWat. It is designed to help users exercise their right to data portability.
