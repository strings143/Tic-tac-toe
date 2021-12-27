import pygame
import pygame as pg
import sys
import random
# 初始化模块，加一下稳一些
pygame.init()
playgame = True
width=600
height=600
# 创建屏幕对象
screen = pygame.display.set_mode((width, height))
# 界面背景颜色渲染，放在while中会不断覆盖格子
screen.fill((215, 191, 227))

# 界面的标题
pygame.display.set_caption('OOXX')
# width、height已经给出
# 长/宽的三分之一，为一个格子的长宽
single = width/3    #格子
radius=single/2     #圈圈
half=radius/2       #叉叉
# 表示九个格子
#pygame.draw.rect(畫布, 顏色, [x坐標, y坐標, 寬度, 高度], 線寬) --> 格子
rect = [0]*9
rect[0] = pygame.draw.rect(screen,(118,96,144),((0,0),(single,single)),width=2)
rect[1] = pygame.draw.rect(screen,(118,96,144),((single,0),(single,single)),width=2)
rect[2] = pygame.draw.rect(screen,(118,96,144),((single*2,0),(single,single)),width=2)
rect[3] = pygame.draw.rect(screen,(118,96,144),((0,single),(single,single)),width=2)
rect[4] = pygame.draw.rect(screen,(118,96,144),((single,single),(single,single)),width=2)
rect[5] = pygame.draw.rect(screen,(118,96,144),((single*2,single),(single,single)),width=2)
rect[6] = pygame.draw.rect(screen,(118,96,144),((0,single*2),(single,single)),width=2)
rect[7] = pygame.draw.rect(screen,(118,96,144),((single,single*2),(single,single)),width=2)
rect[8] = pygame.draw.rect(screen,(118,96,144),((single*2,single*2),(single,single)),width=2)

def draw_O(Num):
    if (Num == 0):
        pygame.draw.circle(screen, (118, 96, 144), (radius, radius), (single /3), width=5)
    elif(Num==1):
        pygame.draw.circle(screen, (118, 96, 144), (radius * 3, radius), (single / 3), width=5)
    elif(Num==2):
        pygame.draw.circle(screen, (118, 96, 144), (radius * 5, radius), (single / 3), width=5)
    elif (Num == 3):
        pygame.draw.circle(screen, (118, 96, 144), (radius, radius * 3), (single / 3), width=5)
    elif (Num == 4):
        pygame.draw.circle(screen, (118, 96, 144), (radius * 3, radius * 3), (single / 3), width=5)
    elif (Num == 5):
        pygame.draw.circle(screen, (118, 96, 144), (radius * 5, radius * 3), (single / 3), width=5)
    elif (Num == 6):
        pygame.draw.circle(screen, (118, 96, 144), (radius, radius * 5), (single / 3), width=5)
    elif (Num == 7):
        pygame.draw.circle(screen, (118, 96, 144), (radius * 3, radius * 5), (single / 3), width=5)
    elif (Num == 8):
        pygame.draw.circle(screen, (118, 96, 144), (radius * 5, radius * 5), (single / 3), width=5)

def draw_X(Num):
    if (Num == 0):
        pygame.draw.line(screen, (118, 96, 144), (half, half), (half * 3, half * 3), width=5)
        pygame.draw.line(screen, (118, 96, 144), (half * 3, half), (half, half * 3), width=5)
    elif(Num==1):
        pygame.draw.line(screen, (118, 96, 144), (half * 5, half), (half * 7, half * 3), width=5)
        pygame.draw.line(screen, (118, 96, 144), (half * 5, half * 3), (half * 7, half), width=5)
    elif(Num==2):
        pygame.draw.line(screen, (118, 96, 144), (half * 9, half), (half * 11, half * 3), width=5)
        pygame.draw.line(screen, (118, 96, 144), (half * 9, half * 3), (half * 11, half), width=5)
    elif (Num == 3):
        pygame.draw.line(screen, (118, 96, 144), (half, half * 5), (half * 3, half * 7), width=5)
        pygame.draw.line(screen, (118, 96, 144), (half * 3, half * 5), (half, half * 7), width=5)
    elif (Num == 4):
        pygame.draw.line(screen, (118, 96, 144), (half * 5, half * 5), (half * 7, half * 7), width=5)
        pygame.draw.line(screen, (118, 96, 144), (half * 5, half * 7), (half * 7, half * 5), width=5)
    elif (Num == 5):
        pygame.draw.line(screen, (118, 96, 144), (half * 9, half * 5), (half * 11, half * 7), width=5)
        pygame.draw.line(screen, (118, 96, 144), (half * 9, half * 7), (half * 11, half * 5), width=5)
    elif (Num == 6):
        pygame.draw.line(screen, (118, 96, 144), (half, half * 9), (half * 3, half * 11), width=5)
        pygame.draw.line(screen, (118, 96, 144), (half * 3, half * 9), (half, half * 11), width=5)
    elif (Num == 7):
        pygame.draw.line(screen, (118, 96, 144), (half * 5, half * 9), (half * 7, half * 11), width=5)
        pygame.draw.line(screen, (118, 96, 144), (half * 5, half * 11), (half * 7, half * 9), width=5)
    elif (Num == 8):
        pygame.draw.line(screen, (118, 96, 144), (half * 9, half * 9), (half * 11, half * 11), width=5)
        pygame.draw.line(screen, (118, 96, 144), (half * 9, half * 11), (half * 11, half * 9), width=5)

