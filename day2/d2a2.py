reports = []

with open('input', 'r') as file:
    for line in file:
        reports.append(line.strip().split(' '))


def checkAscending(l):
    for j in range(1, len(l)):
        if int(l[j]) <= int(l[j-1]) or int(l[j]) - int(l[j-1]) > 3:
            return False 
    return True


def checkDescending(l):
    for j in range(1, len(l)):
        if int(l[j]) >= int(l[j-1]) or int(l[j-1]) - int(l[j]) > 3:
            return False  
    return True


sol = 0
for level in reports:
    if checkAscending(level) or checkDescending(level):
        sol += 1 
    else:
        for n in range(len(level)):
            if (checkAscending(level[:n]+level[n+1:]) or checkDescending(level[:n]+level[n+1:])):
                sol += 1
                break

print(sol)
