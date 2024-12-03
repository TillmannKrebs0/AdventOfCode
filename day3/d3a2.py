import re

with open('input.txt', 'r') as file:
  input = file.read()

multiplyRegex = "mul\([0-9]{1,3},[0-9]{1,3}\)"
sectionsRegEx= "(^|do\(\))(.*?)don't\(\)"
sol=0

def subSolution(str):
  result = 0
  for x in re.findall(multiplyRegex, str):
    x.replace("mul(", "").replace(")", "")
    firstNumber, secondNumber = x.replace("mul(", "").replace(")", "").split(',')
    result += int(firstNumber)*int(secondNumber)
  return result


for doSection in re.findall(sectionsRegEx, input):
    section_content = doSection[1] 
    sol += subSolution(section_content) 


print(sol)

