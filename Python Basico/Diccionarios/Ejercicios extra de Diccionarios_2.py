employees = [

    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},

    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},

    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},

    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},

]

new_list={}
for employee in employees:
    department=employee["department"]

    if department not in new_list:
        new_list[department]=[]

    new_list[department].append(employee["name"])

print(new_list)