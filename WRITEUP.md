# FINE3300 – Assignment 1 Write-Up

## (a) GitHub Repository
[GitHub Repository Link](https://github.com/HabibahElSebakhy/FINE3300-2025-A1)

## (b) Program Output
For a principal amount of **$500,000**, quoted at **5.5%**, amortized over **25 years**: Monthly Payment: $3,051.96
Semi-monthly Payment: $1,524.25
Bi-weekly Payment: $1,406.88
Weekly Payment: $703.07
Rapid Bi-weekly Payment: $1,525.98
Rapid Weekly Payment: $762.99


## (c) Exchange Rate Conversion

Using the Bank of Canada exchange rate file, the program read the latest USD/CAD exchange rate (≈ **1 USD = 1.3698 CAD**) and performed the following conversions:

For an amount of **$100,000 USD → CAD**:
100000.0 USD = 136980.0 CAD

For an amount of **$100,000 CAD → USD**:
100000.0 CAD = 73003.36 USD


**Explanation:**  
- The conversion rate was retrieved from the last row of the Bank of Canada CSV file.  
- The program correctly multiplied when converting **USD → CAD**, and divided when converting **CAD → USD**.  



## References
- Python Software Foundation. (2023). *csv — CSV File Reading and Writing*. Python 3.11 documentation. https://docs.python.org/3/library/csv.html
- Python Software Foundation. (2023). *Reading and Writing Files*. Python 3.11 documentation. https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
- Python Software Foundation. (2023). *Built-in Functions: round*. Python 3.11 documentation. https://docs.python.org/3/library/functions.html#round
