import json

with open('/Users/dizanmasirov/Desktop/PP2/lab4/json/sample-data.json') as file:
    data = json.load(file)

dt = data["imdata"]
print("Interface Status")
print("=" * 70)
print("DN" + " " * 40 + "Description" + " " * 10 + "Speed" + " " * 4 + "MTU")
print("-" *  41 + " " + "-" * 19 + " " + " " + "-" * 6 + "  " + "-" * 6)

for item in dt:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "") 
    speed = attributes.get("speed", "inherit")  
    mtu = attributes["mtu"]

    print(dn, " " * 50, description, " " * 58, speed, mtu)