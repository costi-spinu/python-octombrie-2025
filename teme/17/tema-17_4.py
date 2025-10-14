# Task 4
# Create an app Book Collection. Store the following information about
# books: author, title, genre, year of release, publisher. Provide the
# possibility to add, delete, search, and replace data. Use a dictionary
# to store information.
bookCollection = {}


def store_information(b):
    while True:
        author = input("**Author:").strip()
        if not author:
            print("Field can't be empty.")
            continue
        b["Author"] = author

        title = input("**Title:").strip()
        if not title:
            print("Field can't be empty.")
            continue
        b["Title"] = title

        genre = input("**Genre:").strip()
        if not genre:
            print("Field can't be empty.")
            continue
        b["Genre"] = genre

        year = input("**Year of release:").strip()
        if not year:
            print("Field can't be empty.")
            continue
        b["Year"] = year

        publisher = input("**Publisher:").strip()
        if not publisher:
            print("Field can't be empty.")
            continue
        b["Publisher"] = publisher

        print("Book stored successfully.")
        return print(b)


def add_information(d):
    key = input("Key:").strip()
    value = input("Value:").strip()
    d[key] = value
    return print(d)


def delete_information(key, d):
    if key in d:
        del d[key]
        print(f"The information '{key}' was deleted.")
        return print(d)
    else:
        return print("The key does not exist.")


def search_information(key, d):
    if key in d:
        print(f"Key found!\n\t{key}: {d[key]}")
    else:
        print("Key not found!")


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
        print(f"The value for '{key}' was updated to '{new_value}'.")
    else:
        print("There is not such information!")


# ---------------- MENU ---------------- #
try:
    while True:
        print("\n--- Book Collection App ---")
        print("1. Input information about a book")
        print("2. Add extra information")
        print("3. Delete information")
        print("4. Search information")
        print("5. Replace data key")
        print("6. Replace information for a data key")
        print("7. Show updated information")
        print("8. Exit")

        choice = int(input("\tSelection (1-8):"))

        if choice == 1:
            store_information(bookCollection)
            continue
        elif choice == 2:
            add_information(bookCollection)
            continue
        elif choice == 3:
            delete_information(
                key=input("Enter the key you want to delete:").strip(),
                d=bookCollection,
            )
            continue
        elif choice == 4:
            search_information(key=input("Search keyword?:").strip(), d=bookCollection)
            continue
        elif choice == 5:
            replace_information_key(
                old_key=input("Which key you want to modify?").strip(),
                new_key=input("New key:").strip(),
                d=bookCollection,
            )
            continue
        elif choice == 6:
            replace_information_value(
                key=input("Which key do you want to modify the value?\n").strip(),
                new_value=input("New information:").strip(),
                d=bookCollection,
            )
            continue
        elif choice == 7:
            print(bookCollection)
            continue
        elif choice == 8:
            print("Good bye!")
            break

except ValueError:
    print("Error! Please select from 1-8")
