import pygame, sys
import numpy as np





pygame.init()

WIDTH = 600
HEIGHT = WIDTH
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH//BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE//3
CIRCLE_WIDTH= 15
CIRCLE_COLOR =(234,123,42)
SPACE = SQUARE_SIZE//4
CROSS_WIDTH =25
# screen color 
COLOR = (225,10,225)
CROSS_COLOR =(66,66,66)
RED = (255,0,0)
LINE_COLOR = (25,25,255)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('XO')
screen.fill(COLOR)

board = np.zeros((BOARD_ROWS,BOARD_COLS))

 
# pygame.draw.line( screen ,RED,(10,10),(300,300),10)

def draw_lines():
    pygame.draw.line(screen,RED,(0,SQUARE_SIZE),(WIDTH,SQUARE_SIZE),LINE_WIDTH)
    pygame.draw.line(screen,RED,(0,2*SQUARE_SIZE),(WIDTH,2*SQUARE_SIZE),LINE_WIDTH)
    pygame.draw.line(screen,RED,(SQUARE_SIZE,0),(SQUARE_SIZE,WIDTH),LINE_WIDTH)
    pygame.draw.line(screen,RED,(2*SQUARE_SIZE,0),(2*SQUARE_SIZE,WIDTH),LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen,CIRCLE_COLOR,(int(col*SQUARE_SIZE+SQUARE_SIZE//2),int(row*SQUARE_SIZE+SQUARE_SIZE//2)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][col] ==2:
                pygame.draw.line(screen,CROSS_COLOR,(col*SQUARE_SIZE+SPACE,row*SQUARE_SIZE+SQUARE_SIZE-SPACE),(col*SQUARE_SIZE+SQUARE_SIZE-SPACE,row*SQUARE_SIZE+SPACE),CROSS_WIDTH)
                pygame.draw.line(screen,CROSS_COLOR,(col*SQUARE_SIZE+SPACE,row*SQUARE_SIZE+SPACE),(col*SQUARE_SIZE+SQUARE_SIZE-SPACE,row*SQUARE_SIZE+SQUARE_SIZE-SPACE),CROSS_WIDTH)
                
def mark_square(row,col,player):
    board[row][col] = player

def ava(row,col):
    return board[row][col] == 0 

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True
def winner(player):
    # check vertical
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            vertical_winnner(col,player)
            return True
    # check horizontal
    for row in range(BOARD_ROWS):
        if board[row][0] ==player and board[row][1] == player and board[row][2] == player: 
            horizontal_winner(row,player)
            return True
    # check asc
    if board[2][0]==player and board[1][1] ==player and board[0][2]==player:
        draw_asc_dia(player)
        return True
    #  check desc
    if board[0][0]==player and board[1][1] ==player and board[2][2]==player:
        draw_desc_dia(player)
        return True 
    return False

def vertical_winnner(col,player):
    posX = col*SQUARE_SIZE +SQUARE_SIZE//2
    if player ==1:
        color = CIRCLE_COLOR
    elif player == 2 :
        color = CROSS_COLOR
    pygame.draw.line(screen,color,(posX,15),(posX,HEIGHT-15),15)


def horizontal_winner(row,player):
    posY = row*SQUARE_SIZE +SQUARE_SIZE//2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2 :
        color = CROSS_COLOR
    pygame.draw.line(screen,color,(15,posY),(WIDTH-15,posY),15)
def draw_asc_dia(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2 :
        color = CROSS_COLOR
    pygame.draw.line(screen,color,(15,HEIGHT-15),(WIDTH-15,15),15)

def draw_desc_dia(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2 :
        color = CROSS_COLOR

    pygame.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT-15),15)
def restart():
    screen.fill(COLOR)
    draw_lines()
    player =1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
draw_lines()



player = 1
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row =int(mouseY//SQUARE_SIZE)
            clicked_col =int(mouseX//SQUARE_SIZE)


            if ava(clicked_row,clicked_col):
                mark_square(clicked_row,clicked_col,player)
                if winner(player):
                    game_over=True
                player = player % 2 + 1
                draw_figures()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
            

 
            

        
                
    pygame.display.update()