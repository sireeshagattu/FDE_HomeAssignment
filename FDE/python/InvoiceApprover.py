invoice_amount = 50000

if invoice_amount < 1000:
    invoice_approver = "Supervisor"
elif invoice_amount > 50000:
    invoice_approver = "Manager and Director"
elif invoice_amount > 25000:
    invoice_approver = "Manager"
else:
    invoice_approver = "Supervisor"

print("Invoice Amount:", invoice_amount)
print("Invoice Approver:", invoice_approver)