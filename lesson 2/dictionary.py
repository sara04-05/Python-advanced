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

contact_information ={
    "Festa" : {
        "phone_number" : "123-456",
        "email" : "Festa@gmail.com",
        "home_adress": "Bregu i Diellit",
        "birthday" : "03/02/2003"
    },
    "Sara" :  {
        "phone_number" : "123-123",
        "email" : "Sara@gmail.com",
        "home_adress": "Bregu i Diellit",
        "birthday" : "24/12/2007"
    },
    "Liron" :  {
        "phone_number" : "123-111",
        "email" : "Liron@gmail.com",
        "home_adress": "Bregu i Diellit",
        "birthday" : "01/04/2008"
    }
}

print(contact_information)

sara_information = contact_information["Sara"]
print(sara_information)

contacts = {
    "Festa" : ("123-456" , "Festa@gmail.com"),
    "Sara" : ("123-123" , "Sara@gmail.com"),
    "Liron" : ("123-111" , "Liron@gmail.com")
}

festa_info = contacts["Festa"]
phone_number = festa_info[0]
print(phone_number)
email = festa_info[1]
print(email)

phone_number, email = contacts["festa"]