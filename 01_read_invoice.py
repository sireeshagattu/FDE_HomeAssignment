import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path

csv_path = Path(__file__).parent / "data" / "homework_invoices.csv"

total_invoices = 0
high_amount_count = 0
invalid_amount_count = 0

with open(csv_path, newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for invoice in reader:
        total_invoices += 1

        invoice_id = invoice["invoice_id"]
        vendor = (invoice["vendor"] or "").strip()
        status = (invoice["status"] or "").strip()
        amount_text = (invoice["amount"] or "").strip()

        print(f"\nInvoice: {invoice_id}")
        print(f"Vendor: {vendor or 'Missing vendor'}")
        print(f"Status: {status or 'Missing status'}")

        try:
            if not amount_text:
                raise ValueError("Amount is missing")

            amount = Decimal(amount_text)

            if not amount.is_finite() or amount < 0:
                raise ValueError("Amount must be a finite, non-negative number")

        except (InvalidOperation, ValueError):
            invalid_amount_count += 1
            print(f"Missing/invalid amount: {amount_text or '(blank)'}")
            continue  # Move to the next invoice

        print(f"Amount: {amount:,.2f}")

        if amount > 100000:
            high_amount_count += 1
            print("Amount is greater than 100,000")
        else:
            print("Amount is 100,000 or less")

print("\n--- Summary ---")
print(f"Total invoices read: {total_invoices}")
print(f"Invoices greater than 100,000: {high_amount_count}")
print(f"Invoices with missing/invalid amount: {invalid_amount_count}")