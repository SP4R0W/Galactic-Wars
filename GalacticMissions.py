import pickle
from pygame_functions import *
import random as r

menuImages = ["Assets/Images/Backgrounds/space1.png",
                   "Assets/Images/Backgrounds/space2.png",
                   "Assets/Images/Backgrounds/space3.png"]

enemySprites = ["Assets/Images/Enemy/enemy1.png",
                "Assets/Images/Enemy/enemy2.png",
                "Assets/Images/Enemy/enemy3.png"]

gameThemes = ["Assets/Sounds/Game/Themes/1.wav",
              "Assets/Sounds/Game/Themes/2.wav",
              "Assets/Sounds/Game/Themes/3.wav",
              "Assets/Sounds/Game/Themes/4.wav",
              "Assets/Sounds/Game/Themes/5.wav",
              "Assets/Sounds/Game/Themes/6.wav",
              "Assets/Sounds/Game/Themes/7.wav",
              "Assets/Sounds/Game/Themes/8.wav"]

coordinates = [[100,700, #x start and end
                0,1, #x speed and y speed
                0, #y position
                180], #angle 

                [100,700, #x start and end
                                0,-1, #x speed and y speed
                                700, #y position
                                360], #angle 
               ]

sprites = []
bullets = []
enemies = []

global score
score = 0

global shot
shot = 0

global gameThings
gameThings = {}

