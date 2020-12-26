from Object import *
from scoreboard import Scoreboard
from Trivia import *

def init():
    pygame.init()

    pygame.display.set_caption("新型冠状病毒")
    bg_sound = pygame.mixer.Sound("bg.wav")
    bg_sound.set_volume(0.05)
    bg_sound.play(-1)
    icon = pygame.image.load(".\\image\\icon.jpg")
    pygame.display.set_icon(icon)

def main():
    sb.level = 1
    sb.score = 0
    sb.prep_level()
    sb.prep_score()
    sb.get_high_score()

    b = Bird()
    i = 0
    j = 0
    up_state = False
    group = pygame.sprite.Group()
    state = True
    while state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                up_state = True
                j = 0
                b.image = b.img3

        b.move_down()
        screen.blit(bg, (0,0))
        sb.show_score()
        screen.blit(b.image,b.rect)
        M.move()
        screen.blit(M.image,M.rect)

        i += 1
        j += 1
        if up_state:
            if j > 20:
                up_state = False
            else:
                b.move_up()
        elif j%11 == 0:
            b.image = b.img2
        elif j%21 == 0:
            b.image = b.img1

        if i % (130 - sb.level) == 0:
            pig = Virus_Blue()
            group.add(pig)
        if i % (200 - sb.level*2) == 0:
            pig = Virus_Green()
            group.add(pig)
        if i % (260 - sb.level*3)== 0:
            pig = Virus_Red()
            group.add(pig)
            sb.prep_score()

        for p in group.sprites():
            p.move()
            screen.blit(p.image,p.rect)
            if pygame.sprite.collide_mask(b,p) and i > 200:
                loss_sound.play(0)
                sb.score -= 200
                if Answer(screen,bg,trivia):
                    i = 0
                    break
                else:
                    sb.check_high_score()
                    state = False

        for p in group.sprites().copy():
            if p.rect.left <= -120:
                group.remove(p)
                sb.score += 100
                if sb.score%13==0:
                    sb.level += 1
                    sb.prep_level()

        if pygame.sprite.collide_mask(b,M):
            win_sound.play(0)
            sb.level -= 2
            sb.prep_level()
            sb.score += 1000
            b.rect.center = [150, 425]
            for p in group.sprites().copy():
                group.remove(p)

        pygame.display.update()
        fclock.tick(60)


def Start():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(bg, (0, 0))
        img_re = pygame.image.load(".\\image\\key1.png")
        img_srcpos = img_re.get_rect()

        mouse_press = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        left = img_srcpos.left + 550
        right = img_srcpos.right + 550
        top = img_srcpos.top + 600
        bottom = img_srcpos.bottom + 600

        if left<mouse_pos[0]<right and top<mouse_pos[1]<bottom: #[0]表示左右(x轴）
            img_re = pygame.image.load(".\\image\\key2.png")
            if mouse_press[0]: #当鼠标点击了右键
                select_sound.play(0)
                main()

        screen.blit(img_re,(550,600))
        pygame.display.update()


fclock = pygame.time.Clock()
size = width, height = 1280, 850
screen = pygame.display.set_mode(size)
trivia = Trivia(screen, "temp//problems.txt")  # load the trivia data file
bg = pygame.image.load(".\\image\\bg.jpg")
sb = Scoreboard(screen, 0)
M = Mask(screen)
init()


while 1:
    Start()
