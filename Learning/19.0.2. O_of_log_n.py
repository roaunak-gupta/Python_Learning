

#! This is the Example of O(logn)

def binary_search(arr, target):

    left = 0

    right = len(arr) - 1

    while left <= right:

        middle = (left + right) // 2

        print("Middle : ", middle)

        if arr[middle] == target:
            return middle

        elif arr[middle] < target:

            left = middle + 1

            print("Left : ", left)
        else:

            right = middle - 1

            print("Right : ", right)

    return -1


name_liFst = ["Roaunak", "Aashika", "Uday", "Meenu",
              "Sneha", "Sumit", "Manish", "Om", "Lokesh"]

target_name = "Aashika"

result = binary_search(name_list, target_name)


if result != -1:

    print(f"Found at Index : {result}")
else:

    print("Not Found")
