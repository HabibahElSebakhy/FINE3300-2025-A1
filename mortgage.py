# Question 1: Mortgage Payments
# This program calculates mortgage payments under different payment frequencies
# based on the principal, quoted interest rate, and amortization period.
# Makes internal data/helpers private where it makes sense

class MortgageCalculator:
    def __init__(self, principal, quoted_rate_percent, years):
        # private data (user shouldn't mutate these after creation)
        self.__principal = float(principal)
        self.__quoted_rate_percent = float(quoted_rate_percent)
        self.__years = int(years)

    # private helper: effective annual rate from j2 (semi-annual compounding)
    # into the effective annual interest rate (i_eff).
    # Formula: i_eff = (1 + j2/2)^2 - 1
    def __effective_rate(self):
        j2 = self.__quoted_rate_percent / 100.0
        return (1 + j2 / 2.0) ** 2 - 1.0

    # Private helper method: calculates the payment for a given frequency (m).
    # Formula: Payment = P * r / (1 - (1 + r)^(-n))
    # where:
    #   P = principal
    #   r = periodic interest rate
    #   n = total number of payments
    def __payment(self, m):
        i_eff = self.__effective_rate()
        r = (1 + i_eff) ** (1.0 / m) - 1.0          # periodic rate
        n = int(m * self.__years)                   # number of payments
        return self.__principal * r / (1 - (1 + r) ** (-n))

    # public API: compute all frequencies
    # It computes all six payment types and returns them in a dictionary.

    def calculate(self):
        monthly       = self.__payment(12)
        semi_monthly  = self.__payment(24)
        bi_weekly     = self.__payment(26)
        weekly        = self.__payment(52)
        rapid_biweek  = monthly / 2.0
        rapid_weekly  = monthly / 4.0
        return {
            "Monthly": monthly,
            "Semi-monthly": semi_monthly,
            "Bi-weekly": bi_weekly,
            "Weekly": weekly,
            "Rapid Bi-weekly": rapid_biweek,
            "Rapid Weekly": rapid_weekly,
        }


if __name__ == "__main__":
    try:
        # TYPE ONLY NUMBERS here (no file paths)
        principal = float(input("Enter principal amount: "))
        quoted = float(input("Enter quoted nominal rate (%): "))
        years = int(input("Enter amortization period (years): "))

        calc = MortgageCalculator(principal, quoted, years)
        results = calc.calculate()

        for label, value in results.items():
            print(f"{label} Payment: ${value:,.2f}")

    except ValueError as e:
        print("Input error: please enter numeric values (e.g., 500000, 5.5, 25).")
