# import pygame
# import random
# pygame.init()
# screen=pygame.display.set_mode((600, 600))
# pygame.display.set_caption("Name of window")
# def show_text(msg, x, y, color, size):
#         fontobj= pygame.font.SysFont("freesans", size)
#         msgobj = fontobj.render(msg,False,color)
#         screen.blit(msgobj,(x, y))

# class circle():
#     radius=25
#     def __init__(self):
#         self.x=random.randint(0, 600)
#         self.y=random.randint(0, 600)
#         self.drag=False
#         self.color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     def draw_circle(self):
#         pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
#     def object_clicked(self, pos):
#         if pos[0] >= self.x-circle.radius and pos[0] <= self.x+circle.radius and pos[1] >= self.y-circle.radius and pos[1] <= self.y+circle.radius:
#             self.drag=True

# circles=[]
# for a in range(0, 5):
#     b=circle()   
#     circles.append(b)      
# while True:
#     screen.fill((0,0,0))
#     for c in circles:
#         c.draw_circle()
#     for event in pygame.event.get():
#         if event.type==pygame.MOUSEBUTTONDOWN:
#             for d in circles:
#                 d.object_clicked(event.pos)
#         if event.type==pygame.MOUSEMOTION:
#             for d in circles:
#                 if d.drag==True:
#                     d.x=event.pos[0]
#                     d.y=event.pos[1]
#         if event.type==pygame.MOUSEBUTTONUP:
#             for d in circles:
#                 d.drag=False
#         if event.type==pygame.QUIT:
#             print("bye")
#             pygame.quit()
#             exit()
#     pygame.display.update()

import pygame
import random
pygame.init()
screen=pygame.display.set_mode((600, 600))
pygame.display.set_caption("Name of window")
def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("freesans", size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))

class circle():
    radius=25
    def __init__(self, color):
        self.x=random.randint(0, 600)
        self.y=random.randint(0, 600)
        self.color=color
        self.speed=2
    def draw_circle(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    def move_circle(self):
        if self.color==(255, 0, 0):
            self.x=self.x+self.speed
            if self.x>=600:
                self.speed=self.speed*-1
            if self.x<=0:
                self.speedx=self.speed*-1
        if self.color==(0, 255, 0):
            self.y=self.y+self.speed
            if self.y>=600:
                self.speed=self.speed*-1
            if self.y<=0:
                self.speedx=self.speed*-1



circles=[]
for a in range(0, 10):
    color=(255, 0, 0)
    b=circle(color)
    circles.append(b)
for c in range(0, 10):
    color=(0, 255, 0)
    d=circle(color)
    circles.append(d)
while True:
    screen.fill((0,0,0))
    for z in circles:
        z.draw_circle()
        z.move_circle()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print("bye")
            pygame.quit()
            exit()
    pygame.display.update()

