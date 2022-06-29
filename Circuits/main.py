import pygame
from pygame.locals import *
from object import Object
from switch import Switch
from lamp import Lamp
from menu import Menu
from menu_voice import Menu_voice
from new_object import New_object
from wire import Wire

size = width, height = 620, 540


black = 0,0,0
white = 255,255,255
blue = 0,0,255

screen = pygame.display.set_mode(size) # RESIZABLE

clock = pygame.time.Clock()

obj_list = []
wire_list = []
#x = Object(1,2,20,50)
#obj_list.append(x)

#drawing = False

create_menu = Menu()
create_menu.add_voice(New_object("Nuovo switch", "switch"))
create_menu.add_voice(New_object("Nuova lampada", "lamp"))

dragging = False
moved = False
wiring = False
dragging_index = 0

while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                # left click

                if create_menu.is_displayed():
                    mouse_x, mouse_y = event.pos
                    x = create_menu.on_leftclick(mouse_x, mouse_y)
                    
                    if x != None:
                        
                        obj_list.append(x)

                    create_menu.hide()

                else: 
                    mouse_x, mouse_y = event.pos
                    i = 0
                    for ob in obj_list:
                        if ob.is_inside(mouse_x, mouse_y):
                            dragging = True
                            dragging_index = i
                            starting_x = mouse_x
                            starting_y = mouse_y
                            moved = False
                        i = i + 1

            elif event.button == 2:
                # middle click
                # # # # mouse_x, mouse_y = event.pos
                # # # # ob_todel = None
                # # # # for ob in obj_list:
                # # # #     if ob.is_inside(mouse_x, mouse_y):
                # # # #         ob_todel = ob

                # # # # if ob_todel != None:
                # # # #     obj_list.remove(ob_todel)
                if wiring:
                    wiring = False
                    mouse_x, mouse_y = event.pos
                    dest_ob = None
                    for ob in obj_list:
                        if ob.is_inside(mouse_x, mouse_y):
                            dest_ob = ob

                    if dest_ob != None:
                        x = Wire(starting_ob, dest_ob)
                        wire_list.append(x)
                        # va creato il cavo qui
                        pass
                else:
                    mouse_x, mouse_y = event.pos
                    starting_ob = None
                    for ob in obj_list:
                        if ob.is_inside(mouse_x, mouse_y):
                            starting_ob = ob

                    if starting_ob != None:
                        wiring = True

               
            elif event.button == 3:
                # right click
                #drawing = True
                ### mouse_x, mouse_y = event.pos
                #starting_x = mouse_x
                #starting_y = mouse_y
                #drawing_w = 1
                #drawing_h = 1
                ### x = Switch(mouse_x, mouse_y)
                ### obj_list.append(x)

                mouse_x, mouse_y = event.pos
                
                create_menu.set_position(mouse_x, mouse_y)
                create_menu.display()
                
            # 5 -> scroll up
            # 6 -> scroll down
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if dragging:
                    dragging = False
                    
                    if not moved:
                        obj_list[dragging_index].on_leftclick()
                    
            elif event.button == 3:
                pass
                #drawing = False
                #if drawing_w < 0:
                #    starting_x = starting_x + drawing_w
                #    drawing_w = -drawing_w

                #if drawing_h < 0:
                #    starting_y = starting_y + drawing_h
                #    drawing_h = -drawing_h

                #x = Object(starting_x, starting_y, drawing_w, drawing_h)
                #obj_list.append(x)
            
        elif event.type == pygame.MOUSEMOTION:
            #if drawing:
            #    mouse_x, mouse_y = event.pos
            #    drawing_w = mouse_x - starting_x
            #    drawing_h = mouse_y - starting_y 
            if dragging:
                moved = True

                mouse_x, mouse_y = event.pos
                vec_x = mouse_x - starting_x
                vec_y = mouse_y - starting_y
                
                obj_list[dragging_index].translate(vec_x, vec_y)
                starting_x = mouse_x
                starting_y = mouse_y
        


    for ob in obj_list:
        ob.deactivate_if_passive()

    for w in wire_list:
        w.update()

    for ob in obj_list:
        #pygame.draw.rect(screen, white, ob.get_rect(), ob.get_border_width())
        ob.render(screen)

    for w in wire_list:
        w.render(screen)

    if wiring:
        # devo devo disegnare una linea dall'oggetto da cui sta partento il wiring, al mouse
        pygame.draw.line(screen, white, starting_ob.get_position(), pygame.mouse.get_pos())
        

    create_menu.render(screen)

    #if drawing:
    #    pygame.draw.rect(screen, blue, pygame.Rect(starting_x, starting_y, drawing_w, drawing_h), 2)

    pygame.display.update()
    
    clock.tick(60)
