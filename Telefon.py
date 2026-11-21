import json

try:
    with open ("contacts.json" , "r" , encoding="utf-8") as file:
        contacts = json.load(file)

except FileNotFoundError:
    contacts = {}

def phone1(phone):
    if len(phone) != 11:
        return False
    if not phone.startswith("09"):
        return False
    if not phone.isdigit():
        return False
    return True
while True:
    meno = input("Entekhab Kon: 1.Add    2.Show    3.Search    4.DeleteContact    5.Edit    6.Exit : ")
    if meno == "1":
        esm = input("Esm Contact :")
        phone = input("Shmre cotct :")
        if phone1(phone):
            contacts[esm] = phone
            print("Add Shod")
        else:
            print("no no no")
        # shomre = int(input("Shomare Contact :"))
        # contacts[esm] = shomre
        porsesh = input("Bazam mikhay vared koni?")
        if porsesh == "no":
            break
    elif meno == "2" :
        print(contacts)
    elif meno == "3" :
        search = input("Mored nazar :")
        number = contacts.get(search)
        if number is None:
            print("Peyda Nashod")
        else:
            print(contacts.get(search))
    elif meno == "4":
        mokhatab = input("Kio Delete mikoni?")
        mokhatab1 = contacts.pop(mokhatab , None)
    elif meno == "5":
        name = input("Name Mokhatab?")
        if name in contacts:
            esm2 = input("Esm Contact Chi Beshe?:")
            shomre2 = input("Shomare Jadid Contact :")
            contacts[name] = shomre2
        else:
            print("Mokhtb Not Find")
    elif meno == "6":
        break
    with open("contacts.json" , "w" , encoding="utf-8") as file:
        json.dump(contacts , file , ensure_ascii=False , indent=4)