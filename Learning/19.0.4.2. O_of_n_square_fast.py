
#! This method takes more memory because every item stored in set
def has_dublicate(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True
        seen.add(number)

    return False


number = [10, 20, 20, 30, 40, 50]
result = has_dublicate(number)
if result:
    print("Dublicate found.")
else:
    print("No Dublicate found")
