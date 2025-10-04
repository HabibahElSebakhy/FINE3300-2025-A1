# Question 2: Exchange Rates
# This program reads the latest USD/CAD exchange rate from a CSV file
# and converts an amount from USD to CAD or CAD to USD.
# The exchange rate file is provided by the Bank of Canada.
# Internal details (like reading the CSV) are kept private.

import csv

class ExchangeRates:
    def __init__(self, filepath):
        # Private attribute: store the exchange rate safely
        # so the user cannot accidentally overwrite it
        self.__rate = self.__get_latest_rate(filepath)

    # Private helper method:
    # Reads the CSV file and extracts the latest USD/CAD exchange rate.
    def __get_latest_rate(self, filepath):
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = list(csv.reader(f))   # read all rows
            header = reader[0]             # first row = column names
            last_row = reader[-1]          # last row = latest data

            # Look for USD/CAD column in the header row
            for idx, name in enumerate(header):
                if "USD/CAD" in name.upper() or ("USD" in name.upper() and "CAD" in name.upper()):
                    return float(last_row[idx])  # return rate as float

        # If no USD/CAD column found, stop program
        raise ValueError("USD/CAD rate not found in file")

    # Public method: converts an amount between USD and CAD
    def convert(self, amount, from_currency, to_currency):
        """
        Converts an amount between USD and CAD using the latest exchange rate.
        Formula:
            - USD → CAD: multiply by rate
            - CAD → USD: divide by rate
        """
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == "USD" and to_currency == "CAD":
            return round(amount * self.__rate, 2)   # multiply for USD → CAD
        elif from_currency == "CAD" and to_currency == "USD":
            return round(amount / self.__rate, 2)   # divide for CAD → USD
        else:
            raise ValueError("Only USD <-> CAD conversions supported")

# Example run
if __name__ == "__main__":
    filepath = "BankOfCanadaExchangeRates.csv"   # Bank of Canada CSV file
    exchange = ExchangeRates(filepath)

    # Ask user for inputs
    amount = float(input("Enter amount: "))
    from_cur = input("From currency (USD or CAD): ")
    to_cur = input("To currency (USD or CAD): ")

    # Perform conversion
    result = exchange.convert(amount, from_cur, to_cur)

    # Show result
    print(f"{amount} {from_cur} = {result} {to_cur}")
