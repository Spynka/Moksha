from game_pack.boards import *
from game_pack.ai import *
import pygame
import sys
from game_pack.button import Button
import simpleaudio as sa
sound = sa.WaveObject.from_wave_file('game_pack/assets/пуньк.wav')
sound_pobeda = sa.WaveObject.from_wave_file('game_pack/assets/pobeda.wav')
sound_defeat = sa.WaveObject.from_wave_file('game_pack/assets/defeat.wav')
sound_mimo = sa.WaveObject.from_wave_file('game_pack/assets/mimo.wav')
sound_peredacha = sa.WaveObject.from_wave_file('game_pack/assets/peredacha.wav')
sound_fon = sa.WaveObject.from_wave_file('game_pack/assets/фон.wav')
sound_menu = sa.WaveObject.from_wave_file('game_pack/assets/меню.wav')
pygame.init()
# Параметры экрана
WIDTH, HEIGHT = 1600, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


# Текущий холст
surface = None

# Текущее игровое поле
board = None

# Выделенная пользователем фигура
selected_figure = None

# Выделенная пользователем фигура противника
protivnika_figure = None

# Список доступных ходов
avl_moves = []

# Выбранный ход
selected_move = None

# Сообщение
msg = None
text_conv = None

BG = pygame.image.load("game_pack/assets/Background.png")
BGG = pygame.image.load("game_pack/assets/Players-vmake.jpg")
SP1 = pygame.image.load("game_pack/assets/SP1.png")
SP2 = pygame.image.load("game_pack/assets/SP2.png")
SP3 = pygame.image.load("game_pack/assets/SP3.png")
SP4 = pygame.image.load("game_pack/assets/SP4.png")
SP5 = pygame.image.load("game_pack/assets/SP5.png")
SP6 = pygame.image.load("game_pack/assets/SP6.png")
IG = pygame.image.load("game_pack/assets/Igra.png")
POBEDA = pygame.image.load("game_pack/assets/Pobeda.png")
defeat = pygame.image.load("game_pack/assets/defeat.png")


def get_font(size):
    return pygame.font.Font("game_pack/assets/19843.otf", size)

