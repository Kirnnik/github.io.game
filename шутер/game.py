from pygame import*
from hz import* 
import sys
from random import randint
font.init()
font = font.Font(None,36)
win=display.set_mode((1000,700))
display.set_caption("Star Time")
def menu():
    mixer.init()
    mixer.music.load('back(5).mp3')
    win.fill((0,0,0))
    img2=transform.scale(image.load('STAR TIME.png'),(500,100))
    win.blit(img2,(250,200))
    play=Enemy(200,100,400,450,0,"Play.png",win,0)
    ex=Enemy(200,100,400,570,0,"Exit.png",win,0)
    clock = time.Clock()
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)
    while True:

        clock.tick(60)
        for e in event.get():
            if e.type == QUIT:
                exit(0)
        if mouse.get_pressed()[0]:
            c = mouse.get_pos()
            if play.rect.collidepoint(c):
                game()
            if ex.rect.collidepoint(c):
                exit(0)

        play.reset()
        ex.reset()
        display.update()



def game():
    img1 = transform.scale(image.load('Game_over.png'), (700, 400))
    

    rocket=PlayerSprite(78,63,30,250,7,"rocket.png",win,5)

    mixer.init()
    mixer.music.load('megalovania.mp3')


    bullets=sprite.Group()
    AlienBullets=sprite.Group()
    Aliens=sprite.Group()
    Meteorite=sprite.Group()
    ExtraLifeG=sprite.Group()
    ExtraAmmoG=sprite.Group()
    Stars=sprite.Group()
    Planet1=sprite.Group()

    sound1 = mixer.Sound('Hit.wav')
    sound2 = mixer.Sound('shoot.wav')
    sound3 = mixer.Sound('boom.wav')
    sound4 = mixer.Sound('GameOver.wav')
    sound5 = mixer.Sound('extra.wav')
    m=0

    timer=0
    score=0
    Extrah=0
    MusicTime=0
    t=40
    AlienKills=0
    ShotRocket=0
    ShotAliens=0
    n=100
    Ammo=False
    SpawnAliens=0
    SpawnMeteor=0
    BangTime=0
    AlienPass=0
    Ammoh=0
    AmmoTime=0
    StarTime=0
    PlanetTime=0
    AlienKill=0
    r1= transform.scale(image.load("rocket.png"),(78,63))
    r2= transform.scale(image.load("rocket1.png"), (78,63))
    r3= transform.scale(image.load("rocket2.png"), (78,63))

    a1=transform.scale(image.load("alien.png"),(80,65))
    a2=transform.scale(image.load("alien1.png"),(80,65))
    a3=transform.scale(image.load("alien2.png"),(80,65))

    Lose=False

    clock = time.Clock()
    run=True
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)
    while run:
        
        if Lose==False:
            clock.tick(60)
            for e in event.get():
                    if e.type == QUIT:
                        exit(0)

            ys=randint(0,690)
            wh=randint(4,14)
            star=Enemy(wh,wh,1000,ys,3,"star.png",win,0)
            if StarTime!=10:
                StarTime+=1
            else:
                Stars.add(star)
                StarTime=0

            yp=randint(0,650)
            whp=randint(36,72)
            p=randint(1,11)

            planet1=Enemy(whp,whp,1000,yp,2,"Planet1.png",win,0)
            
            planet2=Enemy(whp,whp,1000,yp,2,"Planet2.png",win,0)
            
            planet3=Enemy(whp,whp,1000,yp,2,"Planet3.png",win,0)
            
            planet4=Enemy(whp,whp,1000,yp,2,"Planet4.png",win,0)
            
            planet5=Enemy(whp,whp,1000,yp,2,"Planet5.png",win,0)
            
            planet6=Enemy(whp,whp,1000,yp,2,"Planet6.png",win,0)

            planet7=Enemy(whp,whp,1000,yp,2,"Planet7.png",win,0)

            planet8=Enemy(whp,whp,1000,yp,2,"Planet8.png",win,0)

            planet9=Enemy(whp,whp,1000,yp,2,"Planet9.png",win,0)

            planet10=Enemy(whp,whp,1000,yp,2,"Planet10.png",win,0)

            planet11=Enemy(whp,whp,1000,yp,2,"Planet11.png",win,0)

            if PlanetTime!=100:
                PlanetTime+=1
            else:
                if p==1:
                    Planet1.add(planet1)
                    p=0
                    PlanetTime=0
                elif p==2:
                    Planet1.add(planet2)
                    p=0
                    PlanetTime=0
                elif p==3:
                    Planet1.add(planet3)
                    p=0
                    PlanetTime=0
                elif p==4:
                    Planet1.add(planet4)
                    p=0
                    PlanetTime=0
                elif p==5:
                    Planet1.add(planet5)
                    p=0
                    PlanetTime=0
                elif p==6:
                    Planet1.add(planet6)
                    p=0
                    PlanetTime=0
                elif p==7:
                    Planet1.add(planet7)
                    p=0
                    PlanetTime=0
                elif p==8:
                    Planet1.add(planet8)
                    p=0
                    PlanetTime=0
                elif p==9:
                    Planet1.add(planet9)
                    p=0
                    PlanetTime=0
                elif p==10:
                    Planet1.add(planet10)
                    p=0
                    PlanetTime=0
                elif p==11:
                    Planet1.add(planet11)
                    p=0
                    PlanetTime=0

            ra=randint(1,3)
            if ra==1:
                rocket.image=r1
            elif ra==2:
                rocket.image=r2
            elif ra==3:
                rocket.image=r3

            y=randint(0,618)
            alien=Enemy(80,65,1000,y,7,"alien.png",win,3)
            if SpawnAliens!=t:
                SpawnAliens+=1
            else:
                Aliens.add(alien)
                SpawnAliens=0
            if MusicTime<310:
                MusicTime+=1
            else:
                t=35
            
            aa=randint(1,3)
            for e in Aliens:
                if aa==1:
                    e.image=a1
                elif aa==2:
                    e.image=a2
                elif aa==3:
                    e.image=a3
            
            ym=randint(0,618)
            meteor=Enemy(69,68,1000,ym,5,"meteor.png",win,3)
            if SpawnMeteor!=n:
                SpawnMeteor+=1
            else:
                Meteorite.add(meteor)
                SpawnMeteor=0
            
            for e in Aliens:
                if ShotAliens<120:
                    ShotAliens+=1
                else:
                    AlienBullet=BulletSprite(26,14,e.rect.x -20,e.rect.y +34,-12,"alienbullet.png",win,0)
                    AlienBullets.add(AlienBullet)
                    ShotAliens=0

            if Ammo==False:
                if ShotRocket<28:
                    ShotRocket+=1
                else:
                    sound2.play()
                    bullet=BulletSprite(30,14,rocket.rect.x +95,rocket.rect.y +23,12,"bullet.png",win,0)
                    bullets.add(bullet)
                    ShotRocket=0
            else:
                if ShotRocket<20:
                    ShotRocket+=1
                else:
                    sound2.play()
                    bullet=BulletSprite(30,14,rocket.rect.x +95,rocket.rect.y ,12,"bullet.png",win,0)
                    bullet1=BulletSprite(30,14,rocket.rect.x +95,rocket.rect.y +45,12,"bullet.png",win,0)
                    bullets.add(bullet)
                    bullets.add(bullet1)
                    ShotRocket=0

            for e in Aliens:
                if sprite.collide_rect(rocket,e):
                    sound3.play()
                    e.kill()
                    rocket.s_HP-=1
                    score-=50
                    Ammo=False
            for e in AlienBullets:
                if sprite.collide_rect(rocket,e):
                    sound3.play()
                    e.kill()
                    rocket.s_HP-=1
                    score-=50
                    Ammo=False
            for e in Meteorite:
                if sprite.collide_rect(rocket,e):
                    e.kill()
                    rocket.s_HP-=2
                    score-=100
                    Ammo=False

            collides=sprite.groupcollide(Aliens, bullets, True, True)
            for e in collides:
                sound1.play()
                e.kill()
                score+=100
                AlienKills+=1
                AlienKill+=1
                if AlienKills==5:
                    rocket.s_HP+=1
                Extrah=randint(1,50)
                if Extrah==10:
                    ExtraLife=BulletSprite(55,55,e.rect.x,e.rect.y,-4,"ExtraLife.png",win,0)
                    ExtraLifeG.add(ExtraLife)
                    Extrah=0
                Ammoh=randint(1,90)
                if Ammoh==1:
                    ExtraAmmo=BulletSprite(55,55,e.rect.x,e.rect.y,-4,"ExtraAmmo.png",win,0)
                    ExtraAmmoG.add(ExtraAmmo)
                    Ammoh=0

            for e in ExtraLifeG:
                if sprite.collide_rect(rocket,e):
                    e.kill()
                    rocket.s_HP+=1
                    sound5.play()
            for e in ExtraAmmoG:
                if sprite.collide_rect(rocket,e):
                    e.kill()
                    Ammo=True
                    sound5.play()

            collides=sprite.groupcollide(bullets, Meteorite, True, False) 
            for e in collides:
                e.kill()

            for e in Aliens:
                if e.rect.x < -100:
                    AlienPass+=1
                    e.kill()
                    score-=50
                    if AlienPass==5:
                        rocket.s_HP-=1 
                        AlienPass=0

            if rocket.s_HP<=0:
                Lose=True
            
            win.fill((0,0,0))
            for e in Planet1:
                e.update()
                e.reset()
            
            for e in Stars:
                e.reset()
                e.update()
            rocket.reset()
            rocket.draw()
            for e in ExtraLifeG:
                e.reset()
                e.update()
            for e in ExtraAmmoG:
                e.reset()
                e.update()
            for e in bullets:
                e.reset()
                e.update()
            for e in Aliens:
                e.update()
                e.reset()
            for e in AlienBullets:
                e.reset()
                e.update()
            for e in Meteorite:
                e.reset()
                e.update()

            text = font.render("HP: " + str(rocket.s_HP),1, (255, 255, 255))
            Score = font.render("Score: " + str(score),1, (255, 255, 255))
            win.blit(text, (10, 20))
            win.blit(Score, (100, 20))

            display.update()
        else:
            mixer.music.pause()
            if m==0:
                sound4.play()
                m+=1
            win.fill((0,0,0))
            win.blit(img1,(140,150))
            
            win.blit(Score, (435, 600))
            Kill = font.render("Aliens killed: "+str(AlienKill),1,(255,255,255))
            win.blit(Kill, (405, 650))
            if timer !=180:
                timer+=1
            else:
                res = font.render("Press F to restart",1,(255,255,255))
                win.blit(res, (400, 20))
                exi = font.render("Press H to return to the menu",1,(255,255,255))
                win.blit(exi, (400, 80))
                for e in event.get():
                    if e.type == KEYDOWN:
                        if e.key == K_f:
                            game()
                        if e.key == K_h:
                            menu()
                    if e.type == QUIT:
                        exit(0)
                
            display.update()
if __name__ == "__main__":
    menu()
if __name__ == "__main__":
    game()