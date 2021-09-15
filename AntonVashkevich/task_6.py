list_of_dict = [{"V": "S001"}, {"V": "S002"},
                {"VI": "S001"}, {"VI": "S005"},
                {"VII": "S005"}, {"V": "S009"},
                {"VIII": "S007"}
                ]
unique = set()
for dic in list_of_dict:
    for value in dic.values():
        unique.add(value)
print(unique)
