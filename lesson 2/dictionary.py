contacts = {"Festa": "123-456",
            "Sara": "456-789"
}

saras_number = contacts["Sara"]
print(saras_number)

contacts["Festa"] = "123-567"
print(contacts)

contacts["Egzon"] = "111-222"
print(contacts)

del contacts["Egzon"]
print(contacts)

keys = contacts.keys()
print(keys)

values = contacts.values()
print(values)

items = contacts.items()
print(items)