import csv
from bs4 import BeautifulSoup
import os

# SET YOUR ABSOLUTE PATH HERE
# Note: Use forward slashes (/) or double backslashes (\\) in Windows paths
FILE_PATH = r'C:\vscodeProjects\klresearchtbvpotentiaal\models\base\index.html'


def extract_transactions(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    transactions = []
    
    # Each transaction is contained within a 'reveal-content' div
    transaction_blocks = soup.find_all('div', class_='reveal-content')

    for block in transaction_blocks:
        data = {}
        
        # 1. Extract Main Transaction Details
        main_content = block.find('div', class_='transaction-content')
        if not main_content:
            continue
            
        # Find all direct key-value pairs (excluding the nested Shares subtab)
        lines = main_content.find_all('div', class_='content-line', recursive=False)
        for line in lines:
            key = line.find('div', class_='content-key').text.strip()
            val = line.find('div', class_='content-val').text.strip()
            data[key] = val

        # 2. Extract Shares (who owed what)
        shares_section = block.find('div', class_='subtab-content')
        if shares_section:
            share_blocks = shares_section.find_all('div', class_='shares-content')
            for share in share_blocks:
                member_name = ""
                amount = ""
                share_lines = share.find_all('div', class_='content-line')
                for s_line in share_lines:
                    s_key = s_line.find('div', class_='content-key').text.strip()
                    s_val = s_line.find('div', class_='content-val').text.strip()
                    if s_key == "Member":
                        member_name = s_val
                    elif s_key == "Amount":
                        amount = s_val
                
                if member_name:
                    # Creates columns like 'Share: Kirsten'
                    data[f"Share: {member_name}"] = amount

        transactions.append(data)
    return transactions

def save_to_csv(transactions, output_file):
    if not transactions:
        return

    # Get all unique keys from all transactions for the CSV header
    headers = set()
    for t in transactions:
        headers.update(t.keys())
    
    # Sort headers to keep 'Name', 'Amount', 'Payed by' etc. near the front
    sorted_headers = sorted(list(headers))

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=sorted_headers)
        writer.writeheader()
        writer.writerows(transactions)

if __name__ == "__main__":
    # Check if path exists first to give a helpful error
    if not os.path.exists(FILE_PATH):
        print(f"ERROR: The file does not exist at: {FILE_PATH}")
        # List files in that directory to help you debug
        folder = os.path.dirname(FILE_PATH)
        if os.path.exists(folder):
            print(f"Files found in that folder: {os.listdir(folder)}")
    else:
        try:
            with open(FILE_PATH, 'r', encoding='utf-8') as f:
                html_data = f.read()
                
            results = extract_transactions(html_data)
            
            # Save the CSV in the same folder as the HTML
            output_csv = FILE_PATH.replace('.html', '.csv')
            save_to_csv(results, output_csv)
            
            print(f"Success! CSV saved to: {output_csv}")
        except Exception as e:
            print(f"An error occurred: {e}")
