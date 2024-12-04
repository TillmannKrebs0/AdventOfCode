with open('input', 'r') as file:
    data = [list(line.strip()) for line in file]

sol = 0
ms_set = {"M", "S"}

for i in range(1,len(data)-1):
    for j in range(1,len(data[i])-1):
        if (data[i][j] == "A"):
            if {data[i-1][j-1], data[i+1][j+1]} == ms_set and {data[i-1][j+1], data[i+1][j-1]} == ms_set:
                sol += 1

print(sol)
