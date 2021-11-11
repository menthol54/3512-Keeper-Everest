land = float(00.00)
equipment = float(00.00)
vehicles = float(00.00)
stock = float(00.00)
debtors = float(00.00)
bank = float(00.00)
cash = float(00.00)
creditor = float(00.00)
accruels = float(00.00)
working_capital = float(00.00)

non_con_assets = {
    'land' : float(00.00), 
    'equipment' : float(00.00), 
    'vehicles' : float(00.00),
    'furniture' : float(00.00),
    'buildings' : float(00.00),
    'machinery' : float(00.00),
    }

for key, value in non_con_assets.items():
    float(input(key + ' '))

