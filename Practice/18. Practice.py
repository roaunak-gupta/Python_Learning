
#! A Array with several names are represented. Remove from original list and Add the Names to New List by Starting names with "A"

names = ["Roaunak", "Aashika", "Billu", "Meenu",
         "Avnish", "Satyam", "Uday", "Sumit", "Ansul", "Manish", "Akul", "Rahul", "Shiv", "Anshika", "Aman"]

names_A = []


def finder(names, names_A):
    i = 0
    while i < len(names):
        print(f"Index : {i}")
        if names[i].startswith("A"):
            print(f"Name : {names[i]}")
            names_A.append(names[i])
            names.remove(names[i])
            continue
        i = i + 1


finder(names, names_A)
print(f"Original List : {names}")
print(f"List of 'A' : {names_A}")
