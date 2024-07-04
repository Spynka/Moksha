from game_pack.figures import *
from game_pack import game

class Move:

    def __init__(self, move_type, figure, new_row, new_col):
        self.m_type = move_type
        self.figure = figure
        self.new_row = new_row
        self.new_col = new_col
        self.old_row = figure.row
        self.old_col = figure.col


class Board:
    def __init__(self, pl_side):
        self.pl_side = pl_side
        self.cmp_side = OPPOSITE_SIDE[pl_side]
        # Списки фигур игрока и компьютера
        self.pl_figures = []
        self.cmp_figures = []
        # Словарь, позволяющий быстро найти список фигур по их цвету
        self.figures_dict = {self.pl_side: self.pl_figures, self.cmp_side: self.cmp_figures}
        if self.cmp_side == BLACK:
            self.cmp_figures.append(BlackOkta(0, 2, self.cmp_side, self))
            self.cmp_figures.append(BlackTetra(0, 3, self.cmp_side, self))
            self.cmp_figures.append(BlackMono(0, 7, self.cmp_side, self))
            self.cmp_figures.append(BlackDi(0, 6, self.cmp_side, self))
            self.cmp_figures.append(BlackTri(0, 4, self.cmp_side, self))
            self.cmp_figures.append(BlackUgol(0, 5, self.cmp_side, self))

        if self.pl_side == WHITE:
            self.pl_figures.append(WhiteOkta(7, 5, self.pl_side, self))
            self.pl_figures.append(WhiteTetra(7, 4, self.pl_side, self))
            self.pl_figures.append(WhiteMono(7, 0, self.pl_side, self))
            self.pl_figures.append(WhiteDi(7, 1, self.pl_side, self))
            self.pl_figures.append(WhiteTri(7, 3, self.pl_side, self))
            self.pl_figures.append(WhiteUgol(7, 2, self.pl_side, self))

        if self.cmp_side == WHITE:
            self.cmp_figures.append(WhiteOkta(0, 7, self.cmp_side, self))
            self.cmp_figures.append(WhiteTetra(0, 6, self.cmp_side, self))
            self.cmp_figures.append(WhiteMono(0, 2, self.cmp_side, self))
            self.cmp_figures.append(WhiteDi(0, 3, self.cmp_side, self))
            self.cmp_figures.append(WhiteTri(0, 5, self.cmp_side, self))
            self.cmp_figures.append(WhiteUgol(0, 4, self.cmp_side, self))

        if self.pl_side == BLACK:
            self.pl_figures.append(BlackOkta(7, 0, self.pl_side, self))
            self.pl_figures.append(BlackTetra(7, 1, self.pl_side, self))
            self.pl_figures.append(BlackMono(7, 5, self.pl_side, self))
            self.pl_figures.append(BlackDi(7, 4, self.pl_side, self))
            self.pl_figures.append(BlackTri(7, 2, self.pl_side, self))
            self.pl_figures.append(BlackUgol(7, 3, self.pl_side, self))

        # Создаем клетки поля
        self.cells = []
        for i in range(0, 8):
            self.cells.append([None] * 8)
        for figure in (self.cmp_figures + self.pl_figures):
            self.cells[figure.row][figure.col] = figure
        # Создаем список сделанных во время игры ходов
        self.move_list = []

    # Метод возвращает количество сделанных ходов
    def get_moves_count(self):
        return len(self.move_list)

    # Метод возвращает количество фигур на доске
    def get_figures_count_pl(self):
        count_pl = 0
        for figure in self.pl_figures:
            if not figure.is_drop:
                count_pl += 1
        return count_pl

    def get_figures_count_cmp(self):
        count_cmp = 0
        for figure in self.cmp_figures:
            if not figure.is_drop:
                count_cmp += 1
        return count_cmp

    # Метод возвращает все доступные ходы для выбранных фигур (белых или черных)
    def get_all_avl_moves(self, side):
        # Определяем набор фигур, для которого будем получать доступные ходы
        work_list = self.figures_dict[side]

        # Перебираем фигуры из набора
        result = []

        for figure in work_list:
            if figure.is_drop:
                continue
        avl_moves = self.get_avl_moves_for_figure(figure)
        result += avl_moves

        # Сортируем ходы по возрастанию приоритета
        result.sort(key=key_func_for_moves)

        # Возвращаем результат
        return result

    def get_avl_moves_for_figure(self, figure):
        moves = []

        figure_type = type(figure)
        keys = pygame.key.get_pressed()
        actions = figure.get_actions()
        for new_row, new_col in actions:
            drop_figure = self.get_figure(new_row, new_col)
            if drop_figure is None:
                moves.append(self.create_normal_move(figure, new_row, new_col))
                continue
                # если фигура на пути другого цвета, то выполняются следующие действия
            if drop_figure.side != figure.side:
                moves.append(self.create_offset(figure, new_row, new_col))
                moves.append(self.create_conversion_move(figure, new_row, new_col))
        return moves

    def get_avl_moves_for_figure90(self, figure):
        moves = []
        figure_type = type(figure)
        actions = figure.get_actions90()
        for new_row, new_col in actions:
            drop_figure = self.get_figure(new_row, new_col)
            if drop_figure is None:
                moves.append(self.create_normal_move(figure, new_row, new_col))
                continue
                # если фигура на пути другого цвета, то выполняются следующие действия
            if drop_figure.side != figure.side:
                moves.append(self.create_offset(figure, new_row, new_col))
                moves.append(self.create_conversion_move(figure, new_row, new_col))
        return moves
    def get_avl_moves_for_figure180(self, figure):
        moves = []
        figure_type = type(figure)
        actions = figure.get_actions180()
        for new_row, new_col in actions:
            drop_figure = self.get_figure(new_row, new_col)
            if drop_figure is None:
                moves.append(self.create_normal_move(figure, new_row, new_col))
                continue
                # если фигура на пути другого цвета, то выполняются следующие действия
            if drop_figure.side != figure.side:
                moves.append(self.create_offset(figure, new_row, new_col))
                moves.append(self.create_conversion_move(figure, new_row, new_col))
        return moves
    def get_avl_moves_for_figure270(self, figure):
        moves = []
        figure_type = type(figure)
        actions = figure.get_actions270()
        for new_row, new_col in actions:
            drop_figure = self.get_figure(new_row, new_col)
            if drop_figure is None:
                moves.append(self.create_normal_move(figure, new_row, new_col))
                continue
                # если фигура на пути другого цвета, то выполняются следующие действия
            if drop_figure.side != figure.side:
                moves.append(self.create_offset(figure, new_row, new_col))
                moves.append(self.create_conversion_move(figure, new_row, new_col))
        return moves

    # Метод создает обычный ход
    @staticmethod
    def create_normal_move(figure, new_row, new_col):
        move = Move(NORMAL_MOVE, figure, new_row, new_col)
        return move

    # Метод создает ход-взятие
    def create_offset(self, figure, new_row, new_col):
        move = Move(OFFSET, figure, new_row, new_col)
        move.drop_figure = self.get_figure(new_row, new_col)
        return move

    # Метод создает ход-конверсию
    def create_conversion_move(self, figure, new_row, new_col):
        move = Move(CONVERSION, figure, new_row, new_col)
        move.drop_figure = self.get_figure(new_row, new_col)
        move.new_figure = None
        move.new_drop_figure = None
        return move


    # Метод применяет переданный ход и вносит его в список совершенных ходов
    def apply_move(self, move):
        # Вносим применяемый ход в список ходов
        self.move_list.append(move)
        # Выполняем действия хода в зависимости от его типа
        # Обычный ход
        if move.m_type == NORMAL_MOVE:
            move.figure.set_pos(move.new_row, move.new_col)
            # Перемещаем фигуру на доске
            self.cells[move.old_row][move.old_col] = None
            self.cells[move.new_row][move.new_col] = move.figure
            return

        # Ход-смещение
        if move.m_type == OFFSET:
            move.figure.set_pos(move.new_row, move.new_col)
            move.figure.is_drop = True
            if move.drop_figure is not None:
                move.drop_figure.is_drop = True
            self.figures_dict[move.drop_figure.side].append(move.drop_figure)
            move.drop_figure.is_drop = True
            if move.old_row > move.new_row and self.cells[move.old_col] == self.cells[move.new_col]:
                if move.drop_figure.row > 0:
                    move.figure.set_pos(move.new_row, move.new_col)
                    move.drop_figure.set_pos(move.drop_figure.row-1, move.drop_figure.col)
                    self.cells[move.drop_figure.row][move.drop_figure.col] = move.drop_figure
                    self.cells[move.old_row][move.old_col] = None
                    self.cells[move.new_row][move.new_col] = move.figure
                else:
                    move.figure.set_pos(move.new_row+1, move.new_col)
                    self.cells[move.old_row][move.old_col] = None
                    self.cells[move.new_row+1][move.new_col] = move.figure
            elif move.old_row < move.new_row and self.cells[move.old_col] == self.cells[move.new_col]:
                if move.drop_figure.row<7:
                    move.figure.set_pos(move.new_row, move.new_col)
                    move.drop_figure.set_pos(move.drop_figure.row+1, move.drop_figure.col)
                    self.cells[move.drop_figure.row][move.drop_figure.col] = move.drop_figure
                    self.cells[move.old_row][move.old_col] = None
                    self.cells[move.new_row][move.new_col] = move.figure
                else:
                    move.figure.set_pos(move.new_row-1, move.new_col)
                    self.cells[move.old_row][move.old_col] = None
                    self.cells[move.new_row-1][move.new_col] = move.figure
            elif move.old_col > move.new_col and self.cells[move.old_row] == self.cells[move.new_row]:
                if move.drop_figure.col>0:
                    move.figure.set_pos(move.new_row, move.new_col)
                    move.drop_figure.set_pos(move.drop_figure.row, move.drop_figure.col-1)
                    # self.cells[move.drop_figure.row][move.drop_figure.col] = None
                    self.cells[move.drop_figure.row][move.drop_figure.col] = move.drop_figure
                    self.cells[move.old_row][move.old_col] = None
                    self.cells[move.new_row][move.new_col] = move.figure
                else:
                    move.figure.set_pos(move.new_row, move.new_col+1)
                    self.cells[move.old_row][move.old_col] = None
                    self.cells[move.new_row][move.new_col+1] = move.figure

            elif move.old_col < move.new_col and self.cells[move.old_row] == self.cells[move.new_row]:
                if move.drop_figure.col<7:
                    move.figure.set_pos(move.new_row, move.new_col)
                    move.drop_figure.set_pos(move.drop_figure.row, move.drop_figure.col+1)
                    self.cells[move.drop_figure.row][move.drop_figure.col] = move.drop_figure
                    self.cells[move.old_row][move.old_col] = None
                    self.cells[move.new_row][move.new_col] = move.figure
                else:
                    move.figure.set_pos(move.new_row, move.new_col - 1)
                    self.cells[move.old_row][move.old_col] = None
                    self.cells[move.new_row][move.new_col-1] = move.figure
            return

        # Ход-конверсия
        if move.m_type == CONVERSION:
            move.figure.set_pos(move.new_row, move.new_col)
            move.figure.is_drop = True
            if move.drop_figure is not None:
                move.drop_figure.is_drop = True
            self.figures_dict[move.drop_figure.side].append(move.drop_figure)
            move.drop_figure.is_drop = True
            self.figures_dict[move.new_figure.side].append(move.new_figure)
            self.figures_dict[move.drop_figure.side].append(move.drop_figure)
            self.cells[move.drop_figure.row][move.drop_figure.col] = None
            move.drop_figure.set_pos(move.new_row, move.new_col)
            self.cells[move.new_figure.row][move.new_figure.col] = move.new_figure
            if type(move.drop_figure) == WhiteOkta or type(move.drop_figure) == BlackOkta:
                self.cells[move.drop_figure.row][move.drop_figure.col] = None
            else:
                self.cells[move.drop_figure.row][move.drop_figure.col] = move.new_drop_figure
            if move.old_row > move.new_row and self.cells[move.old_col] == self.cells[move.new_col]:
                move.new_figure.set_pos(move.new_row+1, move.new_col)
                self.cells[move.old_row][move.old_col] = None
                self.cells[move.new_row+1][move.new_col] = move.new_figure
            elif move.old_row < move.new_row and self.cells[move.old_col] == self.cells[move.new_col]:
                move.new_figure.set_pos(move.new_row-1, move.new_col)
                self.cells[move.old_row][move.old_col] = None
                self.cells[move.new_row-1][move.new_col] = move.new_figure
            elif move.old_col > move.new_col and self.cells[move.old_row] == self.cells[move.new_row]:
                move.new_figure.set_pos(move.new_row, move.new_col+1)
                self.cells[move.old_row][move.old_col] = None
                self.cells[move.new_row][move.new_col+1] = move.new_figure
            elif move.old_col < move.new_col and self.cells[move.old_row] == self.cells[move.new_row]:
                move.new_figure.set_pos(move.new_row, move.new_col - 1)
                self.cells[move.old_row][move.old_col] = None
                self.cells[move.new_row][move.new_col-1] = move.new_figure

    # Метод производит откат последнего хода из списка ходов
    def cancel_move(self):
        if self.get_moves_count() == 0:
            return
        # Получаем последний ход
        last_move = self.move_list.pop(-1)
        move = last_move
        return move

    #Метод возвращает True, если поле (row, col) находится под ударом фигур стороны side
    def is_strike_cell(self, row, col, side):
        work_list = self.figures_dict[side]
        for figure in work_list:
            if figure.is_drop:
                continue
            figure_type = type(figure)
            if figure_type == Di:
                actions = figure.get_actions(DI_MOVES)
            else:
                actions = figure.get_actions()
            for r, c in actions:
                if r == row and c == col:
                    return True

        return False

    # Метод возвращает True, если фигрура находится под ударом фигур противоположной стороны
    def is_strike_figure(self, figure):
        return self.is_strike_cell(figure.row, figure.col, OPPOSITE_SIDE[figure.side])

    # Метод возвращает True, если фигура уже ходила
    def was_move(self, figure):
        for move in self.move_list:
            if figure == move.figure:
                return True
        return False

    # Метод возвращает фигуру, стоящую на клетке r, c
    def get_figure(self, r, c):
        if c <=7:
            return self.cells[r][c]


