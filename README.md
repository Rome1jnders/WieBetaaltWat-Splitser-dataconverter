# Splitser/WieBetaaltWat HTML to CSV Converter (Dutch/NL below)

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
```bash
python converter.py
```

### 4. Result
The script will generate a .csv file in the same directory, which can be opened in Excel or Google Sheets.
## How it works
The script targets the specific HTML table structures used in the Splitser export. It identifies rows and columns containing dates, descriptions, and amounts, ensuring that the data is flattened correctly into a CSV format.

## Disclaimer
This project is independent and not affiliated with Splitser or WieBetaaltWat. It is designed to help users exercise their right to data portability.
# NL/Dutch, Splitser/WieBetaaltWat HTML naar CSV-Converter

Deze tool extraheert transactiegegevens uit een **Splitser (WieBetaaltWat)** AVG-data-export en slaat deze op als een CSV-bestand.

Wanneer u uw gegevens opvraagt onder de AVG (GDPR), levert Splitser een `.zip`-bestand met daarin een `index.html`-bestand. Hoewel dit bestand leesbaar is in een browser, is het niet gestructureerd voor data-analyse. Dit script parseert de HTML en converteert deze naar een overzichtelijke spreadsheet.

## Hoe u gratis uw gegevens kunt verkrijgen

U heeft geen Premium-abonnement nodig om uw gegevens te exporteren. Onder de AVG heeft u het recht op gratis toegang tot uw gegevens.

1.  **Verzoek:** Neem contact op met de [Splitser Support](support.wiebetaaltwat.nl) en vraag om een volledige export van uw persoonsgegevens (AVG/GDPR-verzoek).
2.  **Downloaden:** U ontvangt een link naar een `.zip`-bestand.
3.  **Uitpakken:** Pak de map uit om het `index.html`-bestand te vinden.

## Gebruik

### 1. Installeer afhankelijkheden
Dit script vereist `BeautifulSoup4` voor het parsen van de HTML:

```bash
pip install beautifulsoup4
```

### 2. Configureer het bestandspad
Voordat u het script uitvoert, moet u het verwijzen naar de locatie van uw index.html. Open het Python-bestand en werk de FILE_PATH-variabele bij:
python
#### Pas dit aan naar de daadwerkelijke locatie van uw index.html-bestand
```
FILE_PATH = r'C:\vscodeProjects\klresearchtbvpotentiaal\models\base\index.html'
```

### 3. Voer het script uit
```bash
python converter.py
```

### 4. Resultaat
Het script genereert een .csv-bestand in dezelfde map, dat kan worden geopend in Excel of Google Sheets.
## Hoe het werkt
Het script richt zich op de specifieke HTML-tabelstructuren die in de Splitser-export worden gebruikt. Het identificeert rijen en kolommen met datums, beschrijvingen en bedragen, en zorgt ervoor dat de gegevens correct worden omgezet naar een CSV-formaat.
## Disclaimer
Dit project is onafhankelijk en niet gelieerd aan Splitser of WieBetaaltWat. Het is ontworpen om gebruikers te helpen hun recht op dataportabiliteit uit te oefenen.
