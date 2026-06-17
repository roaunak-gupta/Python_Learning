with open("Number_Converter.txt", "w") as file:

    numbers = "1,5,6,5,8,12,15,16,49,12,56,"

    file.write(numbers)



with open("Number_Converter.txt", "r") as file_read:

    rFile = file_read.read()

    print(file_read)

    num = ""

    for i in range(len(rFile)):

        if(rFile[i] == ","):
            num_int = int(num)

            print("Number :" ,num_int," and Type :",type(num_int))
            
            num = ""

        else:

            num += rFile[i]

# Alternate Option - Short and Easy
with open("Number_Converter.txt","r") as f:
    d = f.read()
    nums = d.split(",");
    print(nums);
    