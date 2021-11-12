
import json

land = 00 
equipment = 00 
vehicles = 00
furniture = 00
buildings = 00
machinery = 00

land += int(input('Land: '))
equipment += int(input('Equipment: '))
vehicles += int(input('Vehicles: '))
furniture += int(input('Furniture: '))
buildings += int(input('Buildings: '))
machinery += int(input('Machinery: '))
non_cur_assets = land + equipment + vehicles + furniture + buildings + machinery

new_val = {
    'land': land,
    'equipment': equipment,
    'vehicles': vehicles,
    'furniture': furniture,
    'buildings': buildings,
    'machinery': machinery,
    'non_cur_assets': non_cur_assets,
}

    
ba = open('balancesheet.json', 'w')

json.dump(new_val, ba, indent = 6)

ba.close()
    

    

        