class game:

    def loadGame():
        global gameThings

        loadFile = open("Assets\Data\saveData.pickle",'rb')
        gameThings = pickle.load(loadFile)
        print(gameThings)

    def P1L1():
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage([[bg],
                            [bg]])

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        x = 250
        y = 500
        xSpeed = 0

        maxSpeed = gameThings["MaxSpeed"]

        neededshot = r.randrange(30,45,5)

        bulletX = 40
        bulletY = 20
        bulletXS = 0
        bulletYS = -5

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Destroy "+str(neededshot)+" ships",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Destroy "+str(neededshot-shot)+" ships")
            
            scrollBackground(0,5)

            if keyPressed("a") or keyPressed("left"):
                bulletX = 40
                bulletY = 20
                bulletXS = 0
                bulletYS = -1.5

                xSpeed -=gameThings["Speed"]

            if keyPressed("d") or keyPressed("right"):

                xSpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()

            if xSpeed > maxSpeed:
                xSpeed = maxSpeed
            if xSpeed < -maxSpeed:
                xSpeed = -maxSpeed
          
            x += xSpeed

            if x > 700:
                x = 0
            if x < 0:
                x = 700

            if len(enemies) != 5:
                enemies.append(Enemy(r.choice(enemySprites),r.randint(100,700),0, 0, 1, 5,30))

            if shot >= neededshot:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P1L1")
                
            if gameThings["Health"] < 10:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Vertical

    def P1L2():
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage(bg)

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        x = 250
        y = 250
        xSpeed = 0
        ySpeed = 0

        time = 0
        neededtime = r.randrange(200,350,50)

        maxSpeed = gameThings["MaxSpeed"]

        bulletX = 40
        bulletY = 20
        bulletXS = 0
        bulletYS = -5

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Survive the attack",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Survive the attack: "+str(neededtime-int(time)))

            if keyPressed("w") or keyPressed("up"):
                bulletX = 40
                bulletY = 20
                bulletXS = 0
                bulletYS = -1

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,360,1)
                ySpeed -=gameThings["Speed"]

            if keyPressed("s") or keyPressed("down"):
                bulletX = 40
                bulletY = -90
                bulletXS = 0
                bulletYS = 1

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,180,1)
                ySpeed +=gameThings["Speed"]

            if keyPressed("a") or keyPressed("left"):
                bulletX = -10
                bulletY = -40
                bulletXS = -1
                bulletYS = 0

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,-90,1)
                xSpeed -=gameThings["Speed"]

            if keyPressed("d") or keyPressed("right"):
                bulletX = 90
                bulletY = -40
                bulletXS = 1
                bulletYS = 0

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,90,1)
                xSpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()

            if xSpeed > maxSpeed:
                xSpeed = maxSpeed
            if xSpeed < -maxSpeed:
                xSpeed = -maxSpeed
            
            if ySpeed > maxSpeed:
                ySpeed = maxSpeed
            if ySpeed < -maxSpeed:
                ySpeed = -maxSpeed

            x += xSpeed
            y += ySpeed
            time += 0.1
            print(time)

            if time >= neededtime:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P1L2")

            if x > 700:
                x = 0
            if x < 0:
                x = 700
            if y > 500:
                y = 0
            if y < 0:
                y = 500

            if len(enemies) != 5:
                cor = r.choice(coordinates)

                enemies.append(Enemy(r.choice(enemySprites),r.randint(cor[0],cor[1]),cor[4], 0*cor[2], 1*cor[3], 5,30,cor[5]))

            if gameThings["Health"] < 10:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Defense

    def P1L3():
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage([[bg,bg]])

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        bg = makeSprite(r.choice(menuImages))

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        x = 0
        y = 250
        xSpeed = 0
        ySpeed = 0

        maxSpeed = gameThings["MaxSpeed"]

        neededshot = r.randrange(40,65,5)

        bulletX = 90
        bulletY = -40
        bulletXS = 1
        bulletYS = 0

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)
        transformSprite(spaceSprite,90,1)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Destroy "+str(neededshot)+" ships",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Destroy "+str(neededshot-shot)+" ships")

            scrollBackground(-5,0)

            if keyPressed("w") or keyPressed("up"):

                ySpeed -=gameThings["Speed"]

            if keyPressed("s") or keyPressed("down"):

                ySpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()
            
            if ySpeed > maxSpeed:
                ySpeed = maxSpeed
            if ySpeed < -maxSpeed:
                ySpeed = -maxSpeed

            y += ySpeed

            if y > 500:
                y = 0
            if y < 0:
                y = 500

            if len(enemies) != 5:
                enemies.append(Enemy(r.choice(enemySprites),800,r.randint(100,500), -2, 0, 5,30,-90))

            if shot >= neededshot:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P1L3")

            if gameThings["Health"] < 10:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Horizontal

    def P1L4():
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage([[bg],
                            [bg]])

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        x = 250
        y = 500
        xSpeed = 0

        maxSpeed = gameThings["MaxSpeed"]

        neededshot = r.randrange(65,100,5)

        bulletX = 40
        bulletY = 20
        bulletXS = 0
        bulletYS = -5

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Survive the counterattack",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Survive the counterattack: "+str(neededshot-shot))
            
            scrollBackground(0,5)

            if keyPressed("a") or keyPressed("left"):
                bulletX = 40
                bulletY = 20
                bulletXS = 0
                bulletYS = -1.5

                xSpeed -=gameThings["Speed"]

            if keyPressed("d") or keyPressed("right"):

                xSpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()

            if xSpeed > maxSpeed:
                xSpeed = maxSpeed
            if xSpeed < -maxSpeed:
                xSpeed = -maxSpeed
          
            x += xSpeed

            if x > 700:
                x = 0
            if x < 0:
                x = 700

            if len(enemies) != 5:
                enemies.append(Enemy(r.choice(enemySprites),r.randint(100,700),0, 0, 1, 5,30))

            if shot >= neededshot:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P1L4")


            if gameThings["Health"] < 10:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Vertical

    def P2L1():
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage(bg)

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        x = 250
        y = 250
        xSpeed = 0
        ySpeed = 0

        time = 0

        neededshot = r.randrange(50,75,5)

        maxSpeed = gameThings["MaxSpeed"]

        bulletX = 40
        bulletY = 20
        bulletXS = 0
        bulletYS = -5

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Destroy "+str(neededshot)+" enemies",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Destroy "+str(neededshot-shot)+" enemies")

            if keyPressed("w") or keyPressed("up"):
                bulletX = 40
                bulletY = 20
                bulletXS = 0
                bulletYS = -1

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,360,1)
                ySpeed -=gameThings["Speed"]

            if keyPressed("s") or keyPressed("down"):
                bulletX = 40
                bulletY = -90
                bulletXS = 0
                bulletYS = 1

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,180,1)
                ySpeed +=gameThings["Speed"]

            if keyPressed("a") or keyPressed("left"):
                bulletX = -10
                bulletY = -40
                bulletXS = -1
                bulletYS = 0

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,-90,1)
                xSpeed -=gameThings["Speed"]

            if keyPressed("d") or keyPressed("right"):
                bulletX = 90
                bulletY = -40
                bulletXS = 1
                bulletYS = 0

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,90,1)
                xSpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()

            if xSpeed > maxSpeed:
                xSpeed = maxSpeed
            if xSpeed < -maxSpeed:
                xSpeed = -maxSpeed
            
            if ySpeed > maxSpeed:
                ySpeed = maxSpeed
            if ySpeed < -maxSpeed:
                ySpeed = -maxSpeed

            x += xSpeed
            y += ySpeed

            if shot >= neededshot:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P2L1")

            if x > 700:
                x = 0
            if x < 0:
                x = 700
            if y > 500:
                y = 0
            if y < 0:
                y = 500

            if len(enemies) != 6:
                cor = r.choice(coordinates)

                enemies.append(Enemy(r.choice(enemySprites),r.randint(cor[0],cor[1]),cor[4], 0*cor[2], 1.25*cor[3], 5,50,cor[5]))

            if gameThings["Health"] < 10:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Defense

    def P2L2():
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage([[bg,bg]])

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        bg = makeSprite(r.choice(menuImages))

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        time = 0
        neededtime = r.randrange(400,500,10)
        print(neededtime)
        x = 0
        y = 250
        xSpeed = 0
        ySpeed = 0

        maxSpeed = gameThings["MaxSpeed"]

        bulletX = 90
        bulletY = -40
        bulletXS = 1
        bulletYS = 0

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)
        transformSprite(spaceSprite,90,1)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Reach the base",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Reach the base: "+str(neededtime-int(time)))

            scrollBackground(-5,0)

            if keyPressed("w") or keyPressed("up"):

                ySpeed -=gameThings["Speed"]

            if keyPressed("s") or keyPressed("down"):

                ySpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()
            
            if ySpeed > maxSpeed:
                ySpeed = maxSpeed
            if ySpeed < -maxSpeed:
                ySpeed = -maxSpeed

            y += ySpeed
            time += 0.1

            if y > 500:
                y = 0
            if y < 0:
                y = 500

            if len(enemies) != 6:
                enemies.append(Enemy(r.choice(enemySprites),800,r.randint(100,500), -2.25, 0, 5,50,-90))

            if time >= neededtime:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P2L2")

            if gameThings["Health"] < 10:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Horizontal

    def P2L3():
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage(bg)

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        x = 250
        y = 250
        xSpeed = 0
        ySpeed = 0

        time = 0
        neededtime = r.randrange(400,600,50)

        maxSpeed = gameThings["MaxSpeed"]

        bulletX = 40
        bulletY = 20
        bulletXS = 0
        bulletYS = -5

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Survive until reinforcements arrive",18,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Survive until reinforcements arrive "+str(neededtime-int(time)))

            if keyPressed("w") or keyPressed("up"):
                bulletX = 40
                bulletY = 20
                bulletXS = 0
                bulletYS = -1

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,360,1)
                ySpeed -=gameThings["Speed"]

            if keyPressed("s") or keyPressed("down"):
                bulletX = 40
                bulletY = -90
                bulletXS = 0
                bulletYS = 1

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,180,1)
                ySpeed +=gameThings["Speed"]

            if keyPressed("a") or keyPressed("left"):
                bulletX = -10
                bulletY = -40
                bulletXS = -1
                bulletYS = 0

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,-90,1)
                xSpeed -=gameThings["Speed"]

            if keyPressed("d") or keyPressed("right"):
                bulletX = 90
                bulletY = -40
                bulletXS = 1
                bulletYS = 0

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,90,1)
                xSpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()

            if xSpeed > maxSpeed:
                xSpeed = maxSpeed
            if xSpeed < -maxSpeed:
                xSpeed = -maxSpeed
            
            if ySpeed > maxSpeed:
                ySpeed = maxSpeed
            if ySpeed < -maxSpeed:
                ySpeed = -maxSpeed

            x += xSpeed
            y += ySpeed
            time += 0.1
            print(time)

            if time >= neededtime:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P2L3")


            if x > 700:
                x = 0
            if x < 0:
                x = 700
            if y > 500:
                y = 0
            if y < 0:
                y = 500

            if len(enemies) != 6:
                cor = r.choice(coordinates)

                enemies.append(Enemy(r.choice(enemySprites),r.randint(cor[0],cor[1]),cor[4], 0*cor[2], 1.25*cor[3], 5,50,cor[5]))

            if gameThings["Health"] < 10:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Defense

    def P2L4():
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage([[bg,bg]])

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        bg = makeSprite(r.choice(menuImages))

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        time = 0
        neededtime = r.randrange(400,500,10)
        print(neededtime)
        x = 0
        y = 250
        xSpeed = 0
        ySpeed = 0

        maxSpeed = gameThings["MaxSpeed"]

        bulletX = 90
        bulletY = -40
        bulletXS = 1
        bulletYS = 0

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)
        transformSprite(spaceSprite,90,1)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Escape from base",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Escape from base: "+str(neededtime-int(time)))

            scrollBackground(-5,0)

            if keyPressed("w") or keyPressed("up"):

                ySpeed -=gameThings["Speed"]

            if keyPressed("s") or keyPressed("down"):

                ySpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()
            
            if ySpeed > maxSpeed:
                ySpeed = maxSpeed
            if ySpeed < -maxSpeed:
                ySpeed = -maxSpeed

            y += ySpeed
            time += 0.1

            if y > 500:
                y = 0
            if y < 0:
                y = 500

            if len(enemies) != 6:
                enemies.append(Enemy(r.choice(enemySprites),800,r.randint(100,500), -2.25, 0, 5,50,-90))

            if time >= neededtime:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P2L4")

            if gameThings["Health"] < 10:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Horizontal

    def P2L5():
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage(bg)

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        x = 250
        y = 250
        xSpeed = 0
        ySpeed = 0

        time = 0

        neededshot = r.randrange(65,100,5)

        maxSpeed = gameThings["MaxSpeed"]

        bulletX = 40
        bulletY = 20
        bulletXS = 0
        bulletYS = -5

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Repeal an invasion",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Repeal an invasion: "+str(neededshot-shot))

            if keyPressed("w") or keyPressed("up"):
                bulletX = 40
                bulletY = 20
                bulletXS = 0
                bulletYS = -1

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,360,1)
                ySpeed -=gameThings["Speed"]

            if keyPressed("s") or keyPressed("down"):
                bulletX = 40
                bulletY = -90
                bulletXS = 0
                bulletYS = 1

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,180,1)
                ySpeed +=gameThings["Speed"]

            if keyPressed("a") or keyPressed("left"):
                bulletX = -10
                bulletY = -40
                bulletXS = -1
                bulletYS = 0

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,-90,1)
                xSpeed -=gameThings["Speed"]

            if keyPressed("d") or keyPressed("right"):
                bulletX = 90
                bulletY = -40
                bulletXS = 1
                bulletYS = 0

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,90,1)
                xSpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()

            if xSpeed > maxSpeed:
                xSpeed = maxSpeed
            if xSpeed < -maxSpeed:
                xSpeed = -maxSpeed
            
            if ySpeed > maxSpeed:
                ySpeed = maxSpeed
            if ySpeed < -maxSpeed:
                ySpeed = -maxSpeed

            x += xSpeed
            y += ySpeed

            if shot >= neededshot:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P2L5")

            if x > 700:
                x = 0
            if x < 0:
                x = 700
            if y > 500:
                y = 0
            if y < 0:
                y = 500

            if len(enemies) != 6:
                cor = r.choice(coordinates)

                enemies.append(Enemy(r.choice(enemySprites),r.randint(cor[0],cor[1]),cor[4], 0*cor[2], 1.25*cor[3], 5,50,cor[5]))

            if gameThings["Health"] < 10:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Defense

    def P2L6():
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage([[bg],
                            [bg]])

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        x = 250
        y = 500
        xSpeed = 0
        time = 0

        maxSpeed = gameThings["MaxSpeed"]

        bulletX = 40
        bulletY = 20
        bulletXS = 0
        bulletYS = -5

        neededtime = r.randrange(500,750,25)

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Leave the planet",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Leave the planet: "+str(neededtime-int(time)))
            
            scrollBackground(0,5)

            if keyPressed("a") or keyPressed("left"):
                bulletX = 40
                bulletY = 20
                bulletXS = 0
                bulletYS = -1.5

                xSpeed -=gameThings["Speed"]

            if keyPressed("d") or keyPressed("right"):

                xSpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()

            if xSpeed > maxSpeed:
                xSpeed = maxSpeed
            if xSpeed < -maxSpeed:
                xSpeed = -maxSpeed
          
            x += xSpeed
            time += 0.1
            print(time)

            if x > 700:
                x = 0
            if x < 0:
                x = 700

            if len(enemies) != 6:
                enemies.append(Enemy(r.choice(enemySprites),r.randint(100,700),0, 0, 1.25, 5,50))

            if time >= neededtime:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P2L6")
                
            if gameThings["Health"] < 10:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Vertical

    def P3L1(): #Horizontal
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage([[bg,bg]])

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        bg = makeSprite(r.choice(menuImages))

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        time = 0
        neededtime = r.randrange(500,750,25)
        print(neededtime)
        x = 0
        y = 250
        xSpeed = 0
        ySpeed = 0

        maxSpeed = gameThings["MaxSpeed"]

        bulletX = 90
        bulletY = -40
        bulletXS = 1
        bulletYS = 0

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)
        transformSprite(spaceSprite,90,1)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Reach the planet",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Reach the planet: "+str(neededtime-int(time)))

            scrollBackground(-5,0)

            if keyPressed("w") or keyPressed("up"):

                ySpeed -=gameThings["Speed"]

            if keyPressed("s") or keyPressed("down"):

                ySpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()
            
            if ySpeed > maxSpeed:
                ySpeed = maxSpeed
            if ySpeed < -maxSpeed:
                ySpeed = -maxSpeed

            y += ySpeed
            time += 0.1

            if y > 500:
                y = 0
            if y < 0:
                y = 500

            if len(enemies) != 7:
                enemies.append(Enemy(r.choice(enemySprites),800,r.randint(100,500), -2.5, 0, 5,75,-90))

            if time >= neededtime:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P3L1")


            if gameThings["Health"] < 10:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Horizontal

    def P3L2(): #Vertical
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage([[bg],
                            [bg]])

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        x = 250
        y = 500
        xSpeed = 0
        time = 0

        maxSpeed = gameThings["MaxSpeed"]

        bulletX = 40
        bulletY = 20
        bulletXS = 0
        bulletYS = -5

        neededshot = r.randrange(75,105,5)

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Destroy "+str(neededshot)+" ships",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:
            
            changeLabel(obj,"Destroy "+str(neededshot-shot)+" ships")

            scrollBackground(0,5)

            if keyPressed("a") or keyPressed("left"):
                bulletX = 40
                bulletY = 20
                bulletXS = 0
                bulletYS = -1.5

                xSpeed -=gameThings["Speed"]

            if keyPressed("d") or keyPressed("right"):

                xSpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()

            if xSpeed > maxSpeed:
                xSpeed = maxSpeed
            if xSpeed < -maxSpeed:
                xSpeed = -maxSpeed
          
            x += xSpeed

            print(shot)

            if x > 700:
                x = 0
            if x < 0:
                x = 700

            if len(enemies) != 6:
                enemies.append(Enemy(r.choice(enemySprites),r.randint(100,700),0, 0, 1.50, 5,75))

            if shot >= neededshot:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P3L2")
                
            if gameThings["Health"] < 10:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Vertical

    def P3L3(): #Defense
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage(bg)

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        x = 250
        y = 250
        xSpeed = 0
        ySpeed = 0

        time = 0

        neededtime = r.randrange(300,500,50)

        maxSpeed = gameThings["MaxSpeed"]

        bulletX = 40
        bulletY = 20
        bulletXS = 0
        bulletYS = -5

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Survive the attack",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Survive the attack: "+str(neededtime-int(time)))

            if keyPressed("w") or keyPressed("up"):
                bulletX = 40
                bulletY = 20
                bulletXS = 0
                bulletYS = -1

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,360,1)
                ySpeed -=gameThings["Speed"]

            if keyPressed("s") or keyPressed("down"):
                bulletX = 40
                bulletY = -90
                bulletXS = 0
                bulletYS = 1

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,180,1)
                ySpeed +=gameThings["Speed"]

            if keyPressed("a") or keyPressed("left"):
                bulletX = -10
                bulletY = -40
                bulletXS = -1
                bulletYS = 0

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,-90,1)
                xSpeed -=gameThings["Speed"]

            if keyPressed("d") or keyPressed("right"):
                bulletX = 90
                bulletY = -40
                bulletXS = 1
                bulletYS = 0

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,90,1)
                xSpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()

            if xSpeed > maxSpeed:
                xSpeed = maxSpeed
            if xSpeed < -maxSpeed:
                xSpeed = -maxSpeed
            
            if ySpeed > maxSpeed:
                ySpeed = maxSpeed
            if ySpeed < -maxSpeed:
                ySpeed = -maxSpeed

            x += xSpeed
            y += ySpeed
            time += 0.1

            if time >= neededtime:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(s,s,"P3L3")

            if x > 700:
                x = 0
            if x < 0:
                x = 700
            if y > 500:
                y = 0
            if y < 0:
                y = 500

            if len(enemies) != 7:
                cor = r.choice(coordinates)

                enemies.append(Enemy(r.choice(enemySprites),r.randint(cor[0],cor[1]),cor[4], 0*cor[2], 1.5*cor[3], 5,75,cor[5]))

            if gameThings["Health"] < 10:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Defense

    def P3L4(): #Vertical
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage([[bg],
                            [bg]])

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        x = 250
        y = 500
        xSpeed = 0
        time = 0

        maxSpeed = gameThings["MaxSpeed"]

        bulletX = 40
        bulletY = 20
        bulletXS = 0
        bulletYS = -5

        neededtime = r.randrange(500,700,50)
        print(neededtime)

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Reach the base",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Reach the base: "+str(neededtime-int(time)))
            
            scrollBackground(0,5)

            if keyPressed("a") or keyPressed("left"):
                bulletX = 40
                bulletY = 20
                bulletXS = 0
                bulletYS = -1.5

                xSpeed -=gameThings["Speed"]

            if keyPressed("d") or keyPressed("right"):

                xSpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()

            if xSpeed > maxSpeed:
                xSpeed = maxSpeed
            if xSpeed < -maxSpeed:
                xSpeed = -maxSpeed

            time += 0.1
          
            x += xSpeed
            print(time)

            if x > 700:
                x = 0
            if x < 0:
                x = 700

            if len(enemies) != 6:
                enemies.append(Enemy(r.choice(enemySprites),r.randint(100,700),0, 0, 1.50, 5,75))

            if time >= neededtime:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P3L4")
                
            if gameThings["Health"] < 10:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Vertical

    def P3L5(): #Defense
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage(bg)

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        x = 250
        y = 250
        xSpeed = 0
        ySpeed = 0

        time = 0

        neededshot = r.randrange(70,120,10)

        maxSpeed = gameThings["MaxSpeed"]

        bulletX = 40
        bulletY = 20
        bulletXS = 0
        bulletYS = -5

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Destroy all forces",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Destroy all forces: "+str(neededshot-shot))

            if keyPressed("w") or keyPressed("up"):
                bulletX = 40
                bulletY = 20
                bulletXS = 0
                bulletYS = -1

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,360,1)
                ySpeed -=gameThings["Speed"]

            if keyPressed("s") or keyPressed("down"):
                bulletX = 40
                bulletY = -90
                bulletXS = 0
                bulletYS = 1

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,180,1)
                ySpeed +=gameThings["Speed"]

            if keyPressed("a") or keyPressed("left"):
                bulletX = -10
                bulletY = -40
                bulletXS = -1
                bulletYS = 0

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,-90,1)
                xSpeed -=gameThings["Speed"]

            if keyPressed("d") or keyPressed("right"):
                bulletX = 90
                bulletY = -40
                bulletXS = 1
                bulletYS = 0

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,90,1)
                xSpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()

            if xSpeed > maxSpeed:
                xSpeed = maxSpeed
            if xSpeed < -maxSpeed:
                xSpeed = -maxSpeed
            
            if ySpeed > maxSpeed:
                ySpeed = maxSpeed
            if ySpeed < -maxSpeed:
                ySpeed = -maxSpeed

            x += xSpeed
            y += ySpeed

            if shot >= neededshot:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P3L5")

            if x > 700:
                x = 0
            if x < 0:
                x = 700
            if y > 500:
                y = 0
            if y < 0:
                y = 500

            if len(enemies) != 7:
                cor = r.choice(coordinates)

                enemies.append(Enemy(r.choice(enemySprites),r.randint(cor[0],cor[1]),cor[4], 0*cor[2], 1.5*cor[3], 5,75,cor[5]))

            if gameThings["Health"] < 10:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Defense

    def P4L1():
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage([[bg,bg]])

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        bg = makeSprite(r.choice(menuImages))

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        time = 0
        neededshot = r.randrange(50,100,5)

        x = 0
        y = 250
        xSpeed = 0
        ySpeed = 0

        maxSpeed = gameThings["MaxSpeed"]

        bulletX = 90
        bulletY = -40
        bulletXS = 1
        bulletYS = 0

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)
        transformSprite(spaceSprite,90,1)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Destroy "+str(neededshot)+" ships",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Destroy "+str(neededshot-shot)+" ships")

            scrollBackground(-5,0)

            if keyPressed("w") or keyPressed("up"):

                ySpeed -=gameThings["Speed"]

            if keyPressed("s") or keyPressed("down"):

                ySpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()
            
            if ySpeed > maxSpeed:
                ySpeed = maxSpeed
            if ySpeed < -maxSpeed:
                ySpeed = -maxSpeed

            y += ySpeed
            time += 0.1

            if y > 500:
                y = 0
            if y < 0:
                y = 500

            if len(enemies) != 8:
                enemies.append(Enemy(r.choice(enemySprites),800,r.randint(100,500), -3, 0, 10,125,-90))

            if shot >= neededshot:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P4L1")

            if gameThings["Health"] < 20:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Horizontal

    def P4L2(): #Vertical
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage([[bg],
                            [bg]])

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        x = 250
        y = 500
        xSpeed = 0
        time = 0

        maxSpeed = gameThings["MaxSpeed"]

        bulletX = 40
        bulletY = 20
        bulletXS = 0
        bulletYS = -5

        neededtime = r.randrange(500,850,50)
        print(neededtime)

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Reach the forces",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Reach the attack forces: "+str(neededtime-int(time)))
            
            scrollBackground(0,5)

            if keyPressed("a") or keyPressed("left"):
                bulletX = 40
                bulletY = 20
                bulletXS = 0
                bulletYS = -1.5

                xSpeed -=gameThings["Speed"]

            if keyPressed("d") or keyPressed("right"):

                xSpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()

            if xSpeed > maxSpeed:
                xSpeed = maxSpeed
            if xSpeed < -maxSpeed:
                xSpeed = -maxSpeed

            time += 0.1
          
            x += xSpeed
            print(time)

            if x > 700:
                x = 0
            if x < 0:
                x = 700

            if len(enemies) != 8:
                enemies.append(Enemy(r.choice(enemySprites),r.randint(100,700),0, 0, 2, 10,125))

            if time >= neededtime:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P4L2")

                
            if gameThings["Health"] < 20:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Vertical

    def P4L3(): #Defense
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage(bg)

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        x = 250
        y = 250
        xSpeed = 0
        ySpeed = 0

        time = 0

        neededshot = r.randrange(75,125,5)

        maxSpeed = gameThings["MaxSpeed"]

        bulletX = 40
        bulletY = 20
        bulletXS = 0
        bulletYS = -5

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Repeal an attack",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Repeal an attack: "+str(neededshot-shot))

            if keyPressed("w") or keyPressed("up"):
                bulletX = 40
                bulletY = 20
                bulletXS = 0
                bulletYS = -1

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,360,1)
                ySpeed -=gameThings["Speed"]

            if keyPressed("s") or keyPressed("down"):
                bulletX = 40
                bulletY = -90
                bulletXS = 0
                bulletYS = 1

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,180,1)
                ySpeed +=gameThings["Speed"]

            if keyPressed("a") or keyPressed("left"):
                bulletX = -10
                bulletY = -40
                bulletXS = -1
                bulletYS = 0

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,-90,1)
                xSpeed -=gameThings["Speed"]

            if keyPressed("d") or keyPressed("right"):
                bulletX = 90
                bulletY = -40
                bulletXS = 1
                bulletYS = 0

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,90,1)
                xSpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()

            if xSpeed > maxSpeed:
                xSpeed = maxSpeed
            if xSpeed < -maxSpeed:
                xSpeed = -maxSpeed
            
            if ySpeed > maxSpeed:
                ySpeed = maxSpeed
            if ySpeed < -maxSpeed:
                ySpeed = -maxSpeed

            x += xSpeed
            y += ySpeed

            if shot >= neededshot:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(score,shot,"P4L3")

            if x > 700:
                x = 0
            if x < 0:
                x = 700
            if y > 500:
                y = 0
            if y < 0:
                y = 500

            if len(enemies) != 8:
                cor = r.choice(coordinates)

                enemies.append(Enemy(r.choice(enemySprites),r.randint(cor[0],cor[1]),cor[4], 0*cor[2], 2*cor[3], 10,125,cor[5]))

            if gameThings["Health"] < 20:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Defense

    def P4L4(): #Horizontal
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage([[bg],
                            [bg]])

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        x = 250
        y = 500
        xSpeed = 0
        time = 0

        maxSpeed = gameThings["MaxSpeed"]

        bulletX = 40
        bulletY = 20
        bulletXS = 0
        bulletYS = -5

        neededtime = r.randrange(750,1000,50)
        print(neededtime)

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Reach the base",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Reach the base: "+str(neededtime-int(time)))
            
            scrollBackground(0,5)

            if keyPressed("a") or keyPressed("left"):
                bulletX = 40
                bulletY = 20
                bulletXS = 0
                bulletYS = -1.5

                xSpeed -=gameThings["Speed"]

            if keyPressed("d") or keyPressed("right"):

                xSpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()

            if xSpeed > maxSpeed:
                xSpeed = maxSpeed
            if xSpeed < -maxSpeed:
                xSpeed = -maxSpeed

            time += 0.1
          
            x += xSpeed
            print(time)

            if x > 700:
                x = 0
            if x < 0:
                x = 700

            if len(enemies) != 8:
                enemies.append(Enemy(r.choice(enemySprites),r.randint(100,700),0, 0, 2, 10,125))

            if time >= neededtime:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P4L4")

                
            if gameThings["Health"] < 20:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Horizontal

    def P4L5(): #Defense
        global spaceSprite
        global sprite
        global bulletRun
        global health
        global score
        global scoret
        global obj
        bulletRun = False

        screenSize(800,600)
        setBackgroundColour("white")
        bg = r.choice(menuImages)
        setBackgroundImage(bg)

        setAutoUpdate(False)

        pygame.display.set_caption("Galactic Wars")
        icon = pygame.image.load("Assets/Images/icon.png")
        pygame.display.set_icon(icon)

        game.loadGame()

        spaceSprite = makeSprite("Assets/Images/Ship/gameSprite.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/gameSprite2.png")
        addSpriteImage(spaceSprite,"Assets/Images/Ship/explosion.png")

        sprite = makeSprite("Assets/Images/Ship/bullet.png")

        play = True

        x = 250
        y = 250
        xSpeed = 0
        ySpeed = 0

        time = 0

        neededshot = r.randrange(100,150,5)

        maxSpeed = gameThings["MaxSpeed"]

        bulletX = 40
        bulletY = 20
        bulletXS = 0
        bulletYS = -5

        showSprite(spaceSprite)
        moveSprite(spaceSprite,x,y)

        health = newLabel("HEALTH: "+str(gameThings["Health"]),32,"Forte","red",0,0,'clear')
        showLabel(health)

        scoret = newLabel("SCORE: "+str(score),32,"Forte","gray",0,35,'clear')
        showLabel(scoret)

        obj = newLabel("Destroy all forces",32,"Forte","white",0,70,'clear')
        showLabel(obj)

        contrl1 = newLabel("Use arrows or WASD to move the ship",18,"Forte","white",0,105,'clear')
        showLabel(contrl1)

        contrl2 = newLabel("Press 'space' to shoot",18,"Forte","white",0,125,'clear')
        showLabel(contrl2)

        contrl3 = newLabel("Press '1' key to go to main menu",18,"Forte","white",0,145,'clear')
        showLabel(contrl3)

        g = makeMusic(r.choice(gameThemes))
        playMusic(-1)

        while play:

            changeLabel(obj,"Destroy all forces: "+str(neededshot-shot))

            if keyPressed("w") or keyPressed("up"):
                bulletX = 40
                bulletY = 20
                bulletXS = 0
                bulletYS = -1

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,360,1)
                ySpeed -=gameThings["Speed"]

            if keyPressed("s") or keyPressed("down"):
                bulletX = 40
                bulletY = -90
                bulletXS = 0
                bulletYS = 1

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,180,1)
                ySpeed +=gameThings["Speed"]

            if keyPressed("a") or keyPressed("left"):
                bulletX = -10
                bulletY = -40
                bulletXS = -1
                bulletYS = 0

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,-90,1)
                xSpeed -=gameThings["Speed"]

            if keyPressed("d") or keyPressed("right"):
                bulletX = 90
                bulletY = -40
                bulletXS = 1
                bulletYS = 0

                changeSpriteImage(spaceSprite,1)
                transformSprite(spaceSprite,90,1)
                xSpeed +=gameThings["Speed"]

            if bulletRun == False:
                if keyPressed("space"):
                    bulletRun = True
                    shoot = makeSound("Assets/Sounds/Game/Effects/shoot.wav")
                    playSound(shoot)
                    bullets.append(Projectile(x + bulletX, y - bulletY, bulletXS * 10, bulletYS * 10, gameThings["Damage"]))

            if keyPressed("1"):
                game.killGame()

                import GalacticWars
                GalacticWars.menu.MainMenu()

            if xSpeed > maxSpeed:
                xSpeed = maxSpeed
            if xSpeed < -maxSpeed:
                xSpeed = -maxSpeed
            
            if ySpeed > maxSpeed:
                ySpeed = maxSpeed
            if ySpeed < -maxSpeed:
                ySpeed = -maxSpeed

            x += xSpeed
            y += ySpeed

            if shot >= neededshot:
                s = shot
                sc = score

                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionComplete(sc,s,"P4L5")

            if x > 700:
                x = 0
            if x < 0:
                x = 700
            if y > 500:
                y = 0
            if y < 0:
                y = 500

            if len(enemies) != 8:
                cor = r.choice(coordinates)

                enemies.append(Enemy(r.choice(enemySprites),r.randint(cor[0],cor[1]),cor[4], 0*cor[2], 2*cor[3], 10,125,cor[5]))

            if gameThings["Health"] < 20:
                lh = makeSound("Assets/Sounds/Game/Effects/lowhealth.wav")
                playSound(lh)

            if gameThings["Health"] <= 0:
                game.killGame()

                import GalacticWars
                GalacticWars.menu.missionFailed()

            for bullet in bullets:  # ask each bullet in the list to move
                if bullet.move() == False:
                    bulletRun = False
                    hideSprite(sprite)
                    bullets.remove(bullet)

            for enemy in enemies:
                if enemy.move() == False or enemy.hit() == True:
                    hideSprite(enemy.sprite)
                    enemies.remove(enemy)

            moveSprite(spaceSprite,x,y)

            tick(60)
            updateDisplay() #Defense

    def killGame():
        global health
        global scoret
        global obj
        global sprite
        global spaceSprite
        global score
        global shot

        score = 0
        shot = 0

        killSprite(sprite)
        killSprite(spaceSprite)

        hideLabel(health)
        hideLabel(scoret)
        hideLabel(obj)

        for enemy in enemies:
            enemies.remove(enemy)
            enemy.kill()

