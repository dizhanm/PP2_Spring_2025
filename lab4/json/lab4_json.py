import json

with open('/Users/dizanmasirov/Desktop/PP2/lab4/json/sample-data.json') as file:
    data = json.load(file)

dt = data["imdata"]

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print(f"{'-' * 50} {'-' * 20} {'-' * 10} {'-' * 10}")

for item in dt:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes["mtu"]

    print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<10}")