class SelectorBoardWhiteOkta:
    def __init__(self, side, main_board):
        self.whiteokta = WhiteOkta(4, 3, side, main_board)
    def get_figure(self, r, c):
        if r == 4 and c == 3:
            return self.whiteokta

class SelectorBoardBlackOkta:
    def __init__(self, side, main_board):
        self.blackokta = BlackOkta(4, 3, side, main_board)
    def get_figure(self, r, c):
        if r == 4 and c == 3:
            return self.blackokta

class SelectorBoardWhiteTetra:
    def __init__(self, side, main_board):
        self.whitetetra = WhiteTetra(4, 3, side, main_board)
    def get_figure(self, r, c):
        if r == 4 and c == 3:
            return self.whitetetra
class SelectorBoardBlackTetra:
    def __init__(self, side, main_board):
        self.blacktetra = BlackTetra(4, 3, side, main_board)
    def get_figure(self, r, c):
        if r == 4 and c == 3:
            return self.blacktetra
class SelectorBoardWhiteTri:
    def __init__(self, side, main_board):
        self.whitetri = WhiteTri(4, 3, side, main_board)
    def get_figure(self, r, c):
        if r == 4 and c == 3:
            return self.whitetri

class SelectorBoardBlackTri:
    def __init__(self, side, main_board):
        self.blacktri = BlackTri(4, 3, side, main_board)
    def get_figure(self, r, c):
        if r == 4 and c == 3:
            return self.blacktri

