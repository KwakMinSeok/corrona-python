import pygame

WHITE=(255,255,255) 
BLACK= (0,0,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
SHADOW = (192, 192, 192)
WHITE = (255, 255, 255)
LIGHTGREEN = (0, 255, 0 )
GREEN = (0, 200, 0 )
BLUE = (0, 0, 128)
LIGHTBLUE= (0, 0, 255)
RED= (200, 0, 0 )
LIGHTRED= (255, 100, 100)
PURPLE = (102, 0, 102)
LIGHTPURPLE= (153, 0, 153)
pygame.init()
win = pygame.display.set_mode((900,500))
pygame.display.set_caption("Barriar")

pygame.display.flip()
class Button():
    def __init__(self,color,width,height,ax,ay,bx,by):
        self.color=color
        self.width=width
        self.height=height
        self.ax=ax
        self.by=by
        self.ay=ay
        self.bx=bx
    def move(self):
       
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.ay -= 5
            if self.ay<-125:
                self.ay=-125
            self.by += 5
            if self.by>375:
                self.by=375

        if keys[pygame.K_DOWN]:
            self.ay += 5
            if self.ay>0:
                self.ay=0
            self.by -= 5
            if self.by<250:
                self.by=250
        
    def draw(self):
        win.fill(WHITE)
        pygame.draw.rect(win,BLACK,(0,0,900,500),5)
        pygame.draw.rect(win,self.color,(self.ax,self.ay,self.width,self.height),5)
        pygame.draw.rect(win,self.color,(self.bx,self.by,self.width,self.height),5)
        pygame.display.update()
            

def main_loop():
    TEST=Button(BLACK,40,250,200,0,200,250)
    run = True
    while run:
        pygame.time.delay(100)       
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                run=False
        TEST.move()
        TEST.draw()
    pygame.quit()

main_loop()