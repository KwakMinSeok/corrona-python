import pygame,random
from person_status import Person

def main():
    pygame.init()
    WIDTH=HEIGHT=600
    screen=pygame.display.set_mode([WIDTH,HEIGHT])
    pygame.display.set_caption("Virus simulation")
    screen.fill(pygame.Color('gray'))
    clock= pygame.time.Clock()
    MAX_FPS=10
    
    running = True

    spawnbuffer=10
    # 두개만 조절하면 됨
    #사람수
    numpeople =200
    #자가격리 퍼센트
    social_distancing_percentage = 0.75
    patientZero= Person(random.randint(spawnbuffer,WIDTH-spawnbuffer),random.randint(spawnbuffer,HEIGHT-spawnbuffer),"sick",False)
    people =[patientZero]
    socialDistancing=False
    for i in range(numpeople -1):
        
        if i < social_distancing_percentage*numpeople:
            socialDistancing=True
        colliding = True
        while colliding:
            person = Person(random.randint(spawnbuffer,WIDTH-spawnbuffer),random.randint(spawnbuffer,HEIGHT-spawnbuffer),"healthy",False)
            colliding = False
            for person2 in people:
                if person.checkCollisionwithotherball(person2):
                    colliding =True
                    break
        people.append(person)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        for person in people:
            person.update(screen,people)
        screen.fill(pygame.Color("gray")) 
        for person in people:
            person.draw(screen)    
        
        
        
        
        pygame.display.flip()
       
        clock.tick(MAX_FPS) 
        
    pygame.quit()    
main()