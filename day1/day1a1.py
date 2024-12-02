list1 = []
list2 = []
sol = 0

with open('input', 'r') as file:
    for line in file:
        list1.append(int(line.split(' ')[0]))
        list2.append(int(line.split('   ')[1].replace('\n', '')))

list1.sort()
list2.sort()

for i in range(len(list1)):
    sol += abs(list1[i]-list2[i])

print(sol)
