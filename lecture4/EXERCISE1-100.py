row = int(input("Enter a row: "))
N_row = 100//row
for i in range(row):
    start = i * N_row + 1
    end = start + N_row - 1
    for j in range(start, end + 1):
        print(j, end=' ')
    print()  