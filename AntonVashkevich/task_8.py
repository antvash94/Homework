rows = tuple(map(int, input("from, to:").split(",")))
columns = tuple(map(int, input("from, to:").split(",")))

for col in range(columns[0], columns[1]+1):
    print("\t"+str(col), end='')
print()
for row in range(rows[0], rows[1]+1):
    print(row, end="\t")
    for col in range(columns[0], columns[1]+1):
        print(row*col, end="\t")
    print()
