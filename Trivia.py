import pygame,sys,random

width,height = 1280,850
pygame.mixer.init()
loss_sound = pygame.mixer.Sound("loss.wav")
loss_sound.set_volume(0.2)
select_sound = pygame.mixer.Sound("select.wav")
select_sound.set_volume(0.2)
win_sound = pygame.mixer.Sound("mask.wav")
win_sound.set_volume(0.2)

A1 = pygame.image.load(".\\image\\A1.png")
A2 = pygame.image.load(".\\image\\A2.png")
B1 = pygame.image.load(".\\image\\B1.png")
B2 = pygame.image.load(".\\image\\B2.png")
C1 = pygame.image.load(".\\image\\C1.png")
C2 = pygame.image.load(".\\image\\C2.png")
D1 = pygame.image.load(".\\image\\D1.png")
D2 = pygame.image.load(".\\image\\D2.png")
temp = [[0,0],[0,0],[0,0],[0,0]]

def print_text(screen,font,x,y,text,color=(255,255,255),an = -1):
     #制作阴影
    imgText = font.render(text,True,(0,0,0))
    screen.blit(imgText,(int(x-2),int(y-2)))

    imgText=font.render(text,True,color)
    screen.blit(imgText,(int(x),int(y)))
    if an != -1:
        if an == 1:
            screen.blit(A1,(int(x - 100),int(y + 10)))
        elif an == 2:
            screen.blit(B1,(int(x - 100),int(y + 10)))
        elif an == 3:
            screen.blit(C1,(int(x - 100),int(y + 10)))
        elif an == 4:
            screen.blit(D1,(int(x - 100),int(y + 10)))
    if temp[3] == [0,0]:
        if an == 1:
            temp[0] = [int(x - 100),int(y + 10)]
        elif an == 2:
            temp[1] = [int(x - 100),int(y + 10)]
        elif an == 3:
            temp[2] = [int(x - 100),int(y + 10)]
        elif an == 4:
            temp[3] = [int(x - 100),int(y + 10)]

class Trivia(object): #继承了object这个类
    pygame.font.init()
    font2 = pygame.font.Font("c:/Windows/Fonts/msyh.ttc",40)

    def __init__(self,screen,filename):
        self.screen = screen
        self.data = []  #用于存放数据
        self.current = 0 #指针
        self.total = 0  #记录题数
        self.correct = 0 #记录正确选项
        self.score = 0

        self.white = 255,255,255
        self.red = 255,0,0
        self.green = 0,255,0
        self.orange = 255, 165, 0
        self.yellow = 255,255,0
        self.colors=[self.white,self.white,self.white,self.white]  #颜色列表

        self.current = random.randint(1, 354)  #随机得到一个问题
        self.current -= self.current % 6

        #read trivia data from filename
        f = open(filename, "r",encoding="utf-8")
        trivia_data = f.readlines() #读取f的所有行并返回列表
        f.close()

        #count and clean up trivia data
        for text_line in trivia_data:
            self.data.append(text_line.strip())
            self.total += 1

    def show_question(self):
        self.correct = int(self.data[self.current + 5])
        fontsize = int(1000/len(self.data[self.current]))
        if fontsize > 50:
            fontsize = 50
        elif fontsize < 30:
            fontsize = 30

        if len(self.data[self.current]) > 35:
            str1 = self.data[self.current][0:35]
            if len(self.data[self.current]) <= 70:
                str2 = self.data[self.current][35:]
                print_text(self.screen,pygame.font.Font("c:/Windows/Fonts/msyh.ttc",fontsize),width/6,height/20*6,str1,self.yellow)
                print_text(self.screen,pygame.font.Font("c:/Windows/Fonts/msyh.ttc",fontsize),width/6,height/20*7,str2,self.yellow)
        else:
            print_text(self.screen,pygame.font.Font("c:/Windows/Fonts/msyh.ttc",fontsize),width/6,height/20*6,self.data[self.current],self.yellow)

        #下面的代码是输出选项
        maxlen = 0
        for i in range(4):
            if len(self.data[self.current + i + 1]) > maxlen:
                maxlen = len(self.data[self.current + i + 1])

        print_text(self.screen,self.font2,width/20 * 9 - maxlen*20,height/20*9,self.data[self.current+1],self.colors[0],1)
        print_text(self.screen,self.font2,width/20 * 9 - maxlen*20,height/20*11,self.data[self.current+2],self.colors[1],2)
        print_text(self.screen,self.font2,width/20 * 9 - maxlen*20,height/20*13,self.data[self.current+3],self.colors[2],3)
        print_text(self.screen,self.font2,width/20 * 9 - maxlen*20,height/20*15,self.data[self.current+4],self.colors[3],4)

    def handle_input(self,number):
        if not self.score:
            if number == self.correct:
                self.colors[self.correct - 1] = self.green
                self.score += 1
                win_sound.play(0)
            else:
                self.colors[number - 1] = self.red
                self.colors[self.correct - 1] = self.green  #显示正确答案
                self.score -= 1
                loss_sound.play(0)
            pygame.display.update()

    def next_question(self):
        if self.score: #初始化
            self.score = 0
            self.correct = 0
            self.colors = [self.white,self.white,self.white,self.white]
            self.current = random.randint(1,354) #换个问题
            self.current -= self.current % 6
            temp[3] = [0,0]

    def Good(self):
        print_text(self.screen,self.font2,width / 20 * 7,height / 20 * 17,"回答正确！",self.orange)
        print_text(self.screen,self.font2,width / 20 * 7,height / 20 * 18,"按回车键继续挑战吧！",self.orange)
    def Loss(self):
        print_text(self.screen,self.font2, width / 20 * 7, height / 20 * 17, "回答错误！", self.orange)
        print_text(self.screen,self.font2, width / 20 * 7, height / 20 * 18, "按回车回到开始页面！", self.orange)


def Answer(screen,bg,trivia):
    trivia.next_question()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if trivia.score == 1:
                        return 1
                    elif trivia.score == -1:
                        return 0
            elif event.type == pygame.QUIT:
                sys.exit()

        screen.blit(bg, (0, 0))
        trivia.show_question()  # display trivia_data
        mouse_press = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if temp[0][0] < mouse_pos[0] < temp[0][0] + 78 and temp[0][1] < mouse_pos[1] < temp[0][1] + 40:  # [0]表示左右(x轴）
            screen.blit(A2,temp[0])
            if mouse_press[0]:  # 当鼠标点击了右键
                trivia.handle_input(1)
        elif temp[1][0] < mouse_pos[0] < temp[1][0] + 78 and temp[1][1] < mouse_pos[1] < temp[1][1] + 40:  # [0]表示左右(x轴）
            screen.blit(B2,temp[1])
            if mouse_press[0]:  # 当鼠标点击了右键
                trivia.handle_input(2)

        elif temp[2][0] < mouse_pos[0] < temp[2][0] + 78 and temp[2][1] < mouse_pos[1] < temp[2][1] + 40:  # [0]表示左右(x轴）
            screen.blit(C2,temp[2])
            if mouse_press[0]:  # 当鼠标点击了右键
                trivia.handle_input(3)
        elif temp[3][0] < mouse_pos[0] < temp[3][0] + 78 and temp[3][1] < mouse_pos[1] < temp[3][1] + 40:  # [0]表示左右(x轴）
            screen.blit(D2,temp[3])
            if mouse_press[0]:  # 当鼠标点击了右键
                trivia.handle_input(4)

        if trivia.score == 1:
            trivia.Good()
        elif trivia.score == -1:
            trivia.Loss()

        pygame.display.update()