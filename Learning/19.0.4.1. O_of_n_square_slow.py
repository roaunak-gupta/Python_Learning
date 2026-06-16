
#! This method is slow and worst case is O(n²)
def has_dublicate(number):
    for i in range(len(number)):
        for j in range(len(number)):
            if i != j and number[i] == number[j]:
                print(f"At Index : {i} and {j}")
                number.remove(number[i])
                return True

    return False


number = [10, 20, 20, 30, 40, 50]
result = has_dublicate(number)
if result:
    print("Dublicate found and remove Dublicate")
    print(f"New List {number}")
else:
    print("No Dublicate found")
