import csv
from decimal import Decimal


# Using if / elif / else
def approver_using_if(amount):
    if amount < 0:
        return "Invalid amount"
    elif amount > 50000:
        return "Manager and Director"
    elif amount > 25000:
        return "Manager"
    elif amount < 1000:
        return "Supervisor"
    else:
        return "Approval rule not defined"


# Same logic using match case
def approver_using_match(amount):
    match amount:
        case value if value < 0:
            return "Invalid amount"
        case value if value > 50000:
            return "Manager and Director"
        case value if value > 25000:
            return "Manager"
        case value if value < 1000:
            return "Supervisor"
        case _:
            return "Approval rule not defined"


# Test the amount from your question
invoice_amount = 50000

print("Using if:", approver_using_if(invoice_amount))
print("Using match:", approver_using_match(invoice_amount))


# Read invoices from your uploaded CSV
with open("data/homework_invoices.csv", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    print("\nCSV columns:", reader.fieldnames)

    # Change this to the exact amount column shown above.
    amount_column = "amount"

    if amount_column not in (reader.fieldnames or []):
        print(f"Update amount_column to match your CSV header.")
    else:
        for row_number, row in enumerate(reader, start=2):
            try:
                amount_text = row[amount_column].strip().replace(",", "")
                amount = Decimal(amount_text)

                if not amount.is_finite():
                    raise ValueError("Amount must be a finite number")

            except (ValueError, ArithmeticError, AttributeError):
                print(f"CSV row {row_number}: Invalid or missing amount")
                continue

            print(
                f"Amount: {amount} | "
                f"If: {approver_using_if(amount)} | "
                f"Match: {approver_using_match(amount)}"
            )