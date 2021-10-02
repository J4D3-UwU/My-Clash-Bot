from PIL import ImageGrab as ig
import pyautogui

priority1 = 1
priority2 = 1
priority3 = 1
priority4 = 1
priority5 = 1
priority6 = 1
priority7 = 1
priority8 = 1
priority9 = 1
priority10 = 1
priority11 = 1
priority12 = 1
priority13 = 1
while(True):
    screen = ig.grab()

    if pyautogui.locateCenterOnScreen("D:\\cr.ss\\place2.png", confidence=0.6) != None:

        deck_region = (774, 862, 436, 113)
        # Deck
        archer =                pyautogui.locateCenterOnScreen("D:\\cr.ss\\deck 1\\archer.png", region=deck_region, confidence=0.6)       #Archers
        goblins =               pyautogui.locateCenterOnScreen("D:\\cr.ss\\deck 1\\goblins.png", region=deck_region, confidence=0.6)      #Spear Goblins
        hut =                   pyautogui.locateCenterOnScreen("D:\\cr.ss\\deck 1\\hut.png", region=deck_region, confidence=0.6)          #Hut
        skeletons =             pyautogui.locateCenterOnScreen("D:\\cr.ss\\deck 1\\skeletons.png", region=deck_region, confidence=0.6)    #Skeleton Army
        bats =                  pyautogui.locateCenterOnScreen("D:\\cr.ss\\deck 1\\bats.png", region=deck_region, confidence=0.6)         #Bats
        valk =                  pyautogui.locateCenterOnScreen("D:\\cr.ss\\deck 1\\val.png", region=deck_region, confidence=0.6)          #Valkyrie
        ram =                   pyautogui.locateCenterOnScreen("D:\\cr.ss\\deck 1\\ram.png", region=deck_region, confidence=0.6)          #Battle Ram
        witch =                 pyautogui.locateCenterOnScreen("D:\\cr.ss\\deck 1\\witch.png", region=deck_region, confidence=0.6)        #Witch


        enemy_left_tower =      pyautogui.locateCenterOnScreen("D:\\cr.ss\\tower.png", region=(748, 209, 91, 69), confidence=0.55)
        enemy_right_tower =     pyautogui.locateCenterOnScreen("D:\\cr.ss\\tower.png", region=(1040, 209, 91, 69), confidence=0.55)
        my_left_tower =         pyautogui.locateCenterOnScreen("D:\\cr.ss\\tower.png", region=(748, 621, 91, 69), confidence=0.55)
        my_right_tower =        pyautogui.locateCenterOnScreen("D:\\cr.ss\\tower.png", region=(1040, 621, 91, 69), confidence=0.55)

        xbow =     pyautogui.locateCenterOnScreen("D:\\cr.ss\\xbow.png", region=(700, 348, 475, 234), confidence=0.62)

        # Enemy Side 4
        if pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(695, 140, 233, 154), confidence=0.7) == pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(766, 170, 47, 22), confidence=0.7): enemy_towers_left4 = None
        else: enemy_towers_left4 = pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(695, 140, 233, 154), confidence=0.7)
        if pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(928, 140, 233, 154), confidence=0.7) == pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(1063, 170, 47, 22), confidence=0.7): enemy_towers_right4 = None
        else: enemy_towers_right4 = pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(928, 140, 233, 154), confidence=0.7)
        enemy_mid_left4 =        pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(695, 294, 233, 118), confidence=0.7)
        enemy_mid_right4 =       pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(928, 294, 233, 118), confidence=0.7)
        enemy_bridge_left4 =     pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(695, 412, 233, 58), confidence=0.7)
        enemy_bridge_right4 =    pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(928, 412, 233, 58), confidence=0.7)

        # My Side 4
        my_bridge_left4 =        pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(695, 480, 233, 53), confidence=0.7)
        my_bridge_right4 =       pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(928, 480, 233, 53), confidence=0.7)
        my_mid_left4 =           pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(695, 533, 233, 57), confidence=0.7)
        my_mid_right4 =          pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(928, 533, 233, 57), confidence=0.7)
        if pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(695, 590, 233, 190), confidence=0.7) == pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(769, 644, 47, 22), confidence=0.7): my_towers_left4 = None
        else: my_towers_left4 = pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(695, 590, 233, 190), confidence=0.7)
        if pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(928, 590, 233, 190), confidence=0.7) == pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(1063, 644, 47, 22), confidence=0.7): my_towers_right4 = None
        else: my_towers_left4 = pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy4.png", region=(928, 590, 233, 190), confidence=0.7)


        # Enemy Side 5
        if pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(695, 140, 233, 154), confidence=0.7) == pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(766, 170, 47, 22), confidence=0.7): enemy_towers_left5 = None
        else: enemy_towers_left5 = pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(695, 140, 233, 154), confidence=0.7)
        if pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(928, 140, 233, 154), confidence=0.7) == pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(1063, 170, 47, 22), confidence=0.7): enemy_towers_right5 = None
        else: enemy_towers_right5 = pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(928, 140, 233, 154), confidence=0.7)
        enemy_mid_left5 =        pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(695, 294, 233, 118), confidence=0.7)
        enemy_mid_right5 =       pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(928, 294, 233, 118), confidence=0.7)
        enemy_bridge_left5 =     pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(695, 412, 233, 58), confidence=0.7)
        enemy_bridge_right5 =    pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(928, 412, 233, 58), confidence=0.7)

        # My Side 5
        my_bridge_left5 =        pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(695, 480, 233, 53), confidence=0.7)
        my_bridge_right5 =       pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(928, 480, 233, 53), confidence=0.7)
        my_mid_left5 =           pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(695, 533, 233, 57), confidence=0.7)
        my_mid_right5 =          pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(928, 533, 233, 57), confidence=0.7)
        if pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(695, 590, 233, 190), confidence=0.7) == pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(769, 644, 47, 22), confidence=0.7): my_towers_left5 = None
        else: my_towers_left5 = pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(695, 590, 233, 190), confidence=0.7)
        if pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(928, 590, 233, 190), confidence=0.7) == pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(1063, 644, 47, 22), confidence=0.7): my_towers_right5 = None
        else: my_towers_right5 = pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy5.png", region=(928, 590, 233, 190), confidence=0.7)


        # Enemy Side 7
        if pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(695, 140, 233, 154), confidence=0.7) == pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(766, 170, 47, 22), confidence=0.7): enemy_towers_left7 = None
        else: enemy_towers_left7 = pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(695, 140, 233, 154), confidence=0.7)
        if pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(928, 140, 233, 154), confidence=0.7) == pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(1063, 170, 47, 22), confidence=0.7): enemy_towers_right7 = None
        else: enemy_towers_right7 = pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(928, 140, 233, 154), confidence=0.7)
        enemy_mid_left7 =       pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(695, 294, 233, 118), confidence=0.7)
        enemy_mid_right7 =      pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(928, 294, 233, 118), confidence=0.7)
        enemy_bridge_left7 =    pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(695, 412, 233, 58), confidence=0.7)
        enemy_bridge_right7 =   pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(928, 412, 233, 58), confidence=0.7)


        # My Side 7
        my_bridge_left7 =       pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(695, 480, 233, 53), confidence=0.7)
        my_bridge_right7 =      pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(928, 480, 233, 53), confidence=0.7)
        my_mid_left7 =          pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(695, 533, 233, 57), confidence=0.7)
        my_mid_right7 =         pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(928, 533, 233, 57), confidence=0.7)
        if pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(695, 590, 233, 190), confidence=0.7) == pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(769, 644, 47, 22), confidence=0.7): my_towers_left7 = None
        else: my_towers_left7 = pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(695, 590, 233, 190), confidence=0.7)
        if pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(928, 590, 233, 190), confidence=0.7) == pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(1063, 644, 47, 22), confidence=0.7): my_towers_right7 = None
        else: my_towers_right7 = pyautogui.locateCenterOnScreen("D:\\cr.ss\\enemy\\enemy7.png", region=(928, 590, 233, 190), confidence=0.7)





        #Elixer
        if "(204, 32, 210)" or "(205, 33, 211)" in str(screen.getpixel((1197, 1015))): elixer = 10
        elif "(204, 32, 210)" or "(205, 33, 211)" in str(screen.getpixel((1158, 1015))): elixer = 9
        elif "(204, 32, 210)" or "(205, 33, 211)" in str(screen.getpixel((1116, 1015))): elixer = 8
        elif "(204, 32, 210)" or "(205, 33, 211)" in str(screen.getpixel((1077, 1015))): elixer = 7
        elif "(204, 32, 210)" or "(205, 33, 211)" in str(screen.getpixel((1037, 1015))): elixer = 6
        elif "(204, 32, 210)" or "(205, 33, 211)" in str(screen.getpixel((999, 1015))): elixer = 5
        elif "(204, 32, 210)" or "(205, 33, 211)" in str(screen.getpixel((960, 1015))): elixer = 4
        elif "(204, 32, 210)" or "(205, 33, 211)" in str(screen.getpixel((921, 1015))): elixer = 3
        elif "(204, 32, 210)" or "(205, 33, 211)" in str(screen.getpixel((881, 1015))): elixer = 2
        else: elixer = 1


    #if pyautogui.locateCenterOnScreen("D:\\cr.ss\\place2.png", confidence=0.6) != None:
        import time
        if my_towers_left4 != None or my_towers_left5 != None or my_towers_left7 != None:
            if priority1 == 1:
                if archer != None and elixer > 2:
                    pyautogui.click(archer)
                    time.sleep(0.05)
                    pyautogui.click(714, 765)
                    priority1 = 1
                else: priority1 = priority1 + 1
            if priority1 == 2:
                if skeletons != None and elixer > 2:
                    pyautogui.click(skeletons)
                    time.sleep(0.05)
                    pyautogui.click(791, 597)
                    priority1 = 1
                else: priority1 = priority1 + 1
            if priority1 == 3:
                if goblins != None and elixer > 1:
                    pyautogui.click(goblins)
                    time.sleep(0.05)
                    pyautogui.click(714, 765)
                    priority1 = 1
                else: priority1 = priority1 + 1
            if priority1 == 4:
                if bats != None and elixer > 1:
                    pyautogui.click(bats)
                    time.sleep(0.05)
                    pyautogui.click(791, 662)
                    priority1 = 1
                else: priority1 = priority1 + 1
            if priority1 == 5:
                if valk != None and elixer > 3:
                    pyautogui.click(valk)
                    time.sleep(0.05)
                    pyautogui.click(791, 597)
                    priority1 = 1
                else: priority1 = 1


        #Enemy near my right tower
        if my_towers_right4 != None or my_towers_right5 != None or my_towers_right7 != None:
            if priority2 == 1:
                if archer != None and elixer > 2:
                    pyautogui.click(archer)
                    time.sleep(0.05)
                    pyautogui.click(1153, 765)
                    priority2 = 1
                else: priority2 = priority2 + 1
            if priority2 == 2:
                if skeletons != None and elixer > 2:
                    pyautogui.click(skeletons)
                    time.sleep(0.05)
                    pyautogui.click(1086, 597)
                    priority2 = 1
                else: priority2 = priority2 + 1
            if priority2 == 3:
                if goblins != None and elixer > 1:
                    pyautogui.click(goblins)
                    time.sleep(0.05)
                    pyautogui.click(1153, 765)
                    priority2 = 1
                else: priority2 = priority2 + 1
            if priority2 == 4:
                if bats != None and elixer > 1:
                    pyautogui.click(bats)
                    time.sleep(0.05)
                    pyautogui.click(1086, 662)
                    priority2 = 1
                else: priority2 = priority2 + 1
            if priority2 == 5:
                if valk != None and elixer > 3:
                    pyautogui.click(valk)
                    time.sleep(0.05)
                    pyautogui.click(1086, 597)
                    priority2 = 1
                else: priority2 = 1


        #Enemy on my left
        if my_mid_left4 != None or my_mid_left5 != None or my_mid_left7 != None:
            if xbow != None:
                if skeletons != None and elixer > 2:
                    pyautogui.click(skeletons)
                    pyautogui.click(xbow)
            else:
                if priority3 == 1:
                    if valk != None and elixer > 3:
                        pyautogui.click(valk)
                        time.sleep(0.05)
                        pyautogui.click(888, 547)
                        priority3 = 1
                    else: priority3 = priority3 + 1
                if priority3 == 2:
                    if goblins != None and elixer > 1:
                        pyautogui.click(goblins)
                        time.sleep(0.05)
                        pyautogui.click(914, 581)
                        priority3 = 1
                    else: priority3 = priority3 + 1
                if priority3 == 3:
                    if skeletons != None and elixer > 2:
                        pyautogui.click(skeletons)
                        if my_mid_left4 != None:
                            pyautogui.click(my_mid_left4)
                        if my_mid_left5 != None:
                            pyautogui.click(my_mid_left5)
                        if my_mid_left7 != None:
                            pyautogui.click(my_mid_left7)
                        priority3 = 1
                    else: priority3 = priority3 + 1
                if priority3 == 4:
                    if archer != None and elixer > 2:
                        pyautogui.click(archer)
                        time.sleep(0.05)
                        pyautogui.click(914, 581)
                        priority3 = 1
                    else: priority3 = priority3 + 1
                if priority3 == 5:
                    if bats != None and elixer > 1:
                        pyautogui.click(bats)
                        if my_mid_left4 != None:
                            pyautogui.click(my_mid_left4)
                        if my_mid_left5 != None:
                            pyautogui.click(my_mid_left5)
                        if my_mid_left7 != None:
                            pyautogui.click(my_mid_left7)
                        priority3 = 1
                    else: priority3 = 1


        #Enemy on my right
        if my_mid_right4 != None or my_mid_right5 != None or my_mid_right7 != None:
            if xbow != None:
                if skeletons != None and elixer > 2:
                    pyautogui.click(skeletons)
                    pyautogui.click(xbow)
            else:
                if priority4 == 1:
                    if valk != None and elixer > 3:
                        pyautogui.click(valk)
                        time.sleep(0.05)
                        pyautogui.click(973, 547)
                        priority4 = 1
                    else: priority4 = priority4 + 1
                if priority4 == 2:
                    if goblins != None and elixer > 1:
                        pyautogui.click(goblins)
                        pyautogui.click(982, 581)
                        priority4 = 1
                    else: priority4 = priority4 + 1
                if priority4 == 3:
                    if skeletons != None and elixer > 2:
                        pyautogui.click(skeletons)
                        if my_mid_right4 != None:
                            pyautogui.click(my_mid_right4)
                        if my_mid_right5 != None:
                            pyautogui.click(my_mid_right5)
                        if my_mid_right7 != None:
                            pyautogui.click(my_mid_right7)
                if priority4 == 4:
                    if archer != None and elixer > 2:
                        pyautogui.click(archer)
                        time.sleep(0.05)
                        pyautogui.click(982, 581)
                        priority4 = 1
                    else: priority4 = priority4 + 1
                if priority4 == 5:
                    if bats != None and elixer > 1:
                        pyautogui.click(bats)
                        if my_mid_right4 != None:
                            pyautogui.click(my_mid_right4)
                        if my_mid_right5 != None:
                            pyautogui.click(my_mid_right5)
                        if my_mid_right7 != None:
                            pyautogui.click(my_mid_right7)
                        priority4 = 1
                    else: priority4 = 1


        #Enemy past bridge left
        if my_bridge_left4 != None or my_bridge_left5 != None or my_bridge_left7 != None:
            if xbow != None:
                if skeletons != None and elixer > 2:
                    pyautogui.click(skeletons)
                    pyautogui.click(xbow)
            else:
                if priority5 == 1:
                    if bats != None and elixer > 1:
                        pyautogui.click(bats)
                        if my_bridge_left4 != None:
                            pyautogui.click(my_bridge_left4)
                        if my_bridge_left5 != None:
                            pyautogui.click(my_bridge_left5)
                        if my_bridge_left7 != None:
                            pyautogui.click(my_bridge_left7)
                        priority5 = 1
                    else: priority5 = priority5 + 1
                if priority5 == 2:
                    if skeletons != None and elixer > 2:
                        pyautogui.click(skeletons)
                        time.sleep(0.05)
                        pyautogui.click(921, 614)
                        priority5 = 1
                    else: priority5 = priority5 + 1
                if priority5 == 3:
                    if goblins != None and elixer > 1:
                        pyautogui.click(goblins)
                        time.sleep(0.05)
                        pyautogui.click(922, 577)
                        priority5 = 1
                    else: priority5 = priority5 + 1
                if priority5 == 4:
                    if valk != None and elixer > 3:
                        pyautogui.click(valk)
                        if my_bridge_left4 != None:
                            pyautogui.click(my_bridge_left4)
                        if my_bridge_left5 != None:
                            pyautogui.click(my_bridge_left5)
                        if my_bridge_left7 != None:
                            pyautogui.click(my_bridge_left7)
                        priority5 = 1
                    else: priority5 = priority5 + 1
                if priority5 == 5:
                    if archer != None and elixer > 2:
                        pyautogui.click(archer)
                        time.sleep(0.05)
                        pyautogui.click(922, 577)
                        priority5 = 1
                    else: priority5 = 1



        # ENEMY AT BRIDGE RIGHT
        if my_bridge_right4 != None or my_bridge_right5 != None or my_bridge_right7 != None:
            if xbow != None:
                if skeletons != None and elixer > 2:
                    pyautogui.click(skeletons)
                    pyautogui.click(xbow)
            else:
                if priority6 == 1:
                    if bats != None and elixer > 1:
                        pyautogui.click(bats)
                        if my_bridge_right4 != None:
                            pyautogui.click(my_bridge_right4)
                        if my_bridge_right5 != None:
                            pyautogui.click(my_bridge_right5)
                        if my_bridge_right7 != None:
                            pyautogui.click(my_bridge_right7)
                        priority6 = 1
                    else: priority6 = priority6 + 1
                if priority6 == 2:
                    if skeletons != None and elixer > 2:
                        pyautogui.click(skeletons)
                        time.sleep(0.05)
                        pyautogui.click(948, 614)
                        priority6 = 1
                    else: priority6 = priority6 + 1
                if priority6 == 3:
                    if goblins != None and elixer > 1:
                        pyautogui.click(goblins)
                        time.sleep(0.05)
                        pyautogui.click(955, 577)
                        priority6 = 1
                    else: priority6 = priority6 + 1
                if priority6 == 4:
                    if valk != None and elixer > 3:
                        pyautogui.click(valk)
                        if my_bridge_right4 != None:
                            pyautogui.click(my_bridge_right4)
                        if my_bridge_right5 != None:
                            pyautogui.click(my_bridge_right5)
                        if my_bridge_right7 != None:
                            pyautogui.click(my_bridge_right7)
                        priority6 = 1
                    else: priority6 = priority6 + 1
                if priority6 == 5:
                    if archer != None and elixer > 2:
                        pyautogui.click(archer)
                        time.sleep(0.05)
                        pyautogui.click(955, 577)
                        priority6 = 1
                    else: priority6 = 1


        #Enemy near bridge left
        if enemy_bridge_left4 != None or enemy_bridge_left5 != None or enemy_bridge_left7 != None:
            if xbow != None:
                if skeletons != None and elixer > 2:
                    pyautogui.click(skeletons)
                    pyautogui.click(xbow)
            else:
                if priority7 == 1:
                    if bats != None and elixer > 1:
                        pyautogui.click(bats)
                        if enemy_bridge_left4 != None:
                            pyautogui.click(enemy_bridge_left4)
                        if enemy_bridge_left5 != None:
                            pyautogui.click(enemy_bridge_left5)
                        if enemy_bridge_left7 != None:
                            pyautogui.click(enemy_bridge_left7)
                        priority7 = 1
                    else: priority7 = priority7 + 1
                if priority7 == 2:
                    if skeletons != None and elixer > 2:
                        pyautogui.click(skeletons)
                        time.sleep(0.05)
                        pyautogui.click(901, 653)
                        priority7 = 1
                    else: priority7 = priority7 + 1
                if priority7 == 3:
                    if valk != None and elixer > 3:
                        pyautogui.click(valk)
                        time.sleep(0.05)
                        pyautogui.click(901, 653)
                        priority7 = 1
                    else: priority7 = priority7 + 1
                if priority7 == 4:
                    if goblins != None and elixer > 1:
                        pyautogui.click(goblins)
                        time.sleep(0.05)
                        pyautogui.click(927, 578)
                        priority7 = 1
                    else: priority7 = priority7 + 1
                if priority7 == 5:
                    if archer != None and elixer > 2:
                        pyautogui.click(archer)
                        time.sleep(0.05)
                        pyautogui.click(927, 578)
                        priority7 = 1
                    else: priority7 = 1


        #Enemy near bridge right
        if enemy_bridge_right4 != None or enemy_bridge_right5 != None or enemy_bridge_right7 != None:
            if xbow != None:
                if skeletons != None and elixer > 2:
                    pyautogui.click(skeletons)
                    pyautogui.click(xbow)
            else:
                if priority8 == 1:
                    if bats != None and elixer > 1:
                        pyautogui.click(bats)
                        if enemy_bridge_right4 != None:
                            pyautogui.click(enemy_bridge_right4)
                        if enemy_bridge_right5 != None:
                            pyautogui.click(enemy_bridge_right5)
                        if enemy_bridge_right7 != None:
                            pyautogui.click(enemy_bridge_right7)
                        priority8 = 1
                    else: priority8 = priority8 + 1
                if priority8 == 2:
                    if skeletons != None and elixer > 2:
                        pyautogui.click(skeletons)
                        time.sleep(0.05)
                        pyautogui.click(963, 653)
                        priority8 = 1
                    else: priority8 = priority8 + 1
                if priority8 == 3:
                    if valk != None and elixer > 3:
                        pyautogui.click(valk)
                        time.sleep(0.05)
                        pyautogui.click(963, 653)
                        priority8 = 1
                    else: priority8 = priority8 + 1
                if priority8 == 4:
                    if goblins != None and elixer > 1:
                        pyautogui.click(goblins)
                        time.sleep(0.05)
                        pyautogui.click(973, 578)
                        priority8 = 1
                    else: priority8 = priority8 + 1
                if priority8 == 5:
                    if archer != None and elixer > 2:
                        pyautogui.click(archer)
                        time.sleep(0.05)
                        pyautogui.click(973, 578)
                        priority8 = 1
                    else: priority8 = 1


        #Enemy middle left
        if enemy_mid_left4 != None or enemy_mid_left5 != None or enemy_mid_left7 != None:
            if priority9 == 1:
                if bats != None and elixer > 1:
                    pyautogui.click(bats)
                    if enemy_mid_left4 != None:
                        pyautogui.click(enemy_mid_left4)
                    if enemy_mid_left5 != None:
                        pyautogui.click(enemy_mid_left5)
                    if enemy_mid_left7 != None:
                        pyautogui.click(enemy_mid_left7)
                    priority9 = 1
                else: priority9 = priority9 + 1
            if priority9 == 2:
                if skeletons != None and elixer > 2:
                    pyautogui.click(skeletons)
                    time.sleep(0.05)
                    pyautogui.click(901, 653)
                    priority9 = 1
                else: priority9 = priority9 + 1
            if priority9 == 3:
                if valk != None and elixer > 3:
                    pyautogui.click(valk)
                    time.sleep(0.05)
                    pyautogui.click(901, 653)
                    priority9 = 1
                else: priority9 = priority9 + 1
            if priority9 == 4:
                if goblins != None and elixer > 1:
                    pyautogui.click(goblins)
                    time.sleep(0.05)
                    pyautogui.click(927, 578)
                    priority9 = 1
                else: priority9 = priority9 + 1
            if priority9 == 5:
                if archer != None and elixer > 2:
                    pyautogui.click(archer)
                    time.sleep(0.05)
                    pyautogui.click(927, 578)
                    priority9 = 1
                else: priority9 = 1


        #Enemy middle right
        if enemy_mid_right4 != None or enemy_mid_right5 != None or enemy_mid_right7 != None:
            if priority10 == 1:
                if bats != None and elixer > 1:
                    pyautogui.click(bats)
                    if enemy_mid_right4 != None:
                        pyautogui.click(enemy_mid_right4)
                    if enemy_mid_right5 != None:
                        pyautogui.click(enemy_mid_right5)
                    if enemy_mid_right7 != None:
                        pyautogui.click(enemy_mid_right7)
                    priority10 = 1
                else: priority10 = priority10 + 1
            if priority10 == 2:
                if skeletons != None and elixer > 2:
                    pyautogui.click(skeletons)
                    time.sleep(0.05)
                    pyautogui.click(963, 653)
                    priority10 = 1
                else: priority10 = priority10 + 1
            if priority10 == 3:
                if valk != None and elixer > 3:
                    pyautogui.click(valk)
                    time.sleep(0.05)
                    pyautogui.click(963, 653)
                    priority10 = 1
                else: priority10 = priority10 + 1
            if priority10 == 4:
                if goblins != None and elixer > 1:
                    pyautogui.click(goblins)
                    time.sleep(0.05)
                    pyautogui.click(973, 578)
                    priority10 = 1
                else: priority10 = priority10 + 1
            if priority10 == 5:
                if archer != None and elixer > 2:
                    pyautogui.click(archer)
                    time.sleep(0.05)
                    pyautogui.click(973, 578)
                    priority10 = 1
                else: priority10 = 1


        #Enemy at their tower left
        if enemy_towers_left4 != None or enemy_towers_left5 != None or enemy_towers_left7 != None:
            if priority11 == 1:
                if witch != None and elixer > 6:
                    pyautogui.click(witch)
                    time.sleep(2)
                    pyautogui.click(892, 766)
                    priority11 = 1
                else: priority11 = priority11 + 1
            if priority11 == 2:
                if archer != None and elixer > 2:
                    pyautogui.click(archer)
                    time.sleep(0.05)
                    pyautogui.click(892, 780)
                    priority11 = 1
                else: priority11 = priority11 + 1
            if priority11 == 3:
                if goblins != None and elixer > 1:
                    pyautogui.click(goblins)
                    time.sleep(0.05)
                    pyautogui.click(892, 780)
                    priority11 = 1
                else: priority11 = priority11 + 1
            if priority11 == 4:
                if valk != None and elixer > 3:
                    pyautogui.click(valk)
                    time.sleep(0.05)
                    pyautogui.click(881, 690)
                    priority11 = 1
                else: priority11 = priority11 + 1
            if priority11 == 5:
                if bats != None and elixer > 1:
                    pyautogui.click(bats)
                    time.sleep(4)
                    pyautogui.click(713, 762)
                    priority11 = 1
                else: priority11 = 1


        #Enemy at their tower right
        if enemy_towers_right4 != None or enemy_towers_right5 != None or enemy_towers_right7 != None:
            if priority12 == 1:
                if witch != None and elixer > 6:
                    pyautogui.click(witch)
                    time.sleep(2)
                    pyautogui.click(984, 766)
                    time.sleep(0.05)
                    priority12 = 1
                else: priority12 = priority12 + 1
            if priority12 == 2:
                if archer != None and elixer > 2:
                    pyautogui.click(archer)
                    time.sleep(0.05)
                    pyautogui.click(975, 780)
                    priority12 = 1
                else: priority12 = priority12 + 1
            if priority12 == 3:
                if goblins != None and elixer > 1:
                    pyautogui.click(goblins)
                    time.sleep(0.05)
                    pyautogui.click(975, 780)
                    priority12 = 1
                else: priority12 = priority12 + 1
            if priority12 == 4:
                if valk != None and elixer > 3:
                    pyautogui.click(valk)
                    time.sleep(0.05)
                    pyautogui.click(987, 690)
                    priority12 = 1
                else: priority12 = priority12 + 1
            if priority12 == 5:
                if bats != None and elixer > 1:
                    pyautogui.click(bats)
                    time.sleep(4)
                    pyautogui.click(1155, 762)
                    priority12 = 1
                else: priority12 = 1


        #offence
        if elixer > 7 and my_towers_left4 == None and my_towers_left5 == None and my_towers_left7 == None and my_towers_right4 == None and my_towers_right5 == None and my_towers_right7 == None and my_mid_left4 == None and my_mid_left5 == None and my_mid_left7 == None and my_mid_right4 == None and my_mid_right5 == None and my_mid_right7 == None and my_bridge_left4 == None and my_bridge_left5 == None and my_bridge_left7 == None and my_bridge_right4 == None and my_bridge_right5 == None and my_bridge_right7 == None:
            if priority13 == 1:
                if hut != None and elixer > 7:
                    import random
                    pyautogui.click(hut)
                    x = random.randrange(1, 5)
                    if x == 1: pyautogui.click(737, 737)
                    if x == 2: pyautogui.click(1139, 737)
                    if x == 3: pyautogui.click(1003, 622)
                    if x == 4: pyautogui.click(869, 622)
                    if x == 5: pyautogui.click(934, 588)
                    priority13 = 1
                else: priority13 = priority13 + 1
            if priority13 == 2:
                if ram != None and elixer > 8:
                    bprl = 0
                    bprr = 0
                    s = 0
                    pyautogui.click(ram)
                    if enemy_towers_left4 == None and enemy_towers_left5 == None and enemy_towers_left7 == None:
                        bprl = bprl + 1
                    if enemy_mid_left4 == None and enemy_mid_left5 == None and enemy_mid_left7 == None:
                        bprl = bprl + 1
                    if enemy_towers_right4 == None and enemy_towers_right5 == None and enemy_towers_right7 == None:
                        bprr = bprr + 1
                    if enemy_mid_right4 == None and enemy_mid_right5 == None and enemy_mid_right7 == None:
                        bprr = bprr + 1

                    if bprl > bprr:
                        s = 1
                    if bprl < bprr:
                        s = 2
                    if bprl == bprr:
                        s = 0

                    if s == 0:
                        import random
                        x = random.randrange(1, 2)
                        if x == 1: pyautogui.click(794, 257)
                        if x == 2: pyautogui.click(1086, 257)
                    else:
                        if s == 1: pyautogui.click(794, 257)
                        if s == 2: pyautogui.click(1086, 257)
                    priority13 = 1
                else: priority13 = priority13 + 1
            if priority13 == 3:
                if witch != None and elixer > 7:
                    import random
                    pyautogui.click(witch)
                    x1 = random.randrange(1, 2)
                    if x1 == 1: pyautogui.click(987, 765)
                    if x1 == 2: pyautogui.click(879, 765)
                    priority13 = 1
                else: priority13 = 1

    if pyautogui.locateCenterOnScreen("d:\\cr.ss\\place1.png", confidence=0.7) != None: pyautogui.click(834, 681)

    if pyautogui.locateCenterOnScreen("D:\\cr.ss\\place3.png", region=(836, 855, 220, 110), confidence=0.6) != None: pyautogui.click(897, 904)

    if pyautogui.locateCenterOnScreen("D:\\cr.ss\\yes.png", region=(859, 614, 154, 96), confidence=0.6) != None: pyautogui.click(940, 655)