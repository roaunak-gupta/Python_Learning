

#! This is the Example of O(logn)

def binary_search(arr, target):

    left = 0
    right = len(arr)
    attempt = 1
    while left <= right:

        middle = (left + right) // 2
        print(f"Attempt : {attempt} Value Range : {left} - {middle} - {right}")

        if arr[middle] == target:
            return middle

        elif arr[middle] < target:

            left = middle + 1

            print(f"Attempt : {attempt} Update Left : {left} and Right : {right}\n")

        else:

            right = middle - 1
            print(f"Attempt : {attempt} Left : {right} and Update Right : {right}\n")

        attempt = attempt+1
    return -1


i = 0
li = []

while i < 1000:
    i = i+1
    li.append(i)
target = int(input("Enter your Number : "))
print(f"Finding Target : {target}")
result = binary_search(li, target)

if result != -1:
    print(f"Found at Index : {result}")
else:
    print("Not Found !")