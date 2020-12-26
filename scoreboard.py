import pygame.font

class Scoreboard():
    """显示得分信息的类"""
    # high_score = 0
    pygame.font.init()
    def __init__(self,screen,score):
        self.screen = screen
        self.score = score
        self.level = 1

        #显示得分信息时使用的字体设置
        self.text_color = (250,250,250)
        self.font = pygame.font.Font("c:/Windows/Fonts/msyh.ttc", 40)
        self.prep_score()
        self.get_high_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """"将得分转换为一幅渲染的图像"""
        score_str = "{:,}".format(self.score)
        self.score_image =self.font.render(score_str,True,self.text_color)

        #将得分放到屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = 1260
        self.score_rect.top = 20

    def prep_high_score(self):
        """将最高得分转换为渲染得图像"""
        high_score_str = "{:,}".format(self.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = 640
        self.high_score_rect.top = 20
    def prep_level(self):
        self.level_image = self.font.render(str(self.level), True, self.text_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = 1260
        self.level_rect.top = self.score_rect.bottom + 10

    def get_high_score(self):
        source = open("temp/high_score.txt","rt")
        self.high_score = int(source.read(-1))
        source.close()

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)

    def check_high_score(self):
        """检查是否产生新得最高分"""

        if self.score > self.high_score:
            source = open("temp/high_score.txt", "wt")
            source.write(str(self.score))
            source.close()
            self.high_score = self.score
            self.prep_high_score()
