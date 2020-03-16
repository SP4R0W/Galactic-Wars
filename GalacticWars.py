import pygame
import math
import pickle
import random as r

from engine import *
from time import sleep
from pygame_functions import *

guardians = "Assets/Fonts/guardians.ttf"

button = "Assets/Images/GUI/button.png"

spaceSprite = makeSprite("Assets/Images/Ship/gameSprite.png")

menuImages = ["Assets/Images/Backgrounds/space1.png",
                   "Assets/Images/Backgrounds/space2.png",
                   "Assets/Images/Backgrounds/space3.png"]

planetSelectImages = ["Assets/Images/GUI/LevelChoose/planet1.png",
                     "Assets/Images/GUI/LevelChoose/planet2.png",
                     "Assets/Images/GUI/LevelChoose/planet3.png",
                     "Assets/Images/GUI/LevelChoose/planet4.png"]

levelSelectImages = ["Assets/Images/GUI/Levels/1.png",#0
               "Assets/Images/GUI/Levels/2.png", #1
               "Assets/Images/GUI/Levels/3.png",#2
               "Assets/Images/GUI/Levels/4.png",#3
               "Assets/Images/GUI/Levels/5.png",#4
               "Assets/Images/GUI/Levels/6.png",#5
               "Assets/Images/GUI/Levels/buttonlock.png",#6
               "Assets/Images/GUI/Levels/buttontick.png", #7
               "Assets/Images/GUI/Levels/cutscene.png"]#8

menuSounds = ["Assets/Sounds/GUI/Menu/title.wav",
              "Assets/Sounds/GUI/Menu/button.wav",
              "Assets/Sounds/Menu/theme.wav"]

otherSounds = ["Assets/Sounds/GUI/Other/click.wav",
               "Assets/Sounds/GUI/Other/hover.wav"]

gameLose = "Assets/Sounds/Game/gameLose.wav"

winTheme = "Assets/Sounds/Game/winTheme.wav"

global gameThings
gameThings = {"Newgame":True,

              "Money":0,

              "Planet2Active":levelSelectImages[6],
              "Planet3Active":levelSelectImages[6],
              "Planet4Active":levelSelectImages[6],
              "EndingActive":False,

              "Health":25,
              "Speed":0.1,
              "MaxSpeed":15,
              "Damage":5,

              "HealthCost":750,
              "HealthBought":0,

              "SpeedCost":500,
              "SpeedBought":0,

              "DamageCost":1000,
              "DamageBought":0,

              "P1L1":levelSelectImages[0],
              "P1L2":levelSelectImages[6],
              "P1L3":levelSelectImages[6],
              "P1L4":levelSelectImages[6],

              "P2L1":levelSelectImages[0],
              "P2L2":levelSelectImages[6],
              "P2L3":levelSelectImages[6],
              "P2L4":levelSelectImages[6],
              "P2L5":levelSelectImages[6],
              "P2L6":levelSelectImages[6],
              
              "P3L1":levelSelectImages[0],
              "P3L2":levelSelectImages[6],
              "P3L3":levelSelectImages[6],
              "P3L4":levelSelectImages[6],
              "P3L5":levelSelectImages[6],
              
              "P4L1":levelSelectImages[0],
              "P4L2":levelSelectImages[6],
              "P4L3":levelSelectImages[6],
              "P4L4":levelSelectImages[6],
              "P4L5":levelSelectImages[6],}

