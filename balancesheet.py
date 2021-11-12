import json
import datetime
now = datetime.datetime.now()
file_number = 0
land = 00 
equipment = 00 
vehicles = 00
furniture = 00
buildings = 00
machinery = 00

land += float(input('Land: '))
equipment += float(input('Equipment: '))
vehicles += float(input('Vehicles: '))
furniture += float(input('Furniture: '))
buildings += float(input('Buildings: '))
machinery += float(input('Machinery: '))
non_cur_assets = land + equipment + vehicles + furniture + buildings + machinery

new_val = {
    'date': now.strftime("%Y-%m-%d %H:%M:%S"),
    'land': land,
    'equipment': equipment,
    'vehicles': vehicles,
    'furniture': furniture,
    'buildings': buildings,
    'machinery': machinery,
    'non_cur_assets': non_cur_assets,
}

    
ba = open(f'bal_sheets/balancesheet.json{file_number}', 'w')

json.dump(new_val, ba, indent = 6)

ba.close()
    
    

        


