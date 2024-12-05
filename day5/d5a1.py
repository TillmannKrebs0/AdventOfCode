rules = set()
with open("rules", "r") as file:
    for line in file:
        parts = line.strip().split("|")
        rules.add((int(parts[0]), int(parts[1])))


updates = []
with open("updates", "r") as file:
    for line in file:
        updates.append([int(x) for x in line.strip().split(",")])


sol = 0
for u in updates:
    correct = True
    for i in range(1, len(u)):
        for j in range(i):
            print((u[j],u[i]))
            if (u[j],u[i]) not in rules:
                correct = False
                break
        if not correct:
            break
    if correct:
      sol += u[len(u) // 2]

print(sol)