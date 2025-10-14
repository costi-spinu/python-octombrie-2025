# Task 3
# Create an app Company. Store the following information about a person:
#  full name, phone number, corporate email, job title, room number, skype.
#  Provide the possibility to add, delete, search, and replace data.
# Use a dictionary to store information.

appCompany = {}


def storeInformation(a):
    while True:
        fullName = input("**Full name:")
        a["Full name"] = fullName
        if not fullName:
            print("Field can't be empty.")
            continue
        phoneNumber = input("**Phone number:")
        a["Phone Number"] = phoneNumber
        if not phoneNumber:
            print("Field can't be empty.")
            continue
        corporateEmail = input("**Bussines E-mail:")
        a["Corporate E-mail"] = corporateEmail
        if not corporateEmail:
            print("Field can't be empty.")
            continue
        jobTitle = input("**Profession:")
        a["Job Title"] = jobTitle
        if not jobTitle:
            print("Field can't be empty.")
            continue

        roomNumber = input("Room number:")
        a["Room Number"] = roomNumber
        if roomNumber == " ":
            continue
        skype = input("Skype Adress:")
        a["Skype adress"] = skype
        if skype == " ":
            continue
        if (
            fullName == ""
            or phoneNumber == ""
            or corporateEmail == ""
            or jobTitle == ""
        ):
            print("** Fields are obligatory:")
        return a


def add_information(d):
    a = input("Cheie:").strip()
    b = input("Valoare:").strip()
    d[a] = b
    return d


def delete_information(cheie, d):

    if cheie in d:
        del d[cheie]
        print(f"Informatia {cheie} a fost eliminata")
        return d
    else:
        return print("Cuvantul nu exista")


def search_information(cheie, d):
    # d={}
    # return print (d.get(cheie, "The information was not found!"))
    if cheie in d:
        i = d[cheie]
        return print(f"key found!\n\t{cheie}:{i}")
    else:
        return print("key not found!")


def replace_information_key(old_key, new_key, d):
    if old_key in d:
        d[new_key] = d.pop(old_key)
        print(f"The key was modified from '{old_key}' to '{new_key}'.")
    else:
        print("The key doesn't exist.")
    return d


def replace_information_value(key, new_value, d):
    if key in d:
        d[key] = new_value
        print(f"The {key} was updated with the new value:{new_value}")
    else:
        return print("There is not such information!")


try:
    while True:
        print("Please select from 1-7")
        print("1. Input information about a person")
        print("2. Add extra information")
        print("3. Delete information")
        print("4. Search information")
        print("5. Replace data key")
        print("6. Replace information for a data key")
        print("7. Updated informations")
        print("8. Exit")
        choice = int(input("\tSelection(1-8):"))
        if choice == 1:
            storeInformation(appCompany)
            continue
        elif choice == 2:
            add_information(appCompany)
            continue
        elif choice == 3:
            delete_information(
                cheie=input("Introdu cuvantul pe care doresti sa il stergi:"),
                d=appCompany,
            )
            continue

        elif choice == 4:
            search_information(cheie=input("Search Key word?:").strip(), d=appCompany)
            continue

        elif choice == 5:
            replace_information_key(
                old_key=input("Wich key you want to modify?"),
                new_key=input("New key:"),
                d=appCompany,
            )
            continue

        elif choice == 6:
            replace_information_value(
                key=input("Which key you want to modify the value?\n"),
                new_value=input("New information:"),
                d=appCompany,
            )
            continue
        elif choice == 7:
            print(appCompany)
            continue
        elif choice == 8:
            print("Good bye!")
            break


except ValueError:
    print("Error!Please select from 1-7")
