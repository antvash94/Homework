keys = input("comma separated keys:").split(",")
my_dict = dict.fromkeys(keys, 0)

result = dict(sorted(my_dict.items()))
print(result)
