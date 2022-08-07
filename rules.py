# Любая живая клетка с менее чем двумя живыми соседями умирает, как будто из-за недонаселения.
# Любая живая ячейка с более чем тремя живыми соседями умирает, как бы от перенаселения.
# Любая живая клетка с двумя-тремя живыми соседями живет до следующего поколения.
# Любая мертвая клетка, имеющая ровно три живых соседа, становится живой клеткой.
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
def check_near(lst_here, row, column):
    if lst_here[row][column]:
        return True


@decorator_near
def make_mask(set_here, row, column):
    set_here.add((row, column))


height = 6
width = 6
current_generation = [[0, 0, 1, 0, 0, 0],
                      [1, 0, 1, 0, 0, 0],
                      [0, 1, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0]]
next_generation = [[0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0]]
CLEAR = [[0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]


#current_mask = set()
#next_mask = set()

x, y = 0, 0

for _ in range(7):
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
#            if current_generation[x][y]:
#                make_mask(next_mask, x, y, height, width)
            y += 1
        x += 1
        y = 0
    else:
        x = 0
    for i in current_generation:
        print(i)
    print()
    current_generation = next_generation[:]
    next_generation = CLEAR[:]


#current_mask = next_mask
#next_mask = set()