pygame.init()
pygame.display.set_caption("Galactic Wars")
icon = pygame.image.load("Assets/Images/icon.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

gameWindow = pygame.display.set_mode((800,600))
gameWindow.fill(white)
pygame.display.update()

class saveFunctions:

    def saveGame():

        saveFile = open("Assets\Data\saveData.pickle",'wb')
        pickle.dump(gameThings,saveFile)
        saveFile.close()

    def loadGame():
        global gameThings

        loadFile = open("Assets\Data\saveData.pickle",'rb')
        gameThings = pickle.load(loadFile)
        print(gameThings)

class shopFunctions:

    global gameThings

    def buyHealth():
        m = int(gameThings["Money"])
        hp = int(gameThings["HealthCost"])
        h = int(gameThings["Health"])
        hb = int(gameThings["HealthBought"])

        if m >= hp:
            m -= hp
            h = h + 5
            hp = hp + 500
            hb += 1

            gameThings["Money"] = m
            gameThings["HealthCost"] = hp
            gameThings["Health"] = h
            gameThings["HealthBought"] = hb

            saveFunctions.saveGame()
            menu.gameShop()

    def buySpeed():
        m = int(gameThings["Money"])
        hp = int(gameThings["SpeedCost"])
        h = int(gameThings["Speed"])
        h1 = int(gameThings["MaxSpeed"])
        hb = int(gameThings["SpeedBought"])

        if m >= hp:
            m -= hp
            h = h + 0.1
            h1 = h1 + 5
            hp = hp + 350
            hb += 1

            gameThings["Money"] = m
            gameThings["SpeedCost"] = hp
            gameThings["Speed"] = h
            gameThings["MaxSpeed"] = h1
            gameThings["SpeedBought"] = hb

            saveFunctions.saveGame()
            menu.gameShop()

    def buyDamage():
        m = int(gameThings["Money"])
        hp = int(gameThings["DamageCost"])
        h = int(gameThings["Damage"])
        hb = int(gameThings["DamageBought"])

        if m >= hp:
            m -= hp
            h = math.floor(h * 1.3)
            hp = hp + 500
            hb += 1

            gameThings["Money"] = m
            gameThings["DamageCost"] = hp
            gameThings["Damage"] = h
            gameThings["DamageBought"] = hb

            saveFunctions.saveGame()
            menu.gameShop()

class menu:

    def MainMenu():
        mainmenu = True

        pygame.mixer.music.stop()

        bg = r.choice(menuImages)

        y = -75
        x = -75

        #Draw the title
        titleSound = Sound(menuSounds[0]).play()

        while y <= 50:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(85,y,"GALACTIC WARS",guardians,48,fadeColors[0]).draw()
            y += 2.5
            pygame.display.update()

        #Draw the button
        while x <= 325:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(85,50,"GALACTIC WARS",guardians,48,fadeColors[0]).draw()

            startButton = ImageButton(x,300,button,width=150,height=56,
                                          normalColor=black).draw()
            x += 12.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        pygame.mixer.music.stop()
        theme = Music(menuSounds[2],looped=-1).play()

        #saveFunctions.saveGame()

        while mainmenu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            b = Image(0,0,bg).draw()

            title = Text(85,50,"GALACTIC WARS",guardians,48,fadeColors[0]).draw()

            startButton = ImageButton(325,300,button,width=150,height=56,
                                      normalColor=black,
                                      text="START",
                                      font=guardians,
                                      fontSize=22,
                                      textx=340.5,
                                      texty=313,
                                      fontColor=white,
                                      clickSound=otherSounds[0],
                                      action=menu.planetSelect).draw()

            pygame.display.update()
            clock.tick(60)

    def planetSelect():
        saveFunctions.loadGame()

        if gameThings["Newgame"] == True:
            cutscenes.newGameCutscene()
        else:
            mainmenu = False
            planetselect = True

            gameWindow.fill(white)

            bg = r.choice(menuImages)
        
            y = -75
            x = -75

            #Draw the title
            while y <= 25:
                gameWindow.fill(white)
                b = Image(0,0,bg).draw()
                title = Text(35,y,"CHOOSE A PLANET",guardians,48,fadeColors[0]).draw()
                y += 2.5
                pygame.display.update()

            #Draw button
            y = 900

            while y >= 480:
                gameWindow.fill(white)
                b = Image(0,0,bg).draw()
                title = Text(35,25,"CHOOSE A PLANET",guardians,48,fadeColors[0]).draw()

                shopButton = ImageButton(200,y,button,width=150,height=56,
                                             normalColor=black).draw()
                y -= 12.5
                pygame.display.update()

            buttonSound = Sound(menuSounds[1],0.05).play()

            #Draw the second button
            y = 900

            while y >= 480:
                gameWindow.fill(white)
                b = Image(0,0,bg).draw()
                title = Text(35,25,"CHOOSE A PLANET",guardians,48,fadeColors[0]).draw()
                shopButton = ImageButton(200,480,button,width=150,height=56,
                                             normalColor=black).draw()

                shopButton = ImageButton(450,y,button,width=150,height=56,
                                             normalColor=black).draw()
                y -= 12.5
                pygame.display.update()

            buttonSound = Sound(menuSounds[1],0.05).play()


            while planetselect:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                title = Text(35,25,"CHOOSE A PLANET",guardians,48,fadeColors[0]).draw()

                p1 = Image(25,135,planetSelectImages[0]).draw()
                level1 = ImageButton(40,285,levelSelectImages[0],99,97,normalColor=black,clickSound=otherSounds[0],action=menu.levelSelect1).draw()

                p2 = Image(235,135,planetSelectImages[1]).draw()
                level2 = ImageButton(247,285,gameThings["Planet2Active"],99,97,normalColor=black,clickSound=otherSounds[0],action=menu.levelSelect2).draw()

                p3 = Image(445,135,planetSelectImages[2]).draw()
                level3 = ImageButton(460,285,gameThings["Planet3Active"],99,97,normalColor=black,clickSound=otherSounds[0],action=menu.levelSelect3).draw()

                p4 = Image(650,135,planetSelectImages[3]).draw()
                level4 = ImageButton(665,285,gameThings["Planet4Active"],99,97,normalColor=black,clickSound=otherSounds[0],action=menu.levelSelect4).draw()

                shopButton = ImageButton(200,480,button,width=150,height=56,
                                          normalColor=black,
                                          text="SHOP",
                                          font=guardians,
                                          fontSize=22,
                                          textx=230,
                                          texty=493,
                                          fontColor=white,
                                          clickSound=otherSounds[0],
                                          action=menu.gameShop).draw()

                backButton = ImageButton(450,480,button,width=150,height=56,
                                          normalColor=black,
                                          text="BACK",
                                          font=guardians,
                                          fontSize=22,
                                          textx=480,
                                          texty=493,
                                          fontColor=white,
                                          clickSound=otherSounds[0],
                                          action=menu.MainMenu).draw()

                pygame.display.update()
                clock.tick(60)

    def gameShop():
        planetselect = False
        shop = True

        saveFunctions.loadGame()

        gameWindow.fill(white)

        bg = r.choice(menuImages)
        
        y = -75
        x = -75

        #Draw the title
        while y <= 25:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(20,y,"UPGRADE THE SHIP",guardians,48,fadeColors[0]).draw()
            y += 2.5
            pygame.display.update()

        #Draw button
        y = 900

        while y >= 480:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(20,25,"UPGRADE THE SHIP",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,y,button,width=150,height=56,
                                         normalColor=black).draw()
            y -= 12.5
            pygame.display.update()

        while shop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            x,y = pygame.mouse.get_pos()
            print(x,y)

            title = Text(20,25,"UPGRADE THE SHIP",guardians,48,fadeColors[0]).draw()
            money = Text(15,115,"Your money amount is "+str(gameThings["Money"]),guardians,22,fadeColors[0]).draw()

            health = Text(25,180,"Extra Armor "+str(gameThings["HealthCost"]),guardians,18,fadeColors[0]).draw()
            speed = Text(505,180,"Extra Speed "+str(gameThings["SpeedCost"]),guardians,18,fadeColors[0]).draw()
            damage = Text(245,325,"Extra Damage "+str(gameThings["DamageCost"]),guardians,18,fadeColors[0]).draw()                    

            hb = int(gameThings["HealthBought"])
            sb = int(gameThings["SpeedBought"])
            db = int(gameThings["DamageBought"])

            if hb != 5:
                upgradeHealthButton = ImageButton(105,215,button,width=150,height=56,
                                          normalColor=black,
                                          text="BUY",
                                          font=guardians,
                                          fontSize=22,
                                          textx=150,
                                          texty=228,
                                          fontColor=white,
                                          clickSound=otherSounds[0],
                                          action=shopFunctions.buyHealth).draw()

            if sb != 3:
                upgradeSpeedButton = ImageButton(575,215,button,width=150,height=56,
                                          normalColor=black,
                                          text="BUY",
                                          font=guardians,
                                          fontSize=22,
                                          textx=620,
                                          texty=228,
                                          fontColor=white,
                                          clickSound=otherSounds[0],
                                          action=shopFunctions.buySpeed).draw()
            if db != 5:
                upgradeDamageButton = ImageButton(325,365,button,width=150,height=56,
                                          normalColor=black,
                                          text="BUY",
                                          font=guardians,
                                          fontSize=22,
                                          textx=375,
                                          texty=378,
                                          fontColor=white,
                                          clickSound=otherSounds[0],
                                          action=shopFunctions.buyDamage).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                      normalColor=black,
                                      text="BACK",
                                      font=guardians,
                                      fontSize=22,
                                      textx=355,
                                      texty=493,
                                      fontColor=white,
                                      clickSound=otherSounds[0],
                                      action=menu.planetSelect).draw()

            pygame.display.update()
            clock.tick(60)

    def levelPlay(level,state=""):
        if state != levelSelectImages[6]:
            pygame.mixer.music.stop()
            level()
            pygame.quit()
            quit()

    def levelSelect1():
        import GalacticMissions

        planetselect = False
        levelselect = True
        
        gameWindow.fill(white)

        bg = r.choice(menuImages)
        
        y = -75
        x = -75

        #Draw the title
        while y <= 25:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(50,y,"CHOOSE A LEVEL",guardians,48,fadeColors[0]).draw()
            y += 2.5
            pygame.display.update()

        #Draw the button
        y = 900

        while y >= 480:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(50,25,"CHOOSE A LEVEL",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,y,button,width=150,height=56,
                                     normalColor=black).draw()
            y -= 12.5
            pygame.display.update()


        while levelselect:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            title = Text(50,25,"CHOOSE A LEVEL",guardians,48,fadeColors[0]).draw()

            level1 = ImageButton(50,165,gameThings["P1L1"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P1L1)).draw()
            level2 = ImageButton(235,175,gameThings["P1L2"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P1L2,gameThings["P1L2"])).draw()
            level3 = ImageButton(445,190,gameThings["P1L3"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P1L3,gameThings["P1L3"])).draw()
            level4 = ImageButton(655,180,gameThings["P1L4"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P1L4,gameThings["P1L4"])).draw()

            if gameThings["Planet2Active"] != levelSelectImages[6]:
                cutscene = ImageButton(345,340,levelSelectImages[8],99,97,normalColor=black,clickSound=otherSounds[0],action=cutscenes.episode1Cutscene).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                      normalColor=black,
                                      text="BACK",
                                      font=guardians,
                                      fontSize=22,
                                      textx=355,
                                      texty=493,
                                      fontColor=white,
                                      clickSound=otherSounds[0],
                                      action=menu.planetSelect).draw()

            pygame.display.update()
            clock.tick(60)

    def levelSelect2():
        if gameThings["Planet2Active"] == levelSelectImages[6]:
            print("nein")

        else:
            import GalacticMissions

            planetselect = False
            levelselect = True
        
            gameWindow.fill(white)

            bg = r.choice(menuImages)

            b = Image(0,0,bg).draw()
        
            y = -75
            x = -75

            #Draw the title
            while y <= 25:
                gameWindow.fill(white)
                b = Image(0,0,bg).draw()
                title = Text(50,y,"CHOOSE A LEVEL",guardians,48,fadeColors[0]).draw()
                y += 2.5
                pygame.display.update()

            #Draw the button
            y = 900

            while y >= 480:
                gameWindow.fill(white)
                b = Image(0,0,bg).draw()
                title = Text(50,25,"CHOOSE A LEVEL",guardians,48,fadeColors[0]).draw()

                backButton = ImageButton(325,y,button,width=150,height=56,
                                         normalColor=black).draw()
                y -= 12.5
                pygame.display.update()

            buttonSound = Sound(menuSounds[1],0.05).play()

            while levelselect:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                title = Text(50,25,"CHOOSE A LEVEL",guardians,48,fadeColors[0]).draw()

                level1 = ImageButton(25,175,gameThings["P2L1"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P2L1)).draw()
                level2 = ImageButton(165,220,gameThings["P2L2"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P2L2,gameThings["P2L2"])).draw()
                level3 = ImageButton(295,185,gameThings["P2L3"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P2L3,gameThings["P2L3"])).draw()
                level4 = ImageButton(425,200,gameThings["P2L4"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P2L4,gameThings["P2L4"])).draw()
                level5 = ImageButton(555,210,gameThings["P2L5"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P2L5,gameThings["P2L5"])).draw()
                level6 = ImageButton(675,205,gameThings["P2L6"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P2L6,gameThings["P2L6"])).draw()

                if gameThings["Planet3Active"] != levelSelectImages[6]:
                    cutscene = ImageButton(345,340,levelSelectImages[8],99,97,normalColor=black,clickSound=otherSounds[0],action=cutscenes.episode2Cutscene).draw()

                backButton = ImageButton(325,480,button,width=150,height=56,
                                          normalColor=black,
                                          text="BACK",
                                          font=guardians,
                                          fontSize=22,
                                          textx=355,
                                          texty=493,
                                          fontColor=white,
                                          clickSound=otherSounds[0],
                                          action=menu.planetSelect).draw()

                pygame.display.update()
                clock.tick(60)

    def levelSelect3():
        if gameThings["Planet3Active"] == levelSelectImages[6]:
            print("nein")

        else:
            import GalacticMissions

            planetselect = False
            levelselect = True
        
            gameWindow.fill(white)

            bg = r.choice(menuImages)

            b = Image(0,0,bg).draw()
        
            y = -75
            x = -75

            #Draw the title
            while y <= 25:
                gameWindow.fill(white)
                b = Image(0,0,bg).draw()
                title = Text(50,y,"CHOOSE A LEVEL",guardians,48,fadeColors[0]).draw()
                y += 2.5
                pygame.display.update()

            #Draw the button
            y = 900

            while y >= 480:
                gameWindow.fill(white)
                b = Image(0,0,bg).draw()
                title = Text(50,25,"CHOOSE A LEVEL",guardians,48,fadeColors[0]).draw()

                backButton = ImageButton(325,y,button,width=150,height=56,
                                         normalColor=black).draw()
                y -= 12.5
                pygame.display.update()

            buttonSound = Sound(menuSounds[1],0.05).play()

            while levelselect:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                x,y = pygame.mouse.get_pos()
                print(x,y)

                title = Text(50,25,"CHOOSE A LEVEL",guardians,48,fadeColors[0]).draw()

                level1 = ImageButton(30,175,gameThings["P3L1"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P3L1)).draw()
                level2 = ImageButton(175,155,gameThings["P3L2"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P3L2,gameThings["P3L2"])).draw()
                level3 = ImageButton(340,185,gameThings["P3L3"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P3L3,gameThings["P3L3"])).draw()
                level4 = ImageButton(500,200,gameThings["P3L4"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P3L4,gameThings["P3L4"])).draw()
                level5 = ImageButton(650,180,gameThings["P3L5"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P3L5,gameThings["P3L5"])).draw()

                if gameThings["Planet4Active"] != levelSelectImages[6]:
                    cutscene = ImageButton(345,340,levelSelectImages[8],99,97,normalColor=black,clickSound=otherSounds[0],action=cutscenes.episode3Cutscene).draw()

                backButton = ImageButton(325,480,button,width=150,height=56,
                                          normalColor=black,
                                          text="BACK",
                                          font=guardians,
                                          fontSize=22,
                                          textx=355,
                                          texty=493,
                                          fontColor=white,
                                          clickSound=otherSounds[0],
                                          action=menu.planetSelect).draw()

                pygame.display.update()
                clock.tick(60)

    def levelSelect4():
        if gameThings["Planet4Active"] == levelSelectImages[6]:
            print("nein")

        else:
            import GalacticMissions

            planetselect = False
            levelselect = True
        
            gameWindow.fill(white)

            bg = r.choice(menuImages)

            b = Image(0,0,bg).draw()
        
            y = -75
            x = -75

            #Draw the title
            while y <= 25:
                gameWindow.fill(white)
                b = Image(0,0,bg).draw()
                title = Text(50,y,"CHOOSE A LEVEL",guardians,48,fadeColors[0]).draw()
                y += 2.5
                pygame.display.update()

            #Draw the button
            y = 900

            while y >= 480:
                gameWindow.fill(white)
                b = Image(0,0,bg).draw()
                title = Text(50,25,"CHOOSE A LEVEL",guardians,48,fadeColors[0]).draw()

                backButton = ImageButton(325,y,button,width=150,height=56,
                                         normalColor=black).draw()
                y -= 12.5
                pygame.display.update()

            buttonSound = Sound(menuSounds[1],0.05).play()

            while levelselect:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                x,y = pygame.mouse.get_pos()
                print(x,y)

                title = Text(50,25,"CHOOSE A LEVEL",guardians,48,fadeColors[0]).draw()

                level1 = ImageButton(30,185,gameThings["P4L1"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P4L1)).draw()
                level2 = ImageButton(175,205,gameThings["P4L2"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P4L2,gameThings["P4L2"])).draw()
                level3 = ImageButton(340,185,gameThings["P4L3"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P4L3,gameThings["P4L3"])).draw()
                level4 = ImageButton(500,205,gameThings["P4L4"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P4L4,gameThings["P4L4"])).draw()
                level5 = ImageButton(650,195,gameThings["P4L5"],99,97,normalColor=black,clickSound=otherSounds[0],action=lambda:menu.levelPlay(GalacticMissions.game.P4L5,gameThings["P4L5"])).draw()

                if gameThings["EndingActive"] == True:
                    cutscene = ImageButton(345,340,levelSelectImages[8],99,97,normalColor=black,clickSound=otherSounds[0],action=cutscenes.endCutscene).draw()

                backButton = ImageButton(325,480,button,width=150,height=56,
                                          normalColor=black,
                                          text="BACK",
                                          font=guardians,
                                          fontSize=22,
                                          textx=355,
                                          texty=493,
                                          fontColor=white,
                                          clickSound=otherSounds[0],
                                          action=menu.planetSelect).draw()

                pygame.display.update()
                clock.tick(60)

    def missionComplete(score,shot,level):
        global gameThings

        missionEnd = True
        
        gameWindow.fill(white)

        bg = r.choice(menuImages)

        b = Image(0,0,bg).draw()

        money = int(score / 10)
        gameThings["Money"] += money
        
        y = -75
        x = -300

        pygame.mixer.music.stop()

        titleSound = Sound(menuSounds[0]).play()

        #Draw the title
        while y <= 25:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(50,y,"MISSION COMPLETE",guardians,48,fadeColors[0]).draw()
            y += 2.5
            pygame.display.update()

        #Draw the button
        y = 900

        while y >= 480:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(50,25,"MISSION COMPLETE",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,y,button,width=150,height=56,
                                    normalColor=black).draw()
            y -= 12.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        #Draw the text
        while x <= 40:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(50,25,"MISSION COMPLETE",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                    normalColor=black).draw()

            killed = Text(x,175,"YOU HAVE KILLED " + str(shot) +" ENEMIES",guardians,28,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300
        while x <= 40:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(50,25,"MISSION COMPLETE",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                    normalColor=black).draw()
            killed = Text(40,175,"YOU HAVE KILLED " + str(shot) +" ENEMIES",guardians,28,fadeColors[0]).draw()

            earned = Text(x,275,"YOU HAVE EARNED " + str(money) +" CASH",guardians,28,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        if level == "P1L1":
            gameThings["P1L1"] = levelSelectImages[7]
            gameThings["P1L2"] = levelSelectImages[1]
        elif level == "P1L2":
            gameThings["P1L2"] = levelSelectImages[7]
            gameThings["P1L3"] = levelSelectImages[2]
        elif level == "P1L3":
            gameThings["P1L3"] = levelSelectImages[7]
            gameThings["P1L4"] = levelSelectImages[3]
        elif level == "P1L4":
            gameThings["P1L4"] = levelSelectImages[7]
            gameThings["Planet2Active"] = levelSelectImages[1]


        elif level == "P2L1":
            gameThings["P2L1"] = levelSelectImages[7]
            gameThings["P2L2"] = levelSelectImages[1]
        elif level == "P2L2":
            gameThings["P2L2"] = levelSelectImages[7]
            gameThings["P2L3"] = levelSelectImages[2]
        elif level == "P2L3":
            gameThings["P2L3"] = levelSelectImages[7]
            gameThings["P2L4"] = levelSelectImages[3]
        elif level == "P2L4":
            gameThings["P2L4"] = levelSelectImages[7]
            gameThings["P2L5"] = levelSelectImages[4]
        elif level == "P2L5":
            gameThings["P2L5"] = levelSelectImages[7]
            gameThings["P2L6"] = levelSelectImages[5]
        elif level == "P2L6":
            gameThings["P2L6"] = levelSelectImages[7]
            gameThings["Planet3Active"] = levelSelectImages[2]

        elif level == "P3L1":
            gameThings["P3L1"] = levelSelectImages[7]
            gameThings["P3L2"] = levelSelectImages[1]
        elif level == "P3L2":
            gameThings["P3L2"] = levelSelectImages[7]
            gameThings["P3L3"] = levelSelectImages[2]
        elif level == "P3L3":
            gameThings["P3L3"] = levelSelectImages[7]
            gameThings["P3L4"] = levelSelectImages[3]
        elif level == "P3L4":
            gameThings["P3L4"] = levelSelectImages[7]
            gameThings["P3L5"] = levelSelectImages[4]
        elif level == "P3L5":
            gameThings["P3L5"] = levelSelectImages[7]
            gameThings["Planet4Active"] = levelSelectImages[3]

        elif level == "P4L1":
            gameThings["P4L1"] = levelSelectImages[7]
            gameThings["P4L2"] = levelSelectImages[1]
        elif level == "P4L2":
            gameThings["P4L2"] = levelSelectImages[7]
            gameThings["P4L3"] = levelSelectImages[2]
        elif level == "P4L3":
            gameThings["P4L3"] = levelSelectImages[7]
            gameThings["P4L4"] = levelSelectImages[3]
        elif level == "P4L4":
            gameThings["P4L4"] = levelSelectImages[7]
            gameThings["P4L5"] = levelSelectImages[4]
        elif level == "P4L5":
            gameThings["P4L5"] = levelSelectImages[7]
            gameThings["EndingActive"] = True

        saveFunctions.saveGame()

        mC = Music("Assets/Sounds/Game/gameWin.wav",0,-1).play()

        while missionEnd:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            title = Text(50,25,"MISSION COMPLETE",guardians,48,fadeColors[0]).draw()
            backButton = ImageButton(325,480,button,width=150,height=56,
                                          normalColor=black,
                                          text="BACK",
                                          font=guardians,
                                          fontSize=22,
                                          textx=355,
                                          texty=493,
                                          fontColor=white,
                                          clickSound=otherSounds[0],
                                          action=menu.MainMenu).draw()


            pygame.display.update()
            clock.tick(60)

    def missionFailed():
        missionEnd = True
        
        gameWindow.fill(white)

        bg = r.choice(menuImages)

        b = Image(0,0,bg).draw()
        
        y = -75
        x = -300

        titleSound = Sound(menuSounds[0]).play()

        #Draw the title
        while y <= 25:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(100,y,"MISSION FAILED",guardians,48,fadeColors[0]).draw()
            y += 2.5
            pygame.display.update()

        #Draw the button
        y = 700

        while y >= 480:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(100,25,"MISSION FAILED",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,y,button,width=150,height=56,
                                    normalColor=black).draw()
            y -= 12.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        pygame.mixer.music.stop()
        theme = Music(gameLose,0,-1).play()

        while missionEnd:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            title = Text(100,25,"MISSION FAILED",guardians,48,fadeColors[0]).draw()

            text = Text(35,145,"You have failed your mission.",guardians,28,fadeColors[0]).draw()
            text2 = Text(50,205,"But do not worry. You can",guardians,28,fadeColors[0]).draw()
            text3 = Text(50,265,"always try again at any",guardians,28,fadeColors[0]).draw()
            text4 = Text(80,325,"moment you want to.",guardians,28,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                          normalColor=black,
                                          text="BACK",
                                          font=guardians,
                                          fontSize=22,
                                          textx=355,
                                          texty=493,
                                          fontColor=white,
                                          clickSound=otherSounds[0],
                                          action=menu.MainMenu).draw()

            pygame.display.update()
            clock.tick(60)

class cutscenes:

    def newGameCutscene():
        global gameThings

        cutscene = True
        
        gameWindow.fill(white)

        bg = r.choice(menuImages)
        
        y = -75
        x = -75

        #Draw the title
        while y <= 25:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,y,"STORY",guardians,48,fadeColors[0]).draw()
            y += 2.5
            pygame.display.update()

        #Draw the button
        y = 900

        while y >= 480:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,y,button,width=150,height=56,
                                     normalColor=black).draw()
            y -= 12.5
            pygame.display.update()

        #Draw the text1
        while x <= 40:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()

            text1 = Text(x,175,"THE YEAR IS 2243. AN EARTH LIKE PLANET",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text2
        while x <= 40:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"THE YEAR IS 2243. AN EARTH LIKE PLANET",guardians,18,fadeColors[0]).draw()

            text2 = Text(x,210,"CALLED MOBIUS IS ATTACKED BY ALIEN RACE",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text3
        while x <= 40:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"THE YEAR IS 2243. AN EARTH LIKE PLANET",guardians,18,fadeColors[0]).draw()
            text2 = Text(40,210,"CALLED MOBIUS IS ATTACKED BY ALIEN RACE",guardians,18,fadeColors[0]).draw()

            text3 = Text(x,245,"KNOWN AS BIOTEX. THE MOBIUS' DEFENCES ARE",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text4
        while x <= 10:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"THE YEAR IS 2243. AN EARTH LIKE PLANET",guardians,18,fadeColors[0]).draw()
            text2 = Text(40,210,"CALLED MOBIUS IS ATTACKED BY ALIEN RACE",guardians,18,fadeColors[0]).draw()
            text3 = Text(40,245,"KNOWN AS BIOTEX. THE MOBIUS DEFENCES ARE",guardians,18,fadeColors[0]).draw()

            text4 = Text(x,290,"QUICKLY OVERRAN. HOWEVER WHEN REINFORCEMENTS",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text5
        while x <= 20:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"THE YEAR IS 2243. AN EARTH LIKE PLANET",guardians,18,fadeColors[0]).draw()
            text2 = Text(40,210,"CALLED MOBIUS IS ATTACKED BY ALIEN RACE",guardians,18,fadeColors[0]).draw()
            text3 = Text(40,245,"KNOWN AS BIOTEX. THE MOBIUS DEFENCES ARE",guardians,18,fadeColors[0]).draw()
            text4 = Text(10,290,"QUICKLY OVERRAN. HOWEVER WHEN REINFORCEMENTS",guardians,18,fadeColors[0]).draw()

            text5 = Text(x,335,"GET DRAFTED, YOU SIGN UP AS WELL. YOUR JOB",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text6
        while x <= 20:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"THE YEAR IS 2243. AN EARTH LIKE PLANET",guardians,18,fadeColors[0]).draw()
            text2 = Text(40,210,"CALLED MOBIUS IS ATTACKED BY ALIEN RACE",guardians,18,fadeColors[0]).draw()
            text3 = Text(40,245,"KNOWN AS BIOTEX. THE MOBIUS DEFENCES ARE",guardians,18,fadeColors[0]).draw()
            text4 = Text(10,290,"QUICKLY OVERRAN. HOWEVER WHEN REINFORCEMENTS",guardians,18,fadeColors[0]).draw()
            text5 = Text(20,335,"GET DRAFTED, YOU SIGN UP AS WELL. YOUR JOB",guardians,18,fadeColors[0]).draw()

            text6 = Text(x,370,"NOW IS TO HELP DEFEND MOBIUS AGAINST THE",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text7
        while x <= 60:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"THE YEAR IS 2243. AN EARTH LIKE PLANET",guardians,18,fadeColors[0]).draw()
            text2 = Text(40,210,"CALLED MOBIUS IS ATTACKED BY ALIEN RACE",guardians,18,fadeColors[0]).draw()
            text3 = Text(40,245,"KNOWN AS BIOTEX. THE MOBIUS DEFENCES ARE",guardians,18,fadeColors[0]).draw()
            text4 = Text(10,290,"QUICKLY OVERRAN. HOWEVER WHEN REINFORCEMENTS",guardians,18,fadeColors[0]).draw()
            text5 = Text(20,335,"GET DRAFTED, YOU SIGN UP AS WELL. YOUR JOB",guardians,18,fadeColors[0]).draw()
            text6 = Text(20,370,"NOW IS TO HELP DEFEND MOBIUS AGAINST THE",guardians,18,fadeColors[0]).draw()

            text7 = Text(x,405,"ALIEN ATTACKERS. GOOD LUCK PRIVATE.",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        gameThings["Newgame"] = False
        saveFunctions.saveGame()

        while cutscene:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                      normalColor=black,
                                      text="BACK",
                                      font=guardians,
                                      fontSize=22,
                                      textx=355,
                                      texty=493,
                                      fontColor=white,
                                      clickSound=otherSounds[0],
                                      action=menu.planetSelect).draw()

            pygame.display.update()
            clock.tick(60)

    def episode1Cutscene():
        cutscene = True
        
        gameWindow.fill(white)

        bg = r.choice(menuImages)
        
        y = -75
        x = -75

        #Draw the title
        while y <= 25:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,y,"STORY",guardians,48,fadeColors[0]).draw()
            y += 2.5
            pygame.display.update()

        #Draw the button
        y = 900

        while y >= 480:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,y,button,width=150,height=56,
                                     normalColor=black).draw()
            y -= 12.5
            pygame.display.update()

        #Draw the text1
        while x <= 20:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()

            text1 = Text(x,175,"AFTER THE DEFEAT OF BIOTEX IN MOBIUS THEY",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text2
        while x <= 20:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(20,175,"AFTER THE DEFEAT OF BIOTEX IN MOBIUS THEY",guardians,18,fadeColors[0]).draw()

            text2 = Text(x,210,"ARE FORCED TO PULL BACK TO ANOTHER PLANET",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text3
        while x <= 30:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(20,175,"AFTER THE DEFEAT OF BIOTEX IN MOBIUS THEY",guardians,18,fadeColors[0]).draw()
            text2 = Text(20,210,"ARE FORCED TO PULL BACK TO ANOTHER PLANET",guardians,18,fadeColors[0]).draw()

            text3 = Text(x,245,"CALLED SECCO. A NEW COUNTEROFFENSIVE IS",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text4
        while x <= 30:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(20,175,"AFTER THE DEFEAT OF BIOTEX IN MOBIUS THEY",guardians,18,fadeColors[0]).draw()
            text2 = Text(20,210,"ARE FORCED TO PULL BACK TO ANOTHER PLANET",guardians,18,fadeColors[0]).draw()
            text3 = Text(30,245,"CALLED SECCO. A NEW COUNTEROFFENSIVE IS",guardians,18,fadeColors[0]).draw()

            text4 = Text(x,290,"PLANNED TO DESTROY ITS AIR DEFENSIVE SO",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text5
        while x <= 40:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(20,175,"AFTER THE DEFEAT OF BIOTEX IN MOBIUS THEY",guardians,18,fadeColors[0]).draw()
            text2 = Text(20,210,"ARE FORCED TO PULL BACK TO ANOTHER PLANET",guardians,18,fadeColors[0]).draw()
            text3 = Text(30,245,"CALLED SECCO. A NEW COUNTEROFFENSIVE IS",guardians,18,fadeColors[0]).draw()
            text4 = Text(30,290,"PLANNED TO DESTROY ITS AIR DEFENSIVE SO",guardians,18,fadeColors[0]).draw()

            text5 = Text(x,335,"THAT THE GROUND TROOPS CAN LAND ON IT.",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text6
        while x <= 60:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(20,175,"AFTER THE DEFEAT OF BIOTEX IN MOBIUS THEY",guardians,18,fadeColors[0]).draw()
            text2 = Text(30,210,"ARE FORCED TO PULL BACK TO ANOTHER PLANET",guardians,18,fadeColors[0]).draw()
            text3 = Text(30,245,"CALLED SECCO. A NEW COUNTEROFFENSIVE IS",guardians,18,fadeColors[0]).draw()
            text4 = Text(30,290,"PLANNED TO DESTROY ITS AIR DEFENSIVE SO",guardians,18,fadeColors[0]).draw()
            text5 = Text(40,335,"THAT THE GROUND TROOPS CAN LAND ON IT.",guardians,18,fadeColors[0]).draw()

            text6 = Text(x,370,"YOU ARE GOING TO PARTICIPATE IN IT.",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text7
        while x <= 60:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(20,175,"AFTER THE DEFEAT OF BIOTEX IN MOBIUS THEY",guardians,18,fadeColors[0]).draw()
            text2 = Text(20,210,"ARE FORCED TO PULL BACK TO ANOTHER PLANET",guardians,18,fadeColors[0]).draw()
            text3 = Text(30,245,"CALLED SECCO. A NEW COUNTEROFFENSIVE IS",guardians,18,fadeColors[0]).draw()
            text4 = Text(30,290,"PLANNED TO DESTROY ITS AIR DEFENSIVE SO",guardians,18,fadeColors[0]).draw()
            text5 = Text(40,335,"THAT THE GROUND TROOPS CAN LAND ON IT.",guardians,18,fadeColors[0]).draw()
            text6 = Text(60,370,"YOU ARE GOING TO PARTICIPATE IN IT.",guardians,18,fadeColors[0]).draw()

            text7 = Text(x,405,"NOW GET MOVING PRIVATE. GOOD LUCK.",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        while cutscene:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                      normalColor=black,
                                      text="BACK",
                                      font=guardians,
                                      fontSize=22,
                                      textx=355,
                                      texty=493,
                                      fontColor=white,
                                      clickSound=otherSounds[0],
                                      action=menu.planetSelect).draw()

            pygame.display.update()
            clock.tick(60)

    def episode2Cutscene():
        cutscene = True
        
        gameWindow.fill(white)

        bg = r.choice(menuImages)
        
        y = -75
        x = -75

        #Draw the title
        while y <= 25:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,y,"STORY",guardians,48,fadeColors[0]).draw()
            y += 2.5
            pygame.display.update()

        #Draw the button
        y = 900

        while y >= 480:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,y,button,width=150,height=56,
                                     normalColor=black).draw()
            y -= 12.5
            pygame.display.update()

        #Draw the text1
        while x <= 40:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()

            text1 = Text(x,175,"AFTER HEAVY BATTLES IN PLANET SECCO",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text2
        while x <= 40:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"AFTER HEAVY BATTLES IN PLANET SECCO",guardians,18,fadeColors[0]).draw()

            text2 = Text(x,210,"HUMANS STILL HAVENT CAPTURED IT. THE",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text3
        while x <= 40:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"AFTER HEAVY BATTLES IN PLANET SECCO",guardians,18,fadeColors[0]).draw()
            text2 = Text(40,210,"HUMANS STILL HAVENT CAPTURED IT. THE",guardians,18,fadeColors[0]).draw()

            text3 = Text(x,245,"ARMY HQ DECIDES TO LEAVE THE PLANET AND",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text4
        while x <= 30:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"AFTER HEAVY BATTLES IN PLANET SECCO",guardians,18,fadeColors[0]).draw()
            text2 = Text(40,210,"HUMANS STILL HAVENT CAPTURED IT. THE",guardians,18,fadeColors[0]).draw()
            text3 = Text(30,245,"ARMY HQ DECIDES TO LEAVE THE PLANET AND",guardians,18,fadeColors[0]).draw()

            text4 = Text(x,290,"FOCUS ON A MORE IMPORTANT TARGET PLANET",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text5
        while x <= 25:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"AFTER HEAVY BATTLES IN PLANET SECCO",guardians,18,fadeColors[0]).draw()
            text2 = Text(40,210,"HUMANS STILL HAVENT CAPTURED IT. THE",guardians,18,fadeColors[0]).draw()
            text3 = Text(30,245,"ARMY HQ DECIDES TO LEAVE THE PLANET AND",guardians,18,fadeColors[0]).draw()
            text4 = Text(30,290,"FOCUS ON A MORE IMPORTANT TARGET PLANET",guardians,18,fadeColors[0]).draw()

            text5 = Text(x,335,"BREEZY. IF IT WILL BE CAPTURED IT WILL OPEN",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text6
        while x <= 25:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"AFTER HEAVY BATTLES IN PLANET SECCO",guardians,18,fadeColors[0]).draw()
            text2 = Text(40,210,"HUMANS STILL HAVENT CAPTURED IT. THE",guardians,18,fadeColors[0]).draw()
            text3 = Text(30,245,"ARMY HQ DECIDES TO LEAVE THE PLANET AND",guardians,18,fadeColors[0]).draw()
            text4 = Text(30,290,"FOCUS ON A MORE IMPORTANT TARGET PLANET",guardians,18,fadeColors[0]).draw()
            text5 = Text(25,335,"BREEZY. IF IT WILL BE CAPTURED IT WILL OPEN",guardians,18,fadeColors[0]).draw()

            text6 = Text(x,370,"DOOR TO COMPLETELY PULL BACK BIOTEX FROM",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text7
        while x <= 25:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"AFTER HEAVY BATTLES IN PLANET SECCO",guardians,18,fadeColors[0]).draw()
            text2 = Text(40,210,"HUMANS STILL HAVENT CAPTURED IT. THE",guardians,18,fadeColors[0]).draw()
            text3 = Text(30,245,"ARMY HQ DECIDES TO LEAVE THE PLANET AND",guardians,18,fadeColors[0]).draw()
            text4 = Text(30,290,"FOCUS ON A MORE IMPORTANT TARGET PLANET",guardians,18,fadeColors[0]).draw()
            text5 = Text(25,335,"BREEZY. IF IT WILL BE CAPTURED IT WILL OPEN",guardians,18,fadeColors[0]).draw()
            text6 = Text(25,370,"DOOR TO COMPLETELY PULL BACK BIOTEX FROM",guardians,18,fadeColors[0]).draw()

            text7 = Text(x,405,"GALAXY. NOW GET MOVING PRIVATE. GOOD LUCK.",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        while cutscene:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                      normalColor=black,
                                      text="BACK",
                                      font=guardians,
                                      fontSize=22,
                                      textx=355,
                                      texty=493,
                                      fontColor=white,
                                      clickSound=otherSounds[0],
                                      action=menu.planetSelect).draw()

            pygame.display.update()
            clock.tick(60)

    def episode3Cutscene():
        cutscene = True
        
        gameWindow.fill(white)

        bg = r.choice(menuImages)
        
        y = -75
        x = -75

        #Draw the title
        while y <= 25:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,y,"STORY",guardians,48,fadeColors[0]).draw()
            y += 2.5
            pygame.display.update()

        #Draw the button
        y = 900

        while y >= 480:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,y,button,width=150,height=56,
                                     normalColor=black).draw()
            y -= 12.5
            pygame.display.update()

        #Draw the text1
        while x <= 40:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()

            text1 = Text(x,175,"PLANET BREEZE HAS BEEN CAPTURED AND",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text2
        while x <= 20:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"PLANET BREEZE HAS BEEN CAPTURED AND",guardians,18,fadeColors[0]).draw()

            text2 = Text(x,210,"THE HUMAN FORCES ARE NOW READY TO STRIKE",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text3
        while x <= 30:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"PLANET BREEZE HAS BEEN CAPTURED AND",guardians,18,fadeColors[0]).draw()
            text2 = Text(20,210,"THE HUMAN FORCES ARE NOW READY TO STRIKE",guardians,18,fadeColors[0]).draw()

            text3 = Text(x,245,"AT THE HOME PLANET OF BIOTEX. PLANET BLUTO",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text4
        while x <= 20:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"PLANET BREEZE HAS BEEN CAPTURED AND",guardians,18,fadeColors[0]).draw()
            text2 = Text(20,210,"THE HUMAN FORCES ARE NOW READY TO STRIKE",guardians,18,fadeColors[0]).draw()
            text3 = Text(30,245,"AT THE HOME PLANET OF BIOTEX. PLANET BLUTO",guardians,18,fadeColors[0]).draw()

            text4 = Text(x,290,"IS HOWEVER HEAVILY DEFENDED AND WILL BE THE",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text5
        while x <= 40:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"PLANET BREEZE HAS BEEN CAPTURED AND",guardians,18,fadeColors[0]).draw()
            text2 = Text(20,210,"THE HUMAN FORCES ARE NOW READY TO STRIKE",guardians,18,fadeColors[0]).draw()
            text3 = Text(30,245,"AT THE HOME PLANET OF BIOTEX. PLANET BLUTO",guardians,18,fadeColors[0]).draw()
            text4 = Text(30,290,"IS HOWEVER HEAVILY DEFENDED AND WILL BE THE",guardians,18,fadeColors[0]).draw()

            text5 = Text(x,335,"TOUGHEST MISSION EVER. IF THE OPERATION",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text6
        while x <= 40:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"PLANET BREEZE HAS BEEN CAPTURED AND",guardians,18,fadeColors[0]).draw()
            text2 = Text(20,210,"THE HUMAN FORCES ARE NOW READY TO STRIKE",guardians,18,fadeColors[0]).draw()
            text3 = Text(30,245,"AT THE HOME PLANET OF BIOTEX. PLANET BLUTO",guardians,18,fadeColors[0]).draw()
            text4 = Text(30,290,"IS HOWEVER HEAVILY DEFENDED AND WILL BE THE",guardians,18,fadeColors[0]).draw()
            text5 = Text(40,335,"TOUGHEST MISSION EVER. IF THE OPERATION",guardians,18,fadeColors[0]).draw()

            text6 = Text(x,370,"SUCCESSES WE WILL BE ABLE TO PUSH BIOTEX",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text7
        while x <= 20:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"PLANET BREEZE HAS BEEN CAPTURED AND",guardians,18,fadeColors[0]).draw()
            text2 = Text(20,210,"THE HUMAN FORCES ARE NOW READY TO STRIKE",guardians,18,fadeColors[0]).draw()
            text3 = Text(30,245,"AT THE HOME PLANET OF BIOTEX. PLANET BLUTO",guardians,18,fadeColors[0]).draw()
            text4 = Text(30,290,"IS HOWEVER HEAVILY DEFENDED AND WILL BE THE",guardians,18,fadeColors[0]).draw()
            text5 = Text(25,335,"TOUGHEST MISSION EVER. IF THE OPERATION",guardians,18,fadeColors[0]).draw()
            text6 = Text(40,370,"SUCCESSES WE WILL BE ABLE TO PUSH BIOTEX",guardians,18,fadeColors[0]).draw()

            text7 = Text(x,405,"FROM OUR GALAXY ONCE AND FOR ALL. GOOD LUCK.",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        while cutscene:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                      normalColor=black,
                                      text="BACK",
                                      font=guardians,
                                      fontSize=22,
                                      textx=355,
                                      texty=493,
                                      fontColor=white,
                                      clickSound=otherSounds[0],
                                      action=menu.planetSelect).draw()

            pygame.display.update()
            clock.tick(60)

    def endCutscene():
        cutscene = True
        
        gameWindow.fill(white)

        bg = r.choice(menuImages)
        
        y = -75
        x = -75

        pygame.mixer.music.stop()
        theme = Music(winTheme,0,-1).play()

        #Draw the title
        while y <= 25:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,y,"STORY",guardians,48,fadeColors[0]).draw()
            y += 2.5
            pygame.display.update()

        #Draw the button
        y = 900

        while y >= 480:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,y,button,width=150,height=56,
                                     normalColor=black).draw()
            y -= 12.5
            pygame.display.update()

        #Draw the text1
        while x <= 40:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()

            text1 = Text(x,175,"PLANET BLUTO HAS BEEN CAPTURED AND",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text2
        while x <= 20:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"PLANET BLUTO HAS BEEN CAPTURED AND",guardians,18,fadeColors[0]).draw()

            text2 = Text(x,210,"THE BIOTEX IS FORCED TO SURRENDER. THE",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text3
        while x <= 30:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"PLANET BLUTO HAS BEEN CAPTURED AND",guardians,18,fadeColors[0]).draw()
            text2 = Text(20,210,"THE BIOTEX IS FORCED TO SURRENDER. THE",guardians,18,fadeColors[0]).draw()

            text3 = Text(x,245,"HUMANS CELEBRATE THE VICTORY EVERYWHERE",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text4
        while x <= 20:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"PLANET BLUTO HAS BEEN CAPTURED AND",guardians,18,fadeColors[0]).draw()
            text2 = Text(20,210,"THE BIOTEX IS FORCED TO SURRENDER. THE",guardians,18,fadeColors[0]).draw()
            text3 = Text(30,245,"HUMANS CELEBRATE THE VICTORY EVERYWHERE",guardians,18,fadeColors[0]).draw()

            text4 = Text(x,290,"AND YOU CAN FINALLY GO BACK TO YOUR FAMILY",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text5
        while x <= 20:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"PLANET BLUTO HAS BEEN CAPTURED AND",guardians,18,fadeColors[0]).draw()
            text2 = Text(20,210,"THE BIOTEX IS FORCED TO SURRENDER. THE",guardians,18,fadeColors[0]).draw()
            text3 = Text(30,245,"HUMANS CELEBRATE THE VICTORY EVERYWHERE",guardians,18,fadeColors[0]).draw()
            text4 = Text(30,290,"AND YOU CAN FINALLY GO BACK TO YOUR FAMILY",guardians,18,fadeColors[0]).draw()

            text5 = Text(x,335,"WITH YOUR NEWLY AWARDED MEDAL OF HONOR FOR",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text6
        while x <= 20:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"PLANET BLUTO HAS BEEN CAPTURED AND",guardians,18,fadeColors[0]).draw()
            text2 = Text(20,210,"THE BIOTEX IS FORCED TO SURRENDER. THE",guardians,18,fadeColors[0]).draw()
            text3 = Text(30,245,"HUMANS CELEBRATE THE VICTORY EVERYWHERE",guardians,18,fadeColors[0]).draw()
            text4 = Text(30,290,"AND YOU CAN FINALLY GO BACK TO YOUR FAMILY",guardians,18,fadeColors[0]).draw()
            text5 = Text(20,335,"WITH YOUR NEWLY AWARDED MEDAL OF HONOR FOR",guardians,18,fadeColors[0]).draw()

            text6 = Text(x,370,"YOUR CONTRIBUTIONS TO THE WINNING OF THIS WAR",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        x = -300

        #Draw the text7
        while x <= 20:
            gameWindow.fill(white)
            b = Image(0,0,bg).draw()
            title = Text(285,25,"STORY",guardians,48,fadeColors[0]).draw()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                     normalColor=black).draw()
            text1 = Text(40,175,"PLANET BLUTO HAS BEEN CAPTURED AND",guardians,18,fadeColors[0]).draw()
            text2 = Text(20,210,"THE BIOTEX IS FORCED TO SURRENDER. THE",guardians,18,fadeColors[0]).draw()
            text3 = Text(30,245,"HUMANS CELEBRATE THE VICTORY EVERYWHERE",guardians,18,fadeColors[0]).draw()
            text4 = Text(30,290,"AND YOU CAN FINALLY GO BACK TO YOUR FAMILY",guardians,18,fadeColors[0]).draw()
            text5 = Text(20,335,"WITH YOUR NEWLY AWARDED MEDAL OF HONOR FOR",guardians,18,fadeColors[0]).draw()
            text6 = Text(20,370,"YOUR CONTRIBUTIONS TO THE WINNING OF THIS WAR",guardians,18,fadeColors[0]).draw()

            text7 = Text(x,405,"CONGRATULATIONS PRIVATE. YOU HAVE DONE WELL.",guardians,18,fadeColors[0]).draw()
            x += 7.5
            pygame.display.update()

        buttonSound = Sound(menuSounds[1],0.05).play()

        while cutscene:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            backButton = ImageButton(325,480,button,width=150,height=56,
                                      normalColor=black,
                                      text="BACK",
                                      font=guardians,
                                      fontSize=22,
                                      textx=355,
                                      texty=493,
                                      fontColor=white,
                                      clickSound=otherSounds[0],
                                      action=menu.MainMenu).draw()

            pygame.display.update()
            clock.tick(60)
