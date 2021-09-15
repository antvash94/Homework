my_list = input("comma separated words:").split(",")
result = sorted(list(set(my_list)))
print(result)
