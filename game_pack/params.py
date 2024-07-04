# Частота кадров
FPS = 10

# Константы сторон
WHITE = 'white'
BLACK = 'black'

# Словарь для быстрого определения противоположной стороны
OPPOSITE_SIDE = {WHITE: BLACK, BLACK: WHITE}

# Ширина/высота клетки в пикселях
CELL_SIZE = 100

# Цвета для белых и черных клеток
WHITE_CELL_COLOR = (210, 180, 140)
BLACK_CELL_COLOR = (138, 102, 66)

# Цвет выделенной ячейки
SELECTED_CELL_COLOR = (120, 120, 255)

# Цвет ячейки, доступной для хода
AVL_MOVE_CELL_COLOR = (140, 203, 94)

# Типы ходов
NORMAL_MOVE = 'normal_move'
CONVERSION = 'conversion'
OFFSET = 'offset'

# Приоритеты ходов
priority_list = [OFFSET, CONVERSION, NORMAL_MOVE]

# Функция-ключ для сортировки ходов
def key_func_for_moves(move):
    return priority_list.index(move.m_type, 0, 3)

