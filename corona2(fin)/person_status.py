import random
import math
import pygame

minMovement=0.5
max_speed=5

class Person():
    #status는 health,sick,recovered
    colors={"healthy":"white","sick":"red","recovered":"blue"}
    def __init__(self,x,y,status,socialDistancing):
        self.x=x
        self.y=y
        self.status=status
        self.socialDistancing=socialDistancing
        self.radius=6
        self.vx=self.vy=0
        self.turnSick=0
        self.recoverytime=random.randint(100,200)
        if not self.socialDistancing:
           while -minMovement<self.vx<minMovement and -minMovement<self.vy<minMovement:
                self.vx=random.uniform(-max_speed,max_speed)
                self.vy=random.uniform(-max_speed,max_speed)
    def draw(self,screen):
        pygame.draw.circle(screen,pygame.Color(self.colors[self.status]),(round(self.x),round(self.y)),self.radius,5)

    #status 상태 변형
    def update(self,screen,people):
        self.people=people
        self.move()
        if self.status =="sick":
            self.turnSick+=1
            #turnSick=감염자수
            if self.turnSick ==self.recoverytime:
                #recoverytime이후에는 회복 기간 이후이므로 status->recovered
                self.status="recovered"
        self.checkCollisionwithwall(screen)
        for other in people:
            if self != other:
                if self.checkCollisionwithotherball(other):
                    self.updateCollisionVelocities(other)
                    if self.status == "sick" and other.status == "healthy":
                        other.status = "sick"
                    elif other.status =="sick" and self.status =="healthy":
                        self.status ="sick"

    def move(self):
        if not self.socialDistancing:
            self.x +=self.vx
            self.y +=self.vy
    def checkCollisionwithwall(self,screen):
        if self.x+self.radius>=screen.get_width() and self.vx>0:
            self.vx*=-1
        elif self.x-self.radius<=0 and self.vx<0:
            self.vx*= -1
        if self.y+self.radius>= screen.get_height() and self.vy>0:
            self.vy*=-1
        elif self.y -self.radius <=10 and self.vy <0:
            self.vy*= -1
    #공 접촉이후 튕김    
    def checkCollisionwithotherball(self,other):
        #루트 -> sqrt
        #math.pow(a,b) -> a^b
        distance = math.sqrt(math.pow(self.x-other.x,2)+math.pow(self.y-other.y,2))
        if distance <= self.radius +other.radius:
            return True
        return False
    def updateCollisionVelocities(self,other):
        #type1 collision - both collision is social distancing
        if not self.socialDistancing and not other.socialDistancing:
            tempVX=self.vx
            tempVY=self.vy
            self.vx=other.vx
            self.vy=other.vy
            other.vx =tempVX
            other.vy =tempVY
        elif other.socialDistancing:
            magV = math.sqrt(math.pow(self.vx,2)+math.pow(self.vy,2))
            tempVector =(self.vx+(self.x -other.x),self.vy +(self.y-other.y))
            magTemVector =math.sqrt(math.pow(tempVector[0],2)+ math.pow(tempVector[1],2))
            normTempvector = (tempVector[0]/magTemVector,tempVector[1]/magTemVector)
            self.vx = normTempvector[0]*magV
            self.vy = normTempvector[1]*magV

