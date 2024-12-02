list1 = []
list2 = []
simScore = 0
dictionary = {}


with open('input', 'r') as file:
    for line in file:
        list1.append(int(line.split(' ')[0]))
        list2.append(int(line.split('   ')[1].replace('\n', '')))


for x in list2:
    if (not dictionary.get(x)):
        dictionary.update({x:1})
    else:
        dictionary.update({x:dictionary.get(x)+1})


for y in list1:
    if (dictionary.get(y)):
        simScore += y*dictionary.get(y)
        
print(simScore)
