import inspect


def decorator_near(func):
    # Декоратор-монстр. Позволяет функциям взаимодействовать с соседними координатами
    def wrapper(collection, row, column, h, w):

        # Если выполняется функция по созданию маски, то есть возможность взаимодействовать с текущими координатами
        if inspect.signature(func) == inspect.signature(make_mask):
            func(collection, row, column)

        if column > 0:  # влево
            if func(collection, row, column-1):
                wrapper.counter += 1

        if row > 0 and column > 0:  # влево-вверх
            if func(collection, row-1, column-1):
                wrapper.counter += 1

        if row > 0:  # вверх
            if func(collection, row-1, column):
                wrapper.counter += 1

        if row > 0 and column < w-1:  # вправо-вверх
            if func(collection, row-1, column+1):
                wrapper.counter += 1

        if column < w-1:  # вправо
            if func(collection, row, column+1):
                wrapper.counter += 1

        if row < h-1 and column < w-1:  # вправо-вниз
             if func(collection, row+1, column+1):
                wrapper.counter += 1

        if row < h-1:  # вниз
            if func(collection, row+1, column):
                wrapper.counter += 1

        if row < h-1 and column > 0:  # влево-вниз
            if func(collection, row+1, column-1):
                wrapper.counter += 1

        if wrapper.counter:
            # если изменился счетчик, то мы его возвращаем. Нужно для проверки живых клеток вокруг.
            for_return = wrapper.counter
            wrapper.counter = 0
            return for_return
    wrapper.counter = 0
    return wrapper


@decorator_near
def check_near_lst(lst_here, row, column):
    if lst_here[row][column]:
        return True


@decorator_near
def check_near_set(set_here, row, column):
    if (row, column) in set_here:
        return True


@decorator_near
def make_mask(set_here, row, column):
    set_here.add((row, column))


height = 6
width = 6
current_generation_lst = [[0, 0, 1, 0, 0, 0],
                          [1, 0, 1, 0, 0, 0],
                          [0, 1, 1, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0]]
#next_generation = [[0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0]]
#CLEAR = [[0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0]]

current_mask = set()
next_mask = set()

current_generation_set = set()
next_generation_set = set()

x, y = 0, 0

while x < height:
    while y < width:
        alives = check_near_lst(current_generation_lst, x, y, height, width)
        if current_generation_lst[x][y] and alives < 2:
            pass
        elif current_generation_lst[x][y] and alives > 3:
            pass
        elif current_generation_lst[x][y] and 2 <= alives <= 3:
            current_generation_set.add((x, y))
            make_mask(current_mask, x, y, height, width)
        elif not current_generation_lst[x][y] and alives == 3:
            current_generation_set.add((x, y))
            make_mask(current_mask, x, y, height, width)
        y += 1
    x += 1
    y = 0
else:
    x = 0


visualization = list()

for _ in range(15):
    for coordinates_in_mask in current_mask:
        x, y = coordinates_in_mask[0], coordinates_in_mask[1]
        alives = check_near_set(current_generation_set, x, y, height, width)
        if (x, y) in current_generation_set and alives < 2:
            pass
        elif (x, y) in current_generation_set and alives > 3:
            pass
        elif (x, y) in current_generation_set and 2 <= alives <= 3:
            next_generation_set.add((x, y))
            make_mask(next_mask, x, y, height, width)
        elif (x, y) not in current_generation_set and alives == 3:
            next_generation_set.add((x, y))
            make_mask(next_mask, x, y, height, width)
    visualization = [[0 for _ in range(width)] for s in range(height)]
    for cell in next_generation_set:
        x, y = cell[0], cell[1]
        visualization[x][y] = 1
    for line in visualization:
        print(line)
    print()
    current_generation_set = next_generation_set
    next_generation_set = set()
    current_mask = next_mask
    next_mask = set()