student = {
    "Name": "Roaunak Gupta",
    "Course": "B.Tech",
    "Branch": "Computer Science & Enginering",
    "Year": "4th",
    "Marks": {
        "Computer Network": 50,
        "Essance of Traditional Knowlendge": 26,
        "Idea of Business Modal": 56,
        "Software Engineering": 46,
        "Mathematics-4": 12,
        "Compiler Design": 56,
        "Big Data": 66
    }
}

student["age"] = 24 # This is an method to add data to an dictionary
print(student["Marks"]["Big Data"], "\n")
print(student.keys(), "\n")  # It return all key in dictionary
print(student.values(), "\n")  # It return all values in dictionary
print(student.items(), "\n")  # Return all values and keys pair in tupple
# It Return the enter key value and when key is wrong then they give an error
print(student["Name"], "\n")
# It Return the enter key value and when key is wrong then return None.
print(student.get("Name"), "\n")


new_dict = {"City": "Barabanki, Uttar Pradesh"}
student.update(new_dict)  # It Return the enter key value
print(student)
