from pygame import*
class GameSprite(sprite.Sprite):
    s_width=0
    s_height=0
    s_speed=0
    image=0
    s_win=0
    rect=0
    i=0
    s_HP=0



    def __init__(self,width,height,x,y,speed,img,win,HP):
        sprite.Sprite.__init__(self)
        self.s_width=width
        self.s_height=height
        self.s_speed=speed
        self.s_win=win
        self.image=transform.scale(image.load(img),(self.s_width,self.s_height))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.i=0
        self.s_HP=HP



    def reset(self):
        self.s_win.blit(self.image,(self.rect.x,self.rect.y))
    

class BulletSprite(GameSprite):
    def update(self):
        self.rect.x+=self.s_speed
        if self.rect.x>1000 or self.rect.x<-10:
            self.kill()

class Enemy(GameSprite):
    def update(self):
        self.rect.x-=self.s_speed
        if self.rect.x<-110:
            self.kill()


class PlayerSprite(GameSprite):
    def draw(self):
        keys=key.get_pressed()
        if keys[K_a] and self.rect.x>5:
            self.rect.x -=self.s_speed

        if keys[K_d] and self.rect.x<400-self.s_width-5:
            self.rect.x += self.s_speed

        if keys[K_w] and self.rect.y>5:
            self.rect.y -=self.s_speed

        if keys[K_s] and self.rect.y<700-self.s_height-5:
            self.rect.y +=self.s_speed


