reports = []

with open('input', 'r') as file:
    for line in file:
        reports.append(line.replace('\n', '').split(' '))
sol = 0


for i in range(len(reports)):
    sorted = True
    for j in range(1, len(reports[i])):
        if (int(reports[i][j]) <= int(reports[i][j-1])):
            sorted = False
        if (int(reports[i][j]) - int(reports[i][j-1]) > 3):
            sorted = False
    if sorted:
        print(reports[i])
        sol += 1

for i in range(len(reports)):
    sorted = True;
    for j in range(1, len(reports[i])):
        if (int(reports[i][j]) >= int(reports[i][j-1])):
            sorted = False

        if (int(reports[i][j-1]) - int(reports[i][j]) > 3):
            sorted = False
    if sorted:
        sol += 1
        print(reports[i])

print(sol)
