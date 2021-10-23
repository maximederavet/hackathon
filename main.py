from decryptor import decrypt
from generator import generate_file
from parking import parking
import pygame
import random
from gui import Button, Window

#initialisaiton de pygame et definition de variables nécessaires
pygame.init()
RED_trns   = (255,  0,  0, 100)    # red
GREEN_trns = (0  ,255, 0 , 100) #green
ORANGE_trns  = (255  ,128 , 0, 128) #blue

generate_file(1, 2,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)

win = Window()

running = True
#display the first datas
parking_list = decrypt("parking_gen.csv")

print(parking_list[0][0][0].name)




while (running):
    win.window.blit(win.background, (0,0))
    win.window.blit(win.iphone, (0, 0))
    #displaying initial data
    days_count = 0
    for parking in parking_list:
        
        
        for days in parking:
            days_count = 0
            for hours in days:
                days_count += 1
                print(days_count)
                if hours.maxcap/hours.Ocupation > 0.66:
                    #print(hours.maxcap/hours.Ocupation)
                    
                    #win.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, RED_trns)
                    pass
                elif hours.maxcap/hours.Ocupation < 0.66 and hours.maxcap/hours.Ocupation > 0.33:
                    #print(hours.maxcap/hours.Ocupation)
                    #print(days_count)
                    pass
                    #win.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, GREEN_trns)
                else:
                    pass
                    #print(days_count)
                    #print(hours.maxcap/hours.Ocupation)
                    win.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, ORANGE_trns)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            win.check_button_click(pos)
    

    win.draw_button()
    pygame.display.flip()