def play_game():
    while True:
        SCREEN.blit(BGG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(60).render("Выберите кол-во игроков", True, "#d0f0c0")
        MENU_RECT = MENU_TEXT.get_rect(center=(320, 150))
        ONE_PLAYER_BUTTON = Button(image=pygame.image.load("game_pack/assets/Play Rect.png"), pos=(320, 300),
                             text_input="1 игрок", font=get_font(75), base_color="#d0f0c0", hovering_color="White")
        TWO_PLAYERS_BUTTON = Button(image=pygame.image.load("game_pack/assets/Options Rect.png"), pos=(320, 420),
                                text_input="2 игрока", font=get_font(75), base_color="#d0f0c0",
                                hovering_color="White")
        BACK_BUTTON = Button(image=pygame.image.load("game_pack/assets/Options Rect.png"), pos=(320, 700),
                             text_input="Назад", font=get_font(75), base_color="#d0f0c0",
                             hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [ONE_PLAYER_BUTTON, TWO_PLAYERS_BUTTON, BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ONE_PLAYER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    one_player()
                if TWO_PLAYERS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    name_gamers()
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
        pygame.display.update()
def name_gamers():
    # Переменные для ввода имен
    player1_name = ""
    player2_name = ""
    input_player1 = True
    # Основной цикл ввода
    running = True
    while running:
        SCREEN.blit(BGG, (0, 0))
        MENU_TEXT = get_font(60).render("Введите Ваши имена", True, "#d0f0c0")
        MENU_RECT = MENU_TEXT.get_rect(center=(320, 150))

        BACK_BUTTON = Button(image=None, pos=(120, 700),
                             text_input="Назад", font=get_font(55), base_color="#d0f0c0",
                             hovering_color="White")
        NEXT_BUTTON = Button(image=None, pos=(520, 700),
                             text_input="В игру", font=get_font(55), base_color="#d0f0c0",
                             hovering_color="White")
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        for button in [NEXT_BUTTON, BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        if input_player1:
            player1_text = get_font(55).render(f"Игрок 1: {player1_name}_", True, "White")
        else:
            player1_text = get_font(55).render(f"Игрок 1: {player1_name}", True, "White")
        player2_text = get_font(55).render(f"Игрок 2: {player2_name}", True, "White")
        SCREEN.blit(player1_text, (100, 350))
        SCREEN.blit(player2_text, (100, 450))
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                if NEXT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    two_players(player1_name, player2_name)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if input_player1:
                    if event.key == pygame.K_BACKSPACE:
                        player1_name = player1_name[:-1]
                    elif event.key == pygame.K_RETURN:
                        input_player1 = False
                    else:
                        player1_name += event.unicode
                else:
                    if event.key == pygame.K_BACKSPACE:
                        player2_name = player2_name[:-1]
                    elif event.key == pygame.K_RETURN:
                         two_players(player1_name, player2_name)
                    else:
                        player2_name += event.unicode
    return player1_name, player2_name

def one_player():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BGG, (0, 0))
        PLAY_TEXT = get_font(45).render("Выберите цвет", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(320, 65))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_WHITE = Button(image=None, pos=(320, 300),
                           text_input="Светлая сторона", font=get_font(65), base_color="White", hovering_color="Black")
        PLAY_BLACK = Button(image=None, pos=(320, 410),
                            text_input="Темная сторона", font=get_font(65), base_color="Black",
                            hovering_color="White")
        PLAY_BACK = Button(image=None, pos=(320, 700),
                           text_input="Я все-таки пойду...", font=get_font(65), base_color="White", hovering_color="Green")
        PLAY_WHITE.changeColor(PLAY_MOUSE_POS)
        PLAY_WHITE.update(SCREEN)
        PLAY_BLACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BLACK.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BLACK.checkForInput(PLAY_MOUSE_POS):
                    start_ai(BLACK)
                if PLAY_WHITE.checkForInput(PLAY_MOUSE_POS):
                    start_ai(WHITE)
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    play_game()
        pygame.display.update()

def two_players(player1_name, player2_name):
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BGG, (0, 0))
        PLAY_TEXT = get_font(45).render("Игрок "+ player1_name +" выберите цвет", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(320, 60))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_WHITE = Button(image=None, pos=(320, 300),
                           text_input="Светлая сторона", font=get_font(65), base_color="White", hovering_color="Black")
        PLAY_BLACK = Button(image=None, pos=(320, 410),
                            text_input="Темная сторона", font=get_font(65), base_color="Black",
                            hovering_color="White")
        PLAY_BACK = Button(image=None, pos=(320, 700),
                           text_input="Я все-таки пойду...", font=get_font(65), base_color="White", hovering_color="Green")

        PLAY_WHITE.changeColor(PLAY_MOUSE_POS)
        PLAY_WHITE.update(SCREEN)
        PLAY_BLACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BLACK.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BLACK.checkForInput(PLAY_MOUSE_POS):
                    start(BLACK,player1_name, player2_name)
                if PLAY_WHITE.checkForInput(PLAY_MOUSE_POS):
                    start(WHITE,player1_name, player2_name)
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    play_game()
        pygame.display.update()

def pobeda():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(POBEDA, (10, 5))
        PLAY_BACK = Button(image=pygame.image.load("game_pack/assets/Play Rect.png"), pos=(1380, 730),
                           text_input="Вернуться в меню", font=get_font(45), base_color="White",
                           hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
        pygame.display.update()

def defeat():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(defeat, (0, 0))
        PLAY_BACK = Button(image=pygame.image.load("game_pack/assets/Options Rect.png"), pos=(1220, 730),
                           text_input="Вернуться в меню", font=get_font(65), base_color="White",
                           hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
        pygame.display.update()
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(SP1, (0, 0))
        OPTIONS_INS = Button(image=None, pos=(780, 470),
                              text_input="Прочесть инструкцию", font=get_font(45), base_color="Black", hovering_color="Green")
        OPTIONS_BACK = Button(image=pygame.image.load("game_pack/assets/Play Rect.png"), pos=(780, 700),
                              text_input="Назад", font=get_font(45), base_color="Black", hovering_color="Green")
        OPTIONS_INS.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_INS.update(SCREEN)
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_INS.checkForInput(OPTIONS_MOUSE_POS):
                    options1()
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        pygame.display.update()
def options1():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(SP2, (0, 0))
        OPTIONS_INS = Button(image=pygame.image.load("game_pack/assets/Play Rect.png"), pos=(1380, 700),
                              text_input="Далее", font=get_font(45), base_color="Black", hovering_color="Green")
        OPTIONS_BACK = Button(image=pygame.image.load("game_pack/assets/Play Rect.png"), pos=(220, 700),
                              text_input="Назад", font=get_font(45), base_color="Black", hovering_color="Green")
        OPTIONS_PLAY = Button(image=None, pos=(780, 700),
                              text_input="В игру", font=get_font(45), base_color="Black", hovering_color="Green")
        OPTIONS_INS.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_INS.update(SCREEN)
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        OPTIONS_PLAY.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_PLAY.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_INS.checkForInput(OPTIONS_MOUSE_POS):
                    options2()
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if OPTIONS_PLAY.checkForInput(OPTIONS_MOUSE_POS):
                    play_game()
        pygame.display.update()
def options2():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(SP3, (0, 0))
        OPTIONS_INS = Button(image=pygame.image.load("game_pack/assets/Play Rect.png"), pos=(1380, 700),
                              text_input="Далее", font=get_font(45), base_color="Black", hovering_color="Green")
        OPTIONS_BACK = Button(image=pygame.image.load("game_pack/assets/Play Rect.png"), pos=(220, 700),
                              text_input="Назад", font=get_font(45), base_color="Black", hovering_color="Green")
        OPTIONS_PLAY = Button(image=None, pos=(780, 700),
                              text_input="В игру", font=get_font(45), base_color="Black", hovering_color="Green")
        OPTIONS_INS.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_INS.update(SCREEN)
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        OPTIONS_PLAY.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_PLAY.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_INS.checkForInput(OPTIONS_MOUSE_POS):
                    options3()
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    options1()
                if OPTIONS_PLAY.checkForInput(OPTIONS_MOUSE_POS):
                    play_game()
        pygame.display.update()

def options3():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(SP4, (0, 0))
        OPTIONS_INS = Button(image=pygame.image.load("game_pack/assets/Play Rect.png"), pos=(1380, 700),
                              text_input="Далее", font=get_font(45), base_color="Black", hovering_color="Green")
        OPTIONS_BACK = Button(image=pygame.image.load("game_pack/assets/Play Rect.png"), pos=(220, 700),
                              text_input="Назад", font=get_font(45), base_color="Black", hovering_color="Green")
        OPTIONS_PLAY = Button(image=None, pos=(780, 700),
                              text_input="В игру", font=get_font(45), base_color="Black", hovering_color="Green")
        OPTIONS_INS.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_INS.update(SCREEN)
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        OPTIONS_PLAY.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_PLAY.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_INS.checkForInput(OPTIONS_MOUSE_POS):
                    options4()
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    options2()
                if OPTIONS_PLAY.checkForInput(OPTIONS_MOUSE_POS):
                    play_game()
        pygame.display.update()
def options4():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(SP5, (0, 0))
        OPTIONS_INS = Button(image=pygame.image.load("game_pack/assets/Play Rect.png"), pos=(1380, 700),
                              text_input="Далее", font=get_font(45), base_color="Black", hovering_color="Green")
        OPTIONS_BACK = Button(image=pygame.image.load("game_pack/assets/Play Rect.png"), pos=(220, 700),
                              text_input="Назад", font=get_font(45), base_color="Black", hovering_color="Green")
        OPTIONS_PLAY = Button(image=None, pos=(780, 700),
                              text_input="В игру", font=get_font(45), base_color="Black", hovering_color="Green")
        OPTIONS_INS.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_INS.update(SCREEN)
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        OPTIONS_PLAY.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_PLAY.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_INS.checkForInput(OPTIONS_MOUSE_POS):
                    options5()
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    options3()
                if OPTIONS_PLAY.checkForInput(OPTIONS_MOUSE_POS):
                    play_game()
        pygame.display.update()
def options5():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(SP6, (0, 0))
        OPTIONS_INS = Button(image=pygame.image.load("game_pack/assets/Play Rect.png"), pos=(1380, 700),
                              text_input="Далее", font=get_font(45), base_color="Black", hovering_color="Green")
        OPTIONS_BACK = Button(image=pygame.image.load("game_pack/assets/Play Rect.png"), pos=(220, 700),
                              text_input="Назад", font=get_font(45), base_color="Black", hovering_color="Green")
        OPTIONS_PLAY = Button(image=None, pos=(780, 700),
                              text_input="В игру", font=get_font(45), base_color="Black", hovering_color="Green")
        OPTIONS_INS.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_INS.update(SCREEN)
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        OPTIONS_PLAY.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_PLAY.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_INS.checkForInput(OPTIONS_MOUSE_POS):
                    play_game()
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    options4()
                if OPTIONS_PLAY.checkForInput(OPTIONS_MOUSE_POS):
                    play_game()
        pygame.display.update()
def main_menu():
    pygame.mixer.music.load('game_pack/assets/меню.wav')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    while True:

        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(180).render("МОКША", True, "#b30000")
        MENU_RECT = MENU_TEXT.get_rect(center=(420, 150))
        PLAY_BUTTON = Button(image=pygame.image.load("game_pack/assets/Play Rect.png"), pos=(420, 370),
                             text_input="Играть", font=get_font(80), base_color="#d0f0c0", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("game_pack/assets/Options Rect.png"), pos=(420, 500),
                                text_input="Правила читать", font=get_font(80), base_color="#d0f0c0", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("game_pack/assets/Options Rect.png"), pos=(420, 630),
                             text_input="Пойти посуду мыть", font=get_font(80), base_color="#d0f0c0", hovering_color="White")
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_game()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


test = None
def __init__(self, side, board):
    self.side = side
    self.board = board
    current_side = side

def start(player_side, player1_name, player2_name):
    global surface, board, selected_figure, avl_moves, selected_move, mode, msg, text_conv, test
    pygame.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('game_pack/assets/фон.wav')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    # play = sound_fon.play()
    selected_figure_450 = None
    selected_figure_360 = None
    selected_figure_270 = None
    selected_figure_180 = None
    selected_figure_90 = None
    selected_figure_90_nov = None
    pygame.display.set_caption('Moksha')
    text_conv = ""
    WIDTH, HEIGHT = 1600, 800
    kol_vo_bl_moksha = 0
    kol_vo_wh_moksha = 0
    SCREEN.blit(IG, (0, 0))
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    mode_status = 0
    mode = 'mode_1'
    flag = None
    current_side = player_side
    main_board = Board(current_side)
    board = main_board
    k = 0
    t=0
    if current_side == WHITE:
        playername = player1_name
    else:
        playername = player2_name
    button = pygame.Rect(890, 260, 300, 50)
    text = pygame.Rect(50, 180, 800, 120)
    Exit = pygame.Rect(1200, 700, 300, 100)
    while True:
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Exit.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    main_menu()
                    break
                if button.collidepoint(event.pos):
                    if selected_figure is None:
                        play = sound_mimo.play()
                    if selected_figure is not None:
                        play = sound.play()
                        selected_figure.image, selected_figure.rect = rot_center(selected_figure.image,
                                                                                 selected_figure.rect, 270)
                        surface.blit(selected_figure.image, selected_figure.rect)
                        k += 90
                        t+=1
                        if selected_figure == selected_figure_270:
                            k=360
                            selected_figure_360 = selected_figure
                            avl_moves = povorot(selected_figure_360, k)
                        elif selected_figure == selected_figure_180:
                            k=270
                            selected_figure_270 = selected_figure
                            avl_moves = povorot(selected_figure_270, k)
                        elif selected_figure == selected_figure_90:
                            k=180
                            selected_figure_180 = selected_figure
                            avl_moves = povorot(selected_figure_180, k)
                        elif selected_figure == selected_figure_90_nov:
                            k=180
                            selected_figure_180 = selected_figure
                            avl_moves = povorot(selected_figure_180, k)
                        elif selected_figure == selected_figure_360:
                            k=90
                            selected_figure_450 = selected_figure
                            avl_moves = povorot(selected_figure_90, k)
                        elif t==1:
                            selected_figure_90 = selected_figure
                            avl_moves = povorot(selected_figure_90, k)
                        else:
                            selected_figure_90_nov = selected_figure
                            avl_moves = povorot(selected_figure_90_nov, k)

                        mode = 'mode_2'
                        continue
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button != 1:
                    continue
                # В режиме 1 разрешен только выбор фигур
                #  При выборе фигуры, получаем список доступных ходов для неё и если он не пуст - переходим в режим 2

                if mode == 'mode_1':
                    text_conv = ""
                    selected_figure = get_mouse_selected_figure_select(event, current_side)

                    if selected_figure is not None:
                        if selected_figure is selected_figure_360:
                            selected_figure_360 = selected_figure
                            k = 360
                            avl_moves = povorot(selected_figure_360, k)
                        elif selected_figure is selected_figure_270:
                            k = 270
                            selected_figure_270 = selected_figure
                            avl_moves = povorot(selected_figure_270, k)
                        elif selected_figure is selected_figure_180:
                            k = 180
                            selected_figure_180 = selected_figure
                            avl_moves = povorot(selected_figure_180, k)
                        elif selected_figure is selected_figure_450:
                            k = 90
                            selected_figure_450 = selected_figure
                            avl_moves = povorot(selected_figure_450, k)
                        elif selected_figure is selected_figure_90:
                            k = 90
                            selected_figure_90 = selected_figure
                            avl_moves = povorot(selected_figure_90, k)
                        elif selected_figure is selected_figure_90_nov:
                            k = 90
                            selected_figure_90_nov = selected_figure
                            avl_moves = povorot(selected_figure_90_nov, k)
                        else:
                            avl_moves = board.get_avl_moves_for_figure(selected_figure)
                        if avl_moves:
                            mode = 'mode_2'
                            continue

                # В режиме 2 разрешен выбор фигур и ходов
                # Если выбран ход-конверсия, то переходим в режим 3
                # Если выбран любой другой ход, то переходим в режим 4
                # Если выбрана другая фигура, то получаем её список доступных ходов
                if mode == 'mode_2':

                    selected_row, selected_col = get_mouse_selected_cell(event)
                    # Сперва проверяем, выбран ли ход
                    selected_move = None
                    for move in avl_moves:
                        if selected_row == move.new_row and selected_col == move.new_col:
                            selected_move = move
                            break

                    if selected_move is not None:
                        # Если ход выбран и это ход-конверсия, то переходим в режим 3

                        if keys[pygame.K_SPACE]:
                            text_conv = "Нажмите на фигуру для понижения уровня"
                            selected_move.m_type = CONVERSION

                            if current_side == WHITE:
                                current_side = BLACK
                                player_side = BLACK
                            elif current_side == BLACK:
                                current_side = WHITE
                                player_side = WHITE
                            else:
                                current_side = player_side
                            drop_selected_figure = get_mouse_selected_figure_select(event, current_side)

                            avl_moves = []
                            if current_side == WHITE:
                                current_side = BLACK
                                player_side = WHITE
                            elif current_side == BLACK:
                                current_side = WHITE
                                player_side = BLACK
                            if type(selected_figure) == WhiteOkta:
                                board = SelectorBoardWhiteTetra(current_side, main_board)
                            elif type(selected_figure) == BlackOkta:
                                board = SelectorBoardBlackOkta(current_side, main_board)
                            elif type(selected_figure) == WhiteTetra:
                                board = SelectorBoardWhiteTri(current_side, main_board)
                            elif type(selected_figure) == BlackTetra:
                                board = SelectorBoardBlackTri(current_side, main_board)
                            elif type(selected_figure) == WhiteTri:
                                board = SelectorBoardWhiteUgol(current_side, main_board)
                            elif type(selected_figure) == BlackTri:
                                board = SelectorBoardBlackUgol(current_side, main_board)
                            elif type(selected_figure) == WhiteUgol:
                                board = SelectorBoardWhiteDi(current_side, main_board)
                            elif type(selected_figure) == BlackUgol:
                                board = SelectorBoardBlackDi(current_side, main_board)
                            elif type(selected_figure) == WhiteDi:
                                board = SelectorBoardWhiteMono(current_side, main_board)
                            elif type(selected_figure) == BlackDi:
                                board = SelectorBoardBlackMono(current_side, main_board)
                            elif type(selected_figure) == WhiteMono:
                                board = SelectorBoardWhiteMoksha(current_side, main_board)
                                kol_vo_wh_moksha += 1
                            elif type(selected_figure) == BlackMono:
                                board = SelectorBoardBlackMoksha(current_side, main_board)
                                kol_vo_bl_moksha += 1
                            mode = 'mode_3'
                            continue

                        # Если ход выбран и это не ход-конверсия, то переходим в режим 4
                        mode = 'mode_4'
                        continue

                    # Если выбрана фигура, то получаем ее список доступных ходов
                    new_selected_figure = get_mouse_selected_figure_select(event, current_side)
                    if new_selected_figure is not None:
                        selected_figure = new_selected_figure
                        if selected_figure is selected_figure_360:
                            selected_figure_360 = selected_figure
                            k = 360
                            avl_moves = povorot(selected_figure_360, k)
                        elif selected_figure is selected_figure_270:
                            k = 270
                            selected_figure_270 = selected_figure
                            avl_moves = povorot(selected_figure_270, k)
                        elif selected_figure is selected_figure_180:
                            k = 180
                            selected_figure_180 = selected_figure
                            avl_moves = povorot(selected_figure_180, k)
                        elif selected_figure is selected_figure_450:
                            k = 90
                            selected_figure_450 = selected_figure
                            avl_moves = povorot(selected_figure_450, k)
                        elif selected_figure is selected_figure_90:
                            k = 90
                            selected_figure_90 = selected_figure
                            avl_moves = povorot(selected_figure_90, k)
                        elif selected_figure is selected_figure_90_nov:
                            k = 90
                            selected_figure_90_nov = selected_figure
                            avl_moves = povorot(selected_figure_90_nov, k)
                        else:
                            avl_moves = board.get_avl_moves_for_figure(selected_figure)
                    continue

                # В режиме 3  нужно выбрать фигуру для хода конверсии
                # Если фигруа выбрана, то записываем её в объект хода и переходим в режим 4
                if mode == 'mode_3':
                    text_conv = "Нажмите на фигуру для повышения уровня"
                    selected_figure = get_mouse_selected_figure_select(event, current_side)
                    if selected_figure is not None:

                        selected_figure.set_pos(selected_move.new_row, selected_move.new_col)

                        selected_move.new_figure = selected_figure
                        if type(drop_selected_figure) == WhiteTetra:
                            board = SelectorBoardWhiteOkta(player_side, main_board)
                        elif type(drop_selected_figure) == BlackTetra:
                            board = SelectorBoardBlackOkta(player_side, main_board)
                        elif type(drop_selected_figure) == BlackOkta:
                            board = main_board
                            new_drop_figure = None
                            drop_selected_figure = None
                            mode = 'mode_4'
                            continue
                        elif type(drop_selected_figure) == WhiteOkta:
                            board = main_board
                            new_drop_figure = None
                            drop_selected_figure = None
                            mode = 'mode_4'
                            continue
                        elif type(drop_selected_figure) == WhiteTri:
                            board = SelectorBoardWhiteTetra(player_side, main_board)
                        elif type(drop_selected_figure) == BlackTri:
                            board = SelectorBoardBlackTetra(player_side, main_board)
                        elif type(drop_selected_figure) == WhiteUgol:
                            board = SelectorBoardWhiteTri(player_side, main_board)
                        elif type(drop_selected_figure) == BlackUgol:
                            board = SelectorBoardBlackTri(player_side, main_board)
                        elif type(drop_selected_figure) == WhiteDi:
                            board = SelectorBoardWhiteUgol(player_side, main_board)
                        elif type(drop_selected_figure) == BlackDi:
                            board = SelectorBoardBlackUgol(player_side, main_board)
                        elif type(drop_selected_figure) == WhiteMono:
                            board = SelectorBoardWhiteDi(player_side, main_board)
                        elif type(drop_selected_figure) == BlackMono:
                            board = SelectorBoardBlackDi(player_side, main_board)

                        mode = 'mode_3.1'
                        continue
                if mode == 'mode_3.1':
                    text_conv = "Нажмите на фигуру для повышения уровня соперника"
                    selected_figure = get_mouse_selected_figure_select(event, player_side)
                    if selected_figure is not None:
                        selected_figure.set_pos(selected_move.new_row, selected_move.new_col)
                        selected_move.new_drop_figure = selected_figure
                        board = main_board
                        play = sound_peredacha.play()
                        mode = 'mode_4'
                        continue

                # В режиме шесть игроку выведено сообщение о завершении игры и любой щелчок мышью приводит к выходу
                if mode == 'mode_6':
                    exit()

                if mode == 'mode_6.1':
                    pygame.mixer.music.stop()
                    play = sound_pobeda.play()
                    # board = main_board
                    pobeda()

                if mode == 'mode_6.2':
                    pygame.mixer.music.stop()
                    play = sound_defeat.play()
                    defeat()


        # Режим 4 не связан с событиями мыши или клавиатуры
        # В этом режиме происходит процесс применения хода игрока и проверка условия завешения игры
        if mode == 'mode_4':

            text_conv = ""

            board.apply_move(selected_move)
            selected_figure = None
            selected_move = None
            avl_moves = []
            if kol_vo_bl_moksha >= 1 or kol_vo_wh_moksha >= 1:
                pygame.mixer.music.stop()
                mode = 'mode_6.1'
                continue
                # Если игра не завершена, то перейти в режим 5
            mode = 'mode_5'
            repaint()

        # В режиме 5 происходит вычисление ответного хода компьютера и проверка его результатов
        # Если игра завершена, то происходит переход в режим 6
        # Если игра не завершена, то происходит переход в режим 1
        if mode == 'mode_5':
            play = sound.play()
            if current_side == WHITE:
                player_side = BLACK
                current_side = BLACK
                playername = player1_name
            elif current_side == BLACK:
                current_side = WHITE
                player_side = WHITE
                playername = player2_name
            else:
                current_side = player_side
            selected_figure = None
            selected_move = None
            # avl_moves = []
            score = "выполнил ход"
            addrecord(playername, score)
            records = getrecords()
            msg = 'Records:'
            for i, (playername, score) in enumerate(records, start=1):
                if playername == "":
                    msg = f'Игрок {score}'
                else:
                    msg = f'{playername} {score}'

            # Если игра не завершена, то перейтив режим 1
            k = 0
            mode = 'mode_1'
            if board.get_figures_count_pl() == 0 or board.get_figures_count_cmp() == 0:
                mode = 'mode_6.2'
                continue
        repaint()
        clock.tick(FPS)


## прошлая версия с компом :
def __init__(self, side, board):
    self.side = side
    self.board = board
def start_ai(player_side):
    global surface, board, selected_figure, avl_moves, selected_move, mode, msg, text_conv, test
    pygame.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('game_pack/assets/фон.wav')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    # play = sound_fon.play()
    selected_figure_450 = None
    selected_figure_360 = None
    selected_figure_270 = None
    selected_figure_180 = None
    selected_figure_90 = None
    selected_figure_90_nov = None
    pygame.display.set_caption('Moksha')
    text_conv = ""
    WIDTH, HEIGHT = 1600, 800
    kol_vo_bl_moksha = 0
    kol_vo_wh_moksha = 0
    SCREEN.blit(IG, (0, 0))
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    mode_status = 0
    mode = 'mode_1'
    flag = None
    current_side = player_side
    main_board = Board(current_side)
    board = main_board
    k = 0
    t=0
    computer_side = OPPOSITE_SIDE[player_side]
    # # Если компьютер играет белыми, то его ход должен быть первым, иначе - первым ходит игрок
    if computer_side == WHITE:
        mode = 'mode_5'
    else:
        mode = 'mode_1'
    mode = 'mode_1'
    # Создаем игровое поле
    main_board = Board(player_side)
    board = main_board
    # # Создаем объект, отвечающий за расчет ответного хода
    ai = Ai(computer_side, main_board)
    button = pygame.Rect(890, 260, 300, 50)
    text = pygame.Rect(50, 180, 800, 120)
    Exit = pygame.Rect(1200, 700, 300, 100)
    while True:
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Exit.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    main_menu()
                    break
                if button.collidepoint(event.pos):
                    if selected_figure is None:
                        play = sound_mimo.play()
                    if selected_figure is not None:
                        play = sound.play()
                        selected_figure.image, selected_figure.rect = rot_center(selected_figure.image,
                                                                                 selected_figure.rect, 270)
                        surface.blit(selected_figure.image, selected_figure.rect)
                        k += 90
                        t+=1
                        if selected_figure == selected_figure_270:
                            k=360
                            selected_figure_360 = selected_figure
                            avl_moves = povorot(selected_figure_360, k)
                        elif selected_figure == selected_figure_180:
                            k=270
                            selected_figure_270 = selected_figure
                            avl_moves = povorot(selected_figure_270, k)
                        elif selected_figure == selected_figure_90:
                            k=180
                            selected_figure_180 = selected_figure
                            avl_moves = povorot(selected_figure_180, k)
                        elif selected_figure == selected_figure_90_nov:
                            k=180
                            selected_figure_180 = selected_figure
                            avl_moves = povorot(selected_figure_180, k)
                        elif selected_figure == selected_figure_360:
                            k=90
                            selected_figure_450 = selected_figure
                            avl_moves = povorot(selected_figure_90, k)
                        elif t==1:
                            selected_figure_90 = selected_figure
                            avl_moves = povorot(selected_figure_90, k)
                        else:
                            selected_figure_90_nov = selected_figure
                            avl_moves = povorot(selected_figure_90_nov, k)

                        mode = 'mode_2'
                        continue
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button != 1:
                    continue
                # В режиме 1 разрешен только выбор фигур
                #  При выборе фигуры, получаем список доступных ходов для неё и если он не пуст - переходим в режим 2

                # if mode == 'mode_1':
                # В режиме 1 разрешен только выбор фигур
                #  При выборе фигуры, получаем список доступных ходов для неё и если он не пуст - переходим в режим 2
                if mode == 'mode_1':
                    # k=0
                    selected_figure = get_mouse_selected_figure(event, player_side)
                    if selected_figure is not None:
                        avl_moves = board.get_avl_moves_for_figure(selected_figure)
                        if avl_moves:
                            mode = 'mode_2'
                            continue

                # В режиме 2 разрешен выбор фигур и ходов
                # Если выбран ход-конверсия, то переходим в режим 3
                # Если выбран любой другой ход, то переходим в режим 4
                # Если выбрана другая фигура, то получаем её список доступных ходов
                if mode == 'mode_2':
                    selected_row, selected_col = get_mouse_selected_cell(event)
                    # Сперва проверяем, выбран ли ход
                    selected_move = None
                    for move in avl_moves:
                        if selected_row == move.new_row and selected_col == move.new_col:
                            selected_move = move
                            break

                    if selected_move is not None:
                        # Если ход выбран и это ход-конверсия, то переходим в режим 3
                        if selected_move is not None:
                            if keys[pygame.K_SPACE]:
                                selected_move.m_type = CONVERSION
                                drop_selected_figure = get_mouse_selected_figure(event, player_side)
                                avl_moves = []
                                if type(selected_figure) == WhiteOkta:
                                    board = SelectorBoardWhiteTetra(player_side, main_board)
                                elif type(selected_figure) == BlackOkta:
                                    board = SelectorBoardBlackOkta(player_side, main_board)
                                elif type(selected_figure) == WhiteTetra:
                                    board = SelectorBoardWhiteTri(player_side, main_board)
                                elif type(selected_figure) == BlackTetra:
                                    board = SelectorBoardBlackTri(player_side, main_board)
                                elif type(selected_figure) == WhiteTri:
                                    board = SelectorBoardWhiteUgol(player_side, main_board)
                                elif type(selected_figure) == BlackTri:
                                    board = SelectorBoardBlackUgol(player_side, main_board)
                                elif type(selected_figure) == WhiteUgol:
                                    board = SelectorBoardWhiteDi(player_side, main_board)
                                elif type(selected_figure) == BlackUgol:
                                    board = SelectorBoardBlackDi(player_side, main_board)
                                elif type(selected_figure) == WhiteDi:
                                    board = SelectorBoardWhiteMono(player_side, main_board)
                                elif type(selected_figure) == BlackDi:
                                    board = SelectorBoardBlackMono(player_side, main_board)
                                elif type(selected_figure) == WhiteMono:
                                    board = SelectorBoardWhiteMoksha(player_side, main_board)
                                    kol_vo_wh_moksha += 1
                                elif type(selected_figure) == BlackMono:
                                    board = SelectorBoardBlackMoksha(player_side, main_board)
                                    kol_vo_bl_moksha += 1
                                mode = 'mode_3'
                                continue
                        # Если ход выбран и это не ход-конверсия, то переходим в режим 4
                        mode = 'mode_4'
                        continue
                    # Если выбрана фигура, то получаем ее список доступных ходов
                    new_selected_figure = get_mouse_selected_figure(event, player_side)
                    if new_selected_figure is not None:
                        selected_figure = new_selected_figure
                        avl_moves = board.get_avl_moves_for_figure(selected_figure)
                    continue

                # В режиме 3  нужно выбрать фигуру для хода конверсии
                # Если фигруа выбрана, то записываем её в объект хода и переходим в режим 4
                if mode == 'mode_3':
                    selected_figure = get_mouse_selected_figure(event, player_side)
                    if selected_figure is not None:
                        selected_figure.set_pos(selected_move.new_row, selected_move.new_col)
                        selected_move.new_figure = selected_figure
                        if type(drop_selected_figure) == WhiteTetra:
                            board = SelectorBoardWhiteOkta(player_side, main_board)
                        elif type(drop_selected_figure) == BlackTetra:
                            board = SelectorBoardBlackOkta(player_side, main_board)
                        elif type(drop_selected_figure) == BlackOkta:
                            board = SelectorBoardBlackOkta(player_side, main_board)
                        elif type(drop_selected_figure) == WhiteOkta:
                            board = SelectorBoardWhiteOkta(player_side, main_board)
                        elif type(drop_selected_figure) == WhiteTri:
                            board = SelectorBoardWhiteTetra(player_side, main_board)
                        elif type(drop_selected_figure) == BlackTri:
                            board = SelectorBoardBlackTetra(player_side, main_board)
                        elif type(drop_selected_figure) == WhiteUgol:
                            board = SelectorBoardWhiteTri(player_side, main_board)
                        elif type(drop_selected_figure) == BlackUgol:
                            board = SelectorBoardBlackTri(player_side, main_board)
                        elif type(drop_selected_figure) == WhiteDi:
                            board = SelectorBoardWhiteUgol(player_side, main_board)
                        elif type(drop_selected_figure) == BlackDi:
                            board = SelectorBoardBlackUgol(player_side, main_board)
                        elif type(drop_selected_figure) == WhiteMono:
                            board = SelectorBoardWhiteDi(player_side, main_board)
                        elif type(drop_selected_figure) == BlackMono:
                            board = SelectorBoardBlackDi(player_side, main_board)
                        mode = 'mode_3.1'
                        continue
                if mode == 'mode_3.1':
                    selected_figure = get_mouse_selected_figure(event, player_side)
                    pygame.display.update()
                    if selected_figure is not None:
                        selected_figure.set_pos(selected_move.new_row, selected_move.new_col)
                        selected_move.new_drop_figure = selected_figure
                        board = main_board
                        mode = 'mode_4'
                        continue

                # В режиме шесть игроку выведено сообщение о завершении игры и любой щелчок мышью приводит к выходу
                if mode == 'mode_6':
                    exit()

        # Режим 4 не связан с событиями мыши или клавиатуры
        # В этом режиме происходит процесс применения хода игрока и проверка условия завешения игры
        if mode == 'mode_4':
            board.apply_move(selected_move)
            selected_figure = None
            selected_move = None
            avl_moves = []
            # Если игра не завершена, то перейти в режим 5
            mode = 'mode_5'
            repaint()

        # В режиме 5 происходит вычисление ответного хода компьютера и проверка его результатов
        # Если игра завершена, то происходит переход в режим 6
        # Если игра не завершена, то происходит переход в режим 1
        if mode == 'mode_5':
            move = ai.get_next_move()
            board.apply_move(move)
            selected_figure = None
            selected_move = None
            avl_moves = []
            mode = 'mode_1'
        repaint()
        clock.tick(FPS)

def povorot(selected_figure, k):
    if k == 360:
        avl_moves = board.get_avl_moves_for_figure(selected_figure)
    elif k == 270:
        avl_moves = board.get_avl_moves_for_figure270(selected_figure)
    elif k == 180:
        avl_moves = board.get_avl_moves_for_figure180(selected_figure)
    elif k == 90:
        avl_moves = board.get_avl_moves_for_figure90(selected_figure)
    else:
        avl_moves = board.get_avl_moves_for_figure(selected_figure)

    return avl_moves

def button():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    button = pygame.Rect(890, 260, 300, 50)
    pygame.draw.rect(surface, WHITE, button)
    text = get_font(45).render('Повернуть фигуру', True, BLACK)
    surface.blit(text, (button.x + 5, button.y + 5))

def Exit():
    WHITE = (255, 255, 255)
    BLACK = (77,77, 77)
    Exit = pygame.Rect(1200, 700, 255, 65)
    pygame.draw.rect(surface, BLACK, Exit)
    text = get_font(45).render('Выйти из игры', True, WHITE)
    surface.blit(text, (Exit.x + 5, Exit.y + 5))

def addrecord(playername, score):
    with open("records.txt", "a") as file:
        file.write(f"{playername},{score}\n")

def getrecords():
    records = []
    try:
        with (open("records.txt", "r") as file):
            for line in file:
                playername, score = line.strip().split(",")
                records.append((playername,score))
    except FileNotFoundError:
        pass
    # records.sort(key=lambda x: x[1], reverse=True)
    return records

def repaint():
    # Блок команд отрисовки

    draw_cells()
    draw_select_cell()
    draw_avl_moves(avl_moves)
    draw_figures()
    draw_msg()
    draw_text()
    button()
    Exit()
    pygame.display.update()

def draw_msg():
    if not msg:
        return
    msg_surface = get_font(45).render(msg, 1, "White")
    msg_rect = msg_surface.get_rect(topleft=(875, 80))
    surface.blit(msg_surface, msg_rect)

def draw_text():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    text = pygame.Rect(0, 150, 800, 120)
    text_conv_surface = get_font(45).render(text_conv, 1, "White")
    text_conv_rect = text_conv_surface.get_rect(topleft=(50, 180))
    if text_conv != "":
        pygame.draw.rect(surface, BLACK, text)
    surface.blit(text_conv_surface,text_conv_rect)
def rot_center(image, rect, angle):
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect

# Функция отрисовывает клетки доски
def draw_cells():
    SCREEN.blit(IG, (0, 0))
    for r in range(0, 8):
        for c in range(0, 8):
            if (r + c) % 2 == 0:
                color = WHITE_CELL_COLOR
            else:
                color = BLACK_CELL_COLOR
            pygame.draw.rect(surface, color, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Функция отрисовывает фигуры на доске
def draw_figures():

    for row in range(0, 8):
        for col in range(0, 8):
            figure = board.get_figure(row, col)
            if figure is None:
                continue
            surface.blit(figure.image, figure.rect)


# Функция отрисовывает выбранную игроком клетку
def draw_select_cell():
    if selected_figure:
        pygame.draw.rect(surface, SELECTED_CELL_COLOR,
                         (selected_figure.col * CELL_SIZE, selected_figure.row * CELL_SIZE, CELL_SIZE, CELL_SIZE))


# Функция отрисовывает клетки, доступные для хода выбранной фигурой
def draw_avl_moves(avl_moves):
    for move in avl_moves:
        row_move = move.new_row
        col_move = move.new_col
        pygame.draw.rect(surface, AVL_MOVE_CELL_COLOR,
                         (col_move * CELL_SIZE + 4, row_move * CELL_SIZE + 4, CELL_SIZE - 8, CELL_SIZE - 8))

    pass

# Функция определяет клетку, которую выбрал игрок
def get_mouse_selected_cell(mouse_event):
    c = mouse_event.pos[0] // CELL_SIZE
    r = mouse_event.pos[1] // CELL_SIZE
    return r, c

# Функция определяет фигуру, которую выбрал игрок
def get_mouse_selected_figure(mouse_event, side=None):
    selected_row, selected_col = get_mouse_selected_cell(mouse_event)
    figure = board.get_figure(selected_row, selected_col)
    if side is not None and figure is not None:
        if figure.side != side:
            return None
    return figure

def get_mouse_selected_figure_select(mouse_event, current_side = None):
    selected_row, selected_col = get_mouse_selected_cell(mouse_event)
    figure = board.get_figure(selected_row, selected_col)
    if figure is not None:
        if figure.side == current_side:
            return figure
        else:
            return None
    else:
        return None




