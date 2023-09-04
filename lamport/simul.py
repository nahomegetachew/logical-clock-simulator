from __future__ import division
import pygame
from lamport import *
from pygame.locals import *
from sys import exit


no_of_p = eval(input("Enter a number of porssesses you want: "))
pygame.init()
screen = pygame.display.set_mode((1200, 580), 0, 32)
font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
logical_time = 0
clock = pygame.time.Clock()
lines = []
points = []
l = lamports(logical_time,no_of_p,0)
processes_ = l.prossess_
gap=int(round(390 / no_of_p))
gap_x = int(round(1000/no_of_p))
out = 50 #a gap betwen events in pixel
selected_p = 0
to_p = 0
pressed=(1,1)
pressed_p=(1,1)
x=0
y=0

    
def draw_lines():
    def animate(line):
        global x,y
        speed = 5
        time_passed = clock.tick(30)
        time_passed_seconds = time_passed / 1000.0
        distance_moved = time_passed_seconds * speed
        x += distance_moved
        y += distance_moved
        pygame.draw.aaline(screen, (0, 0, 0), (i[0], i[1]), (x , x))
        print(x,"ad")
    for i in range(len(processes_)):
        pygame.draw.line(screen, (0, 0, 0), (40, i*gap + 40 ),(1150,i*gap + 40))
        screen.blit( font.render("P" + str(i) , True, (0, 0, 0)), (10, i*gap + 30 ) )
    for i in lines:
            pygame.draw.line(screen, (0, 0, 0), (i[0], i[1] ),(i[2],i[3]))


def draw_points():
        for i in points:
                pygame.draw.circle(screen, (0,0,0), (i[0],i[1]), 3)
                screen.blit( font.render( str(i[2]), True, (0, 0, 0)), (i[0] ,i[1]) )




# def draw_them_lines():
def event_prosses(sender_pid,riciver_pid):
        global l
        if sender_pid == riciver_pid:
                l.event(sender_pid)
                points.append((out * l.prossess_[sender_pid].get_clock() + 40,gap * sender_pid + 40,l.prossess_[sender_pid].get_clock()))
        else:

                l.send(sender_pid,riciver_pid)
                points.append((out * l.prossess_[sender_pid].get_clock() + 40,gap * sender_pid + 40,l.prossess_[sender_pid].get_clock()))
                points.append((out * l.prossess_[riciver_pid].get_clock() + 40,gap * riciver_pid + 40,l.prossess_[riciver_pid].get_clock()))
                lines.append((out * l.prossess_[sender_pid].get_clock() + 40 ,gap * sender_pid + 40,out * l.prossess_[riciver_pid].get_clock() + 40,gap * riciver_pid + 40,0))
                print((out * l.prossess_[sender_pid].get_clock() + 40,gap * sender_pid + 40,l.prossess_[sender_pid].get_clock()) in points)

                
        

        
def draw_controlers(): 
    global pressed,gap_x,selected_p
    pcy=550 #primary controler y axis
    scy=450
     
    for i in range(len(processes_)):
        pygame.draw.circle(screen, (0,0,255), (i * gap_x + 100, pcy), 30, 1)
        screen.blit( font.render("P" + str(i), True, (0, 0, 0)), (i*gap_x + 90,pcy - 10) )
        if pressed[0] > i * gap_x + 80 and  pressed[0] < i * gap_x + 120:
                if pressed[1] > pcy - 20 and pressed[1] < pcy + 20:
                        pygame.draw.line(screen, (0, 0, 0), (100, scy  + 22),((no_of_p - 1) * gap_x + 100,scy + 22),4)
                        selected_p = i
                        for j in range(len(processes_)):
                                pygame.draw.circle(screen, (255,0,0), (j * gap_x + 100, scy), 20, 2)
                                screen.blit( font.render("P" + str(j), True, (0, 0, 0)), (j*gap_x + 90,scy - 10 ) )
                                pygame.draw.line(screen, (0, 0, 0), (j * gap_x + 100, scy + 22),(j * gap_x + 100, scy + 30),4)
                                pygame.draw.line(screen, (0, 0, 0), (i * gap_x + 100, scy + 22),(i * gap_x + 100, scy + 70),4)
                                k = j

        if pressed[0] > i * gap_x + 80 and  pressed[0] < i * gap_x + 120:
                if pressed[1] > scy - 20 and pressed[1] < scy + 20:  
                        pressed=(0,0) 
                        event_prosses(selected_p,i)
        
                        
                

def click_controlers(evnt):
        a=8



while True:
        
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()   
        if event.type == MOUSEBUTTONUP:
                pressed = event.pos


    screen.fill((255, 255, 255))
 
    draw_lines()
    draw_controlers()
    draw_points()

    pygame.display.update()
    