import inspect


def check_near(collection, row, column, h, w):
    counter = 0
    if column > 0:  # влево
        if collection[row][column-1]:
            counter += 1

    if row > 0 and column > 0:  # влево-вверх
        if collection[row-1][column-1]:
            counter += 1

    if row > 0:  # вверх
        if collection[row-1][column]:
            counter += 1

    if row > 0 and column < w-1:  # вправо-вверх
        if collection[row-1][column+1]:
            counter += 1

    if column < w-1:  # вправо
        if collection[row][column+1]:
            counter += 1

    if row < h-1 and column < w-1:  # вправо-вниз
        if collection[row+1][column+1]:
            counter += 1

    if row < h-1:  # вниз
        if collection[row+1][column]:
            counter += 1

    if row < h-1 and column > 0:  # влево-вниз
        if collection[row+1][column-1]:
            counter += 1

    return counter




height = 4
width = 4
current_generation = [[0, 0, 1, 0],
                      [0, 0, 0, 1],
                      [0, 1, 1, 1],
                      [0, 0, 0, 0]]
next_generation = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]

current_mask = set()
next_mask = set()

x, y = 0, 0


while x < height:
    while y < width:
        alives = check_near(current_generation, x, y, height, width)
        if current_generation[x][y] and alives < 2:
            next_generation[x][y] = 0
        elif current_generation[x][y] and alives > 3:
            next_generation[x][y] = 0
        elif current_generation[x][y] and 2 <= alives <= 3:
            next_generation[x][y] = 1
        elif not current_generation[x][y] and alives == 3:
            next_generation[x][y] = 1
        y += 1
    x += 1
    y = 0
else:
    x = 0

current_mask = next_mask
next_mask = set()

for i in next_generation:
    print(i)