import re

result = 0
regEx = "mul\([0-9]{1,3},[0-9]{1,3}\)"

with open('input.txt', 'r') as file:
  input = file.read()

for s in re.findall(regEx, input):
  s.replace("mul(", "").replace(")", "")
  firstNumber, secondNumber = s.replace("mul(", "").replace(")", "").split(',')
  result += int(firstNumber)*int(secondNumber)

print(result)