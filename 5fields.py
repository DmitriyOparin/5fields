# -*- coding:utf-8 -*- 
import pygame
import math



SIZE = (540, 540)
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Пять полей')
screen = pygame.Surface(SIZE)




num_down = 0
global go_move
go_move = 0

pix = 60

# временные для хранения координат шашек
x = 0
y = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0

class Platform:
    def __init__(self):
        self.fon = pygame.image.load('img/fon60.png')
        self.red = pygame.image.load('img/red60.png')
        self.blue = pygame.image.load('img/blue60.png')
        self.green = pygame.image.load('img/green60.png')

def make_level(level, platform):
    x = 0
    y = 0
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                screen.blit(platform.fon, (x,y))
            if level[i][j] == 2:
                screen.blit(platform.blue, (x,y))   
            if level[i][j] == 3:
                screen.blit(platform.red, (x,y))    
            if level[i][j] == 4:
                screen.blit(platform.green, (x,y))  
            x += 60
        y += 60
        x = 0



#функция для проверки возможности хода, параметры - координаты, будет возвращать 1 - значит все ок, ход возможен, 0 - значит ход невозможен    
def true_run(level, xx1, yy1, xx2, yy2):
    #если игрок ходит не на пустую клетку, то сразу ход невозможен
    if level[xx2][yy2] != 1:
        return 0
    else:
    #игрок сходил на пустую клетку, проверяем разные комбинации возможных ходов, либо вверх илли перепрыгнуть
        if math.fabs(xx2-xx1) == 1 and yy2 == yy1:
                return 1
        elif  math.fabs(xx2-xx1) == 2 and yy2 == yy1:
            if 2 <= level[(xx1+xx2)//2][yy2] <= 3:
                return 1
            else:
                return 0
        elif math.fabs(yy2-yy1) == 1 and xx2 == xx1:
            return 1
        elif math.fabs(yy2-yy1) == 2 and xx2 == xx1:
            if 2 <= level[(yy1+yy2//2)][xx2] <= 3:
                return 1
            else: 
                return 0
        else:
            return 0

def move():
    go_move = 0
    #здесь будем все прописывать, все дейстивия
    global num_down,x1,y1,x2,y2
    if num_down == 0:
            #значит произошло первое нажатие 
            #теперь проверяем произошло левой или правой кнопкой мыши, должно левой
        if e.button != 1:
            print('Вы играете другими')#игрок нажал правую кнопку, следовательно мы можем вывести сообщение о невозможности хода либо вообще никак 
        else:
            #игрок нажал левую кнопку, следровательно все ок
            (mouseA, mouseB) = pygame.mouse.get_pos()
            a = int(mouseA/pix)
            b = int(mouseB/pix)
                #проверяем игрок нажал на шашку или нет , было почему level[b][a] не понимаю почему сам так поставил??
            if level[b][a] == 3:
                x1 = b
                y1 = a
                #если да, то все верно, как положено, мы должны изменить значения массива левела и пометить это как то на игровом поле
                #к примеру так 
                level[b][a] = 4
                #и перерисовать игровое поле
                pygame.display.update()
                #увеличиваем наш счетчик ходов игрока
                num_down+=1

    else:
        if e.button == 1:
            #игрок нажал левую кнопку -> значит он будет еще ходить
            (mouseA, mouseB) = pygame.mouse.get_pos()
            a = int(mouseA/pix)
            b = int(mouseB/pix)
            # if (x1-a) == 2 and b == y1:
                # if level[a][b] == 1:
                    # if 
                #здесь проверяем на возможность хода
                #во первых должен игрок щелкнуть на пустую клетку
                #во вторых клетка нажатая второй раз должна отличаться от клетки нажатой в первый раз на 1 или 2 либо по горизонтали либо по вертикали
                #чв третьих если отличается на 2, то между "первой" и "второй" клеткой должна находиться любая шашка
                #я тебе потом это допишу

                # проверяем нажатие второе, перепрыгиваем через 1 шашку, если 
            if num_down == 1:
                x = x1
                y = y1
                x2 = b
                y2 = a
            else:
                x = x2
                y = y2
                x2 = b
                y2 = a
            if true_run(level, x, y, x2, y2):
                level[x][y] = 1
                level[x2][y2] = 4
                pygame.display.update()
                num_down+=1
            else:
                print('Неверный ход')
                # (mouseA, mouseB) = pygame.mouse.get_pos()
                
                # a = int(mouseA/pix)
                # b = int(mouseB/pix)
                # make_level(level, pl)
                #здесь можешь вывсети сообщение о невозможности хода
                if num_down > 0:
                    level[x][y] = 3
                    level[x2][y2] = 1
                    pygame.display.update()
                    num_down = 0
                    
                    #ход невозможен
                    #здесь надо подумать как ты хочешь обрабатывать недопустимый ход
                    #есть несколько вариантов
                    #первый, как у меня был, мы все возвращаем в исходную позицию и выводим сообщение о недопустимости хода
                    #второй вариант, мы никак не реагируем на этот ход, а просто ждем когда игрок сходит правильно
        else:
            (mouseA, mouseB) = pygame.mouse.get_pos()
            a = int(mouseA/pix)
            b = int(mouseB/pix)
                #здесь тоже проверяем на возможность хода, впринципе такие же действия что и чуть выше
                #
                #
                #тож тебе потом допишу
            if num_down == 1:
                x = x1
                y = y1
                x2 = b
                y2 = a
            else:
                x = x2
                y = y2
                x2 = b
                y2 = a
            if true_run(level, x, y, x2, y2):
                level[x][y] = 1
                level[x2][y2] = 3
                pygame.display.update()
                num_down = 0   
                go_move = 1
    if go_move == 1:
        moveAI()
        
        
        
        
        
        
def moveAI():
    MaxMoveAI = -100    #балл лучшего хода всех шашек
    MaxMove = 0         #балл лучшего хода одной шашки
    MaxJ1 = 0   #координата клетки начала хода
    MaxI = 0     #координата клетки начала хода
    MaxJ2 = 0   #координата клетки конца хода
    TempI = 0   #переменная для временного хранения координаты
    TempJ = 0   #переменная для временного хранения координаты
    #проходим по игровому полю и ищем шашки
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 2:   #нашли нужную шашку
                if j == 0:
                    MaxMove = 0   #шашка находится в нужном месте             
                elif j == 1:   #шашка находится почти в нужном месте
                    if level[i][j-1] == 1:   #возможен ли ее ход вперед?
                        MaxMove = 2 + j   #если да, то делаем оценку данного хода
                        if MaxMoveAI < MaxMove:   #если этот ход более выгоден, чем остальные ходы других шашек
                    #если да, то в переменные координат хода записывает координаты этого хода
                            MaxMoveAI=MaxMove   
                            MaxI = i
                            MaxJ1 = j
                            MaxJ2 = j-1
                            MaxMove = 0
                else:
                    if level[i][j-1] > 1 and level[i][j-2] == 1:   #возможно ли данной шашке сделать "прыжок"
                        TempI = i
                        TempJ = j
                        MaxMove = MaxMove + 10 + j   #делаем оценку данного хода
                        j = j - 2
                        print("11111",j)
                        if j>1:
                            while (level[i][j-1] > 1 and level[i][j-2] == 1):   #проверяем возможности дальнейших прыжков
                                j = j-2
                                print("2222",j)
                                MaxMove = MaxMove + 10;
                                if j<2:
                                    break
                        if MaxMoveAI < MaxMove:   #если этот ход более выгоден, чем остальные ходы других шашек
                        #если да, то в переменные координат хода записывает координаты этого хода
                            MaxJ2 = j
                            MaxJ1 = TempJ
                            MaxI = TempI
                            MaxMoveAI = MaxMove
                            MaxMove = 0
                        else:
                            MaxMove = 0
                    elif level[i][j-1] == 1:   #возможно ли данной шашке сходить на одну клетку вперед
                        MaxMove = 2 + j
                        if MaxMoveAI < MaxMove:   #если этот ход более выгоден, чем остальные ходы других шашек
                        #если да, то в переменные координат хода записывает координаты этого хода
                            MaxJ2 = j - 1
                            MaxJ1 = j
                            MaxMoveAI = MaxMove
                            MaxMove = 0
                        else:
                            MaxMove = 0
                MaxMove = 0 
    #меняем игровой массив и делае перерисовку игрового поля            
    level[MaxI][MaxJ1] = 1
    level[MaxI][MaxJ2] = 2
    pygame.display.update()


                    
                    

level = [
    [0,0,0,1,1,1,0,0,0],
    [0,0,0,1,1,1,0,0,0],
    [0,0,0,1,1,1,0,0,0],
    [1,1,1,1,1,1,2,2,2],
    [1,1,1,1,1,1,2,2,2],
    [1,1,1,1,1,1,2,2,2],
    [0,0,0,3,3,3,0,0,0],
    [0,0,0,3,3,3,0,0,0],
    [0,0,0,3,3,3,0,0,0]]

rule = True

pl = Platform()


done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            move()    
        
    screen.fill((240,255,255))
    
    make_level(level, pl)

    window.blit(screen, (0,0))
    pygame.display.flip()