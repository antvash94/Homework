with open("data/unsorted_names.txt", "r") as file:
    sorted_names = sorted(file.readlines())
    with open("data/sorted_names.txt", "w") as f:
        f.writelines(sorted_names)
