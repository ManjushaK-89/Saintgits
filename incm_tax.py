grss_incm=int(input("Enter the Gross Income:"))
Dpndncy=int(input("Enter the no.of dependencies:"))
tax_rate=0.20
std_ddctn=10000
dpndnt_ddctn=3000
incm_tax=grss_incm-std_ddctn-(dpndnt_ddctn*Dpndncy)
tax=incm_tax*tax_rate
print("Income Tax:",float(tax))
