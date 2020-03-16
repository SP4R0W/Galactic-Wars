import pygame
import math

import random as r
import winsound as ws

from time import sleep

pygame.init()

#=========================
#COLORS
#=========================
black = (0,0,0)
white = (255,255,255)
transparent = (0,0,0,0)

indigo = (75,0,130)
pink = (255,192,203)
purple = (128,0,128)
violet = (148,0,211)
royalblue = (65,105,225)
emeraldgreen = (0,201,87)
limegreen = (50,205,50)
forestgreen = (34,139,34)
yellow = (255,255,0)
gold = (205,173,0)
orange = (255,165,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

grey = (128,128,128)

fadeColors = [(245,245,245), #whiteSmoke
(220,220,220), #gainsboro
(211,211,211), #lightGrey
(192,192,192), #silver
(169,169,169), #darkGrey
(128,128,128), #grey
(105,105,105), #dimGrey
(0,0,0)] #black



#=========================
#FONTS
#=========================
arial = 'Assets/Fonts/arial.ttf'
calibri = 'Assets/Fonts/calibri.ttf'
comicsans = 'Assets/Fonts/comic.ttf'
georgia = 'Assets/Fonts/georgia.ttf'
segoesc = 'Assets/Fonts/segoesc.ttf'
timesnewroman = 'Assets/Fonts/times.ttf'
vgadixe = 'Assets/Fonts/vgafixe.fon'
vgasyse = 'Assets/Fonts/vgasyse.fon'


gameWindow = pygame.display.set_mode((640,480))
gameWindow.fill((255,255,255))
pygame.display.update()


class Button:

    def __init__(self,
                 x,y,
                 width=0,height=0,
                 text = "",
                 font = calibri,
                 fontColor = black,
                 ringColor = black,
                 normalColor = red,
                 activeColor = grey,
                 clickSound = None,
                 active=True,
                 action = None):

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.text = text
        self.font = font
        self.fontColor = fontColor

        self.ringColor = ringColor
        self.normalColor = normalColor
        self.activeColor = activeColor

        self.action = action
        self.active = active

        return None

    def draw(self):

        if self.width == 0 and self.height == 0:
            textList = []
            for letter in self.text:
                textList.append(letter)

            self.width = len(textList) * 15
            self.height = len(textList) * 5

            fontSize = self.width / 4
            fontSize = math.floor(fontSize)

        if self.active != False:
            click = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()

            if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
                pygame.draw.rect(gameWindow,self.ringColor,(self.x-5,self.y-5,self.width+10,self.height+10))
                pygame.draw.rect(gameWindow,self.activeColor,(self.x,self.y,self.width,self.height))

                f = pygame.font.Font(self.font,fontSize)
                t = f.render(self.text,False,self.fontColor).convert_alpha()
                gameWindow.blit(t,(self.x+(self.width/5),self.y+(self.height/5)))

                if click[0] == 1 and self.action != None:
                    ws.PlaySound(self.clickSound,ws.SND_ASYNC)
                    self.action()
            else:
                pygame.draw.rect(gameWindow,self.ringColor,(self.x-5,self.y-5,self.width+10,self.height+10))
                pygame.draw.rect(gameWindow,self.normalColor,(self.x,self.y,self.width,self.height))

                f = pygame.font.Font(self.font,fontSize)
                t = f.render(self.text,False,self.fontColor).convert_alpha()
                gameWindow.blit(t,(self.x+(self.width/5),self.y+(self.height/5)))

        else:
            pygame.draw.rect(gameWindow,self.ringColor,(self.x-5,self.y-5,self.width+10,self.height+10))
            pygame.draw.rect(gameWindow,grey,(self.x,self.y,self.width,self.height))

            f = pygame.font.Font(self.font,16)
            t = f.render(self.text,False,self.fontColor).convert_alpha()
            gameWindow.blit(t,(self.x+(self.width/5),self.y+(self.height/5)))
        
    def get_x(self):

        return self.x

    def get_y(self):

        return self.y


class TextButton:

    def __init__(self,
                 x,y,
                 text="",
                 font=calibri,
                 fontSize=16,
                 normalColor=black,
                 activeColor=grey,
                 clickSound = None,
                 active=True,
                 action=None):

        self.x = y
        self.y = y

        self.text = text
        self.font = font
        self.fontSize = fontSize
        self.normalColor = normalColor
        self.activeColor = activeColor
        self.clickSound = clickSound
        
        self.active = active
        self.action = action

    def draw(self):
    
        if self.active != False:
            f = pygame.font.Font(self.font,self.fontSize)
            t = f.render(self.text,False,self.normalColor).convert_alpha()
            gameWindow.blit(t,(self.x,self.y))

            wid = t.get_rect().width
            hei = t.get_rect().height

            click = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()

            if self.x + wid > mouse[0] > self.x and self.y + hei > mouse[1] > self.y:
                f = pygame.font.Font(self.font,self.fontSize)
                t = f.render(self.text,True,self.activeColor).convert_alpha()
                gameWindow.blit(t,(self.x,self.y))
        
                if click[0] == 1 and self.action != None:
                    ws.PlaySound(self.clickSound,ws.SND_ASYNC)
                    self.action()

    def get_x(self):

        return self.x

    def get_y(self):

        return self.y


class ImageButton:

    def __init__(self,
                 x,y,
                 image=None,
                 width=0,height=0,
                 text="",
                 textx=0,texty=0,
                 font=calibri,
                 fontSize=16,
                 fontColor=black,
                 normalColor = red,
                 activeColor = grey,
                 clickSound = None,
                 action=None,
                 active=True):
        
        self.x = x
        self.y = y

        self.image = image

        self.width = width
        self.height = height

        self.text = text
        self.textx = textx
        self.texty = texty
        self.font = font
        self.fontSize = fontSize
        self.fontColor = fontColor

        self.normalColor = normalColor
        self.activeColor = activeColor
        
        self.clickSound = clickSound
        self.action = action
        self.active = active

    def draw(self):

        if self.active != False:
            click = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()
    
            img = pygame.image.load(self.image)

            if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
                pygame.draw.rect(gameWindow,self.activeColor,(self.x-5,self.y-5,self.width+10,self.height+10))
                gameWindow.blit(img,(self.x,self.y))

                f = pygame.font.Font(self.font,self.fontSize)
                t = f.render(self.text,True,self.activeColor)
                gameWindow.blit(t,(self.textx,self.texty))
        
                if click[0] == 1 and self.action != None:
                    s = pygame.mixer.Sound(self.clickSound)
                    pygame.mixer.Sound.play(s)
                    self.action()
            
            else:
                pygame.draw.rect(gameWindow,self.normalColor,(self.x-5,self.y-5,self.width+10,self.height+10))
                gameWindow.blit(img,(self.x,self.y))

                if self.textx == 0 and self.texty == 0:
                    f = pygame.font.Font(self.font,self.fontSize)
                    t = f.render(self.text,True,self.fontColor)
                    gameWindow.blit(t,(self.x+5,self.y+110))
            
                else:
                    f = pygame.font.Font(self.font,self.fontSize)
                    t = f.render(self.text,True,self.fontColor)
                    gameWindow.blit(t,(self.textx,self.texty))
            
      

    def get_x(self):

        return self.x

    def get_y(self):

        return self.y


class Text:

    def __init__(self,
                 x,y,
                 text="",
                 font=calibri,
                 fontSize=16,
                 fontColor=black,
                 angle=0):

        self.x = x
        self.y = y

        self.text = text

        self.font = font
        self.fontSize = fontSize
        self.fontColor = fontColor

        self.angle = angle

        return None

    def draw(self):
        f = pygame.font.Font(self.font,self.fontSize)
        t = f.render(self.text,True,self.fontColor).convert_alpha()
        t = pygame.transform.rotate(t,self.angle)
        gameWindow.blit(t,(self.x,self.y))

    def get_x(self):

        return self.x

    def get_y(self):

        return self.y


class Image:

    def __init__(self,
                 x,y,
                 image):

        self.x = x
        self.y = y

        self.image = image

    def draw(self):

        img = pygame.image.load(self.image).convert_alpha()
        gameWindow.blit(img,(self.x,self.y))

    def get_x(self):

        return self.x

    def get_y(self):

        return self.y


class Music:

    def __init__(self,
                 track,
                 delay=0,
                 looped=1):

        self.track = track

        self.delay = delay

        self.looped = looped

    def play(self):
        sleep(self.delay)
        pygame.mixer.music.load(self.track)
        pygame.mixer.music.play(self.looped)

    def get_length():

        return pygame.mixer.music.get_length()

                              
class Sound:

    def __init__(self,
                 track,
                 delay=0):

        self.track = track

        self.delay = delay


    def play(self):
        sleep(self.delay)
        ws.PlaySound(self.track,ws.SND_ASYNC)
