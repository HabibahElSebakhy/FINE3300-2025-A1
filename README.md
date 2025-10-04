# FINE3300 – Assignment 1

## Project Details
This project has two parts:

1. **Mortgage Payments (`mortgage.py`)**  
   - Calculates mortgage payments for different payment frequencies (monthly, semi-monthly, bi-weekly, weekly, accelerated bi-weekly, accelerated weekly).  
   - Uses the quoted annual fixed interest rate (semi-annual compounding), principal amount, and amortization period.  

2. **Exchange Rates (`exchange.rates.py`)**  
   - Reads the Bank of Canada CSV file to get the latest USD/CAD exchange rate.  
   - Converts between USD and CAD in both directions.  

Both parts can be run directly from the terminal.

---

## How to Use

### Part 1 – Mortgage Payments
1. Run the program:
2. Enter:  
   - Principal amount  
   - Quoted annual interest rate (%)  
   - Amortization period (years)  
3. The program will display payments for all six frequencies.  

---

### Part 2 – Exchange Rates
1. Download the Bank of Canada exchange rate file as a .csv.
2. Drag and drop the file into the same folder as exchange.rates.py.
3. Open a terminal in this folder.
4. Run the program
5. Enter:  
   - Amount (e.g., 100000)  
   - From currency (`USD` or `CAD`)  
   - To currency (`USD` or `CAD`)  
6. The program will output the converted value using the latest rate from the CSV file.  




