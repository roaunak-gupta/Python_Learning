with open("Roaunak_Gupta.txt", "w") as file:
    text = "\nHi Everyone,\nWe are Learning File I/O.\nusing Java.\nI Like Programming in Java.\n"
    file.write(text)
    

with open("Roaunak_Gupta.txt", "r") as file:
    data = file.read()
    new_data = data.replace("Java", "Python")
    print("Java Replaced by Python.");
    print(new_data)


with open("Roaunak_Gupta.txt", "w") as file:
    file.write(new_data)
    print(new_data);
    

with open("Roaunak_Gupta.txt", "r") as file:
    data1 = file.read()
    print(data1)
