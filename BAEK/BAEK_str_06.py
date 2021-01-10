string = input()
string_list = list(string.split(" "))
string_list = [i for i in string_list if i != ""]
print(len(string_list))