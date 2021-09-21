import csv


def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path, "r") as file:
        reader = csv.reader(file, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        sorted_st = sorted(reader, reverse=True, key=lambda x: x[2])
        return [student[0] for student in sorted_st[1:number_of_top_students+1]]


def sort_by_age(file_path):
    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        sorted_st = sorted(reader, reverse=True, key=lambda x: x[1])
        with open("data/sort_students.csv", "w") as f:
            writer = csv.writer(f)
            for i in sorted_st:
                writer.writerow(i)

sort_by_age("data/students.csv")
