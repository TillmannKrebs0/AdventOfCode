import re
import numpy as np

with open('input', 'r') as file:
    input = file.read()

with open('input', 'r') as file:
    data = [list(line.strip()) for line in file]

inputNP = np.array(data)

total=0


# forward
pattern = re.compile("XMAS")
total += len(pattern.findall(input))

#backward
pattern = re.compile("SAMX")
total += len(pattern.findall(input))

#down
transposed = '\n'.join([''.join(row) for row in inputNP.T])

pattern = re.compile("XMAS")
total += len(pattern.findall(transposed))

#up
pattern = re.compile("SAMX")
total += len(pattern.findall(transposed))

#diagonal
def gather_all_diagonals(grid):
    rows, cols = grid.shape
    diagonals = []

    # Top Left -> Bottom Rigt
    for d in range(-rows + 1, cols): 
        diagonal = [
            grid[i, i - d]
            for i in range(max(0, d), min(rows, cols + d))
            if 0 <= i < rows and 0 <= i - d < cols
        ]
        diagonals.append(''.join(diagonal))


    # Top Right -> Bottom Left
    for d in range(1 - cols, rows):
        diagonal = [
            grid[i, cols - 1 - (i - d)]
            for i in range(max(0, d), min(rows, rows + cols - d - 1))
            if 0 <= i < rows and 0 <= cols - 1 - (i - d) < cols
        ]
        diagonals.append(''.join(diagonal))
    return diagonals


pattern = re.compile("XMAS")
total += len(pattern.findall('\n'.join(gather_all_diagonals(inputNP))))

pattern = re.compile("SAMX")
total += len(pattern.findall('\n'.join(gather_all_diagonals(inputNP))))


print(total)