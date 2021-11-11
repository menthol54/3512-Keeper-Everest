non_con_assets = {
    'land' : float(00.00), 
    'equipment' : float(00.00), 
    'vehicles' : float(00.00),
    'furniture' : float(00.00),
    'buildings' : float(00.00),
    'machinery' : float(00.00),
    }

for key, value in non_con_assets.items():
    non_con_amount = input(key + ': ')
    non_con_assets.update(non_con_amount)
    

        


