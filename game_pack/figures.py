import os
import pygame
from game_pack.params import *


class Figure(pygame.sprite.Sprite):

    def __init__(self, filename, r, c, side, board):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.dirname(__file__) + '/' + filename).convert_alpha()
        self.rect = self.image.get_rect(topleft=(c * CELL_SIZE, r * CELL_SIZE))
        self.row = r
        self.col = c
        self.side = side
        self.board = board
        self.is_drop = False

    def set_pos(self, r, c):
        self.row = r
        self.col = c
        self.rect.left = c * CELL_SIZE
        self.rect.top = r * CELL_SIZE


    @staticmethod
    def is_valid_pos(r, c):
        if 0 <= r <= 7 and 0 <= c <= 7:
            return True
        else:
            return False



class WhiteOkta(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'sprites/whiteOkta.png', r, c, side, board)
        if self.board.pl_side == BLACK:
            self.image = pygame.transform.rotate(self.image, 180)
    def get_actions(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
        for delta_row, delta_col in offsets:
            mul = 0
            while True:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
    def get_actions90(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while True:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
    def get_actions180(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while True:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
    def get_actions270(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while True:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result

class BlackOkta(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'sprites/blackOkta.png', r, c, side, board)
        if self.board.pl_side == side:
            self.image = pygame.transform.rotate(self.image, 180)
    def get_actions(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while True:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
    def get_actions90(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while True:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
    def get_actions180(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while True:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
    def get_actions270(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while True:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
class WhiteUgol(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'sprites/whiteUgol.png', r, c, side, board)
        if self.board.pl_side == BLACK:
            self.image = pygame.transform.rotate(self.image, 180)
    def get_actions(self):
        result = []
        if self.board.pl_side == BLACK:
            offsets = [(1, 0), (0, -1)]
        else:
            offsets = [(-1, 0), (0, 1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 2:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                # здесь задается фигура-преграда на пути
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
    def get_actions90(self):
        result = []
        offsets = [(1, 0), (0, 1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 2:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                # здесь задается фигура-преграда на пути
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
    def get_actions180(self):
        result = []
        offsets = [(1, 0), (0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 2:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                # здесь задается фигура-преграда на пути
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result

    def get_actions270(self):
        result = []
        offsets = [(-1, 0), (0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 2:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                # здесь задается фигура-преграда на пути
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
class BlackUgol(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'sprites/blackUgol.png', r, c, side, board)
        if self.board.pl_side == side:
            self.image = pygame.transform.rotate(self.image, 180)
    def get_actions(self):
        result = []
        if self.board.pl_side == BLACK:
            offsets = [(-1, 0), (0, 1)]
        else:
            offsets = [(1, 0), (0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 2:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result

    def get_actions90(self):
        result = []
        offsets = [(-1, 0), (0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 2:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result

    def get_actions180(self):
        result = []
        offsets = [(-1, 0), (0, 1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 2:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result

    def get_actions270(self):
        result = []
        offsets = [(1, 0), (0, 1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 2:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
class WhiteTri(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'sprites/whiteTri.png', r, c, side, board)
        if self.board.pl_side == BLACK:
            self.image = pygame.transform.rotate(self.image, 180)
    def get_actions(self):
        result = []
        if self.board.pl_side == BLACK:
            offsets = [(1, 0), (0, -1), (0, 1)]
        else:
            offsets = [(0, 1), (0, -1), (-1, 0)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 3:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
    def get_actions90(self):
        result = []
        offsets = [(0, 1), (-1, 0), (1, 0)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 3:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
    def get_actions180(self):
        result = []
        offsets = [(1, 0), (0, -1), (0, 1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 3:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
    def get_actions270(self):
        result = []
        offsets = [(-1, 0), (0, -1), (1, 0)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 3:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
class BlackTri(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'sprites/blackTri.png', r, c, side, board)
        if self.board.pl_side == side:
            self.image = pygame.transform.rotate(self.image, 180)
    def get_actions(self):
        result = []
        if self.board.pl_side == BLACK:
            offsets = [(0, 1), (0, -1), (-1, 0)]
        else:
            offsets = [(1, 0), (0, -1), (0, 1)]


        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 3:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
    def get_actions90(self):
        result = []
        offsets = [(1, 0), (0, -1), (-1, 0)]


        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 3:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
    def get_actions180(self):
        result = []
        offsets = [(0, 1), (0, -1), (-1, 0)]


        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 3:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result

    def get_actions270(self):
        result = []
        offsets = [(1, 0), (0, 1), (-1, 0)]


        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 3:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
class WhiteTetra(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'sprites/whiteTetra.png', r, c, side, board)
        if self.board.pl_side == BLACK:
            self.image = pygame.transform.rotate(self.image, 180)
    def get_actions(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 4:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result

    def get_actions90(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 4:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result

    def get_actions180(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 4:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result

    def get_actions270(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 4:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
class BlackTetra(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'sprites/blackTetra.png', r, c, side, board)
        if self.board.pl_side == side:
            self.image = pygame.transform.rotate(self.image, 180)
    def get_actions(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 4:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result

    def get_actions90(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 4:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result

    def get_actions180(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 4:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result

    def get_actions270(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 4:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
class WhiteDi(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'sprites/whiteDi.png', r, c, side, board)
        if self.board.pl_side == BLACK:
            self.image = pygame.transform.rotate(self.image, 180)
    def get_actions(self):
        result = []
        offsets = [(-1, 0), (1, 0)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 2:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result

    def get_actions90(self):
        result = []
        offsets = [(0, 1), (0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 2:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result

    def get_actions180(self):
        result = []
        offsets = [(-1, 0), (1, 0)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 2:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result

    def get_actions270(self):
        result = []
        offsets = [(0, 1), (0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 2:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break
        return result
class BlackDi(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'sprites/blackDi.png', r, c, side, board)
        if self.board.pl_side == side:
            self.image = pygame.transform.rotate(self.image, 180)
    def get_actions(self):
        result = []
        offsets = [(-1, 0), (1, 0)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 2:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result

    def get_actions90(self):
        result = []
        offsets = [(0, 1), (0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 2:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result

    def get_actions180(self):
        result = []
        offsets = [(-1, 0), (1, 0)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 2:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result

    def get_actions270(self):
        result = []
        offsets = [(0, 1), (0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 2:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break


        return result
class WhiteMono(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'sprites/whiteMono.png', r, c, side, board)
        if self.board.pl_side == BLACK:
            self.image = pygame.transform.rotate(self.image, 180)
    def get_actions(self):
        result = []
        if self.board.pl_side == BLACK:
            offsets = [(1, 0)]
        else:
            offsets = [(-1, 0)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 1:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result

    def get_actions90(self):
        result = []
        offsets = [(0, 1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 1:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result

    def get_actions180(self):
        result = []
        offsets = [(1, 0)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 1:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result

    def get_actions270(self):
        result = []
        offsets = [(0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 1:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result
class BlackMono(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'sprites/blackMono.png', r, c, side, board)
        if self.board.pl_side == side:
            self.image = pygame.transform.rotate(self.image, 180)


    def get_actions(self):
        result = []
        if self.board.pl_side == BLACK:
            offsets = [(-1, 0)]
        else:
            offsets = [(1, 0)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 1:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result

    def get_actions90(self):
        result = []
        offsets = [(0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 1:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result

    def get_actions180(self):
        result = []
        offsets = [(-1, 0)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 1:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result

    def get_actions270(self):
        result = []
        offsets = [(0, 1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while mul != 1:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result
class BlackMoksha(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'sprites/blackMoksha.png', r, c, side, board)

    def get_actions(self):
        result = []
        for r1 in range(0, 8):
            for c1 in range(0, 8):
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result

    def get_actions90(self):
        result = []
        for r1 in range(0, 8):
            for c1 in range(0, 8):
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result

    def get_actions180(self):
        result = []
        for r1 in range(0, 8):
            for c1 in range(0, 8):
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result

    def get_actions270(self):
        result = []
        for r1 in range(0, 8):
            for c1 in range(0, 8):
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result
class WhiteMoksha(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'sprites/whiteMoksha.png', r, c, side, board)

    def get_actions(self):
        result = []
        for r1 in range(0, 8):
            for c1 in range(0, 8):
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result
    def get_actions90(self):
        result = []
        for r1 in range(0, 8):
            for c1 in range(0, 8):
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result

    def get_actions180(self):
        result = []
        for r1 in range(0, 8):
            for c1 in range(0, 8):
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result

    def get_actions270(self):
        result = []
        for r1 in range(0, 8):
            for c1 in range(0, 8):
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        return result