class SelectorBoardBlackUgol:
    def __init__(self, side, main_board):
        self.blackugol = BlackUgol(4, 3, side, main_board)
    def get_figure(self, r, c):
        if r == 4 and c == 3:
            return self.blackugol

class SelectorBoardWhiteUgol:
    def __init__(self, side, main_board):
        self.whiteugol = WhiteUgol(4, 3, side, main_board)
    def get_figure(self, r, c):
        if r == 4 and c == 3:
            return self.whiteugol

class SelectorBoardWhiteDi:
    def __init__(self, side, main_board):
        self.whitedi = WhiteDi(4, 3, side, main_board)
    def get_figure(self, r, c):
        if r == 4 and c == 3:
            return self.whitedi

class SelectorBoardBlackDi:
    def __init__(self, side, main_board):
        self.blackdi = BlackDi(4, 3, side, main_board)
    def get_figure(self, r, c):
        if r == 4 and c == 3:
            return self.blackdi
class SelectorBoardWhiteMono:
    def __init__(self, side, main_board):
        self.whitemono = WhiteMono(4, 3, side, main_board)
    def get_figure(self, r, c):
        if r == 4 and c == 3:
            return self.whitemono

class SelectorBoardBlackMono:
    def __init__(self, side, main_board):
        self.blackmono = BlackMono(4, 3, side, main_board)
    def get_figure(self, r, c):
        if r == 4 and c == 3:
            return self.blackmono

class SelectorBoardWhiteMoksha:
    def __init__(self, side, main_board):
        self.whitemoksha = WhiteMoksha(4, 3, side, main_board)
    def get_figure(self, r, c):
        if r == 4 and c == 3:
            return self.whitemoksha

class SelectorBoardBlackMoksha:
    def __init__(self, side, main_board):
        self.blackmoksha = BlackMoksha(4, 3, side, main_board)
    def get_figure(self, r, c):
        if r == 4 and c == 3:
            return self.blackmoksha