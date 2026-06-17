
#! A Array with several names are represented. Remove from original list and Add the Names to New List by Starting names with "A"


names = ["Roaunak", "Aashika", "Billu", "Meenu",
         "Avnish", "Satyam", "Uday", "Sumit", "Ansul", "Manish", "Akul", "Rahul", "Shiv", "Anshika", "Aman"]

names_A = []


def finder(name, names_A):
    for name in names:
        if name.startswith("A"):
            names_A.append(name)

    for name_A in names_A:
        names.remove(name_A)


finder(names, names_A)
print(f"Original List : {names}")
print(f"List of 'A' : {names_A}")