def goFirst():
    if random.randint(0,1) == 0:
        return "player1"
    else:
        return "player2"

def freeSpace(board, pos):
    return board[pos] == ' '

def goPos(board, symbol, pos):
    board[pos] = symbol

def isFull(board):
    for i in range(1, 10):
        if freeSpace(board, i):
            return False
    return True

def isWin(board, symbol):
    return ((board[1] == symbol and board[2] == symbol and board[3] == symbol) or
            (board[4] == symbol and board[5] == symbol and board[6] == symbol) or
            (board[7] == symbol and board[8] == symbol and board[9] == symbol) or
            (board[1] == symbol and board[4] == symbol and board[7] == symbol) or
            (board[2] == symbol and board[5] == symbol and board[8] == symbol) or
            (board[3] == symbol and board[6] == symbol and board[9] == symbol) or
            (board[1] == symbol and board[5] == symbol and board[9] == symbol) or
            (board[3] == symbol and board[5] == symbol and board[7] == symbol))

while True:
    myBoard = [' '] * 10
    player1Symbol, player2Symbol = ['O', 'X']
    turn = goFirst()
    font = pg.font.SysFont("arial", 24)  # 字體大小
    prompt_surface = pg.Surface((width, height/20))  # 建立空的提示圖層
    people= pg.Surface((100, 30))  # 建立空的提示圖層
    while playgame:
        if (turn == "player1"):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for i in range(0,9):
                        if rect[i].collidepoint(mouse_x, mouse_y)and freeSpace(myBoard,i+1):
                            goPos(myBoard,player1Symbol,i+1)
                            draw_O(i)
                            people.fill((0,0,0))
                            people.blit(font.render("   player2", True, (188, 117, 255)),(0, 0))  # 印出誰贏
                            screen.blit(people, (0, height - height / 20))
                            if isWin(myBoard, player1Symbol):
                                prompt_surface.blit(font.render("P1 win!",True,(255,255,255)),(width / 2 -30,0))#印出誰贏
                                screen.blit(prompt_surface, (0, height-height/20))  # 印出提示圖層
                                playgame = False
                            else:
                                if isFull(myBoard):
                                    prompt_surface.blit(font.render("No one won...",True,(255,255,255)),(width / 2 -60,0))#印出沒人贏
                                    screen.blit(prompt_surface, (0, height-height/20))  # 印出提示圖層
                                    break
                                else:
                                    turn = "player2"
        elif (turn == "player2"):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for i in range(0, 9):
                        if rect[i].collidepoint(mouse_x, mouse_y) and freeSpace(myBoard,i+1):
                            goPos(myBoard, player2Symbol, i + 1)
                            draw_X(i)
                            people.fill((0, 0, 0))
                            people.blit(font.render("   player1", True, (188, 117, 255)), (0, 0))  # 印出誰贏
                            screen.blit(people, (0, height - height / 20))
                            if isWin(myBoard, player2Symbol):
                                prompt_surface.blit(font.render("P2 win!",True,(255,255,255)),(width / 2 -30,0))#印出誰贏
                                screen.blit(prompt_surface, (0,height-height/20))  # 印出提示圖層
                                playgame = False
                            else:
                                if isFull(myBoard):
                                    prompt_surface.blit(font.render("No one won...",True,(255,255,255)),(width / 2 -60,0))#印出沒人贏
                                    screen.blit(prompt_surface, (0,height-height/20))  # 印出提示圖層
                                    break
                                else:
                                    turn = "player1"
        pygame.display.flip()
    if(playgame==False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.display.update()