class Projectile():
    def __init__(self, xpos, ypos, xspeed, yspeed, damage):
        global sprite

        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        self.yspeed = yspeed

        self.move()
        showSprite(sprite)

    def move(self):
        global sprite

        self.xpos += self.xspeed
        self.ypos += self.yspeed

        if self.xpos < 0 or self.xpos > 800 or self.ypos < 0 or self.ypos > 800:
            return False

        moveSprite(sprite,self.xpos,self.ypos)
        return True

    def kill(self):
        global sprite

        killSprite(sprite)

class Enemy():
    def __init__(self,sprite, xpos, ypos, xspeed, yspeed, damage,health,angle=180):
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        self.yspeed = yspeed

        self.damage = damage
        self.health = health
        self.angle = angle

        self.sprite = makeSprite(sprite)
        addSpriteImage(self.sprite,"Assets/Images/Ship/explosion.png")
        self.move()
        showSprite(self.sprite)

    def move(self):
        global score
        global scoret

        transformSprite(self.sprite,self.angle,1)
        self.xpos += self.xspeed
        self.ypos += self.yspeed
        if self.xpos < 0 or self.xpos > 800 or self.ypos < 0 or self.ypos > 800:
            score -= 10
            changeLabel(scoret,"SCORE: "+str(score))
            return False
        
        moveSprite(self.sprite, self.xpos, self.ypos)
        return True

    def hit(self):
        global spaceSprite
        global sprite
        global gameThings
        global health
        global scoret
        global score
        global shot

        if touching(self.sprite,spaceSprite):
            gameThings["Health"] -= self.damage
            score -= 50
            changeLabel(scoret,"SCORE: "+str(score))
            changeLabel(health,"HEALTH: "+str(gameThings["Health"]))
            return True

        if touching(self.sprite,sprite):

            self.health -= gameThings["Damage"]

            if self.health <=0:
                score += 100
                shot += 1
                changeSpriteImage(self.sprite,1)
                explode = makeSound("Assets/Sounds/Game/Effects/explode.wav")
                changeLabel(health,"HEALTH: "+str(gameThings["Health"]))
                changeLabel(scoret,"SCORE: "+str(score))
                playSound(explode)
                return True
        else:
            return False

    def kill(self):
        killSprite(self.sprite)

