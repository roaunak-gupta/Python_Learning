list1 = [1,2,1]
list2 = [1,2,3]

copy_list = list1.copy()
copy_list.reverse()
if(list1 == copy_list):
    print("This is an Palindrome List");
else:
    print("This is not an Palindrome List");
    
    