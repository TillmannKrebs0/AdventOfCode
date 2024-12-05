from functools import cmp_to_key

rules = set()
with open("rules", "r") as file:
    for line in file:
        parts = line.strip().split("|")
        rules.add((int(parts[0]), int(parts[1])))

updates = []
with open("updates", "r") as file:
    for line in file:
        updates.append([int(x) for x in line.strip().split(",")])


def compare(a, b):
    if (a,b) in rules:
        return -1
    elif (b,a) in rules:
        return 1
    else:
        return -1
    

sol = 0
for u in updates:
    correct = True
    for i in range(1, len(u)):
        for j in range(i):
            if (u[j],u[i]) not in rules:
                sol += sorted(u, key=cmp_to_key(compare))[len(u) // 2]
                correct = False
                break
        if not correct:
            break
        
print(sol)
