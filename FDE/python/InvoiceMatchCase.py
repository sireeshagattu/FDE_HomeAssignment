invoice_amount = 50000

match invoice_amount:
    case amount if amount > 50000:
        invoice_approver = "Manager and Director"
    case amount if amount > 25000:
        invoice_approver = "Manager"
    case amount if amount < 1000:
        invoice_approver = "Supervisor"
    case _:
        invoice_approver = "Supervisor"

print("Invoice Amount:", invoice_amount)
print("Invoice Approver:", invoice_approver)