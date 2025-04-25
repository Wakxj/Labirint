from pygame import*

okno = display.set_mode((800,500))
fps = time.Clock()
game = True

fon1 = transform.scale(image.load('fon.jpg'), (800,500))
fon2 = transform.scale(image.load('fon.jpg'), (800,500))
fon3 = transform.scale(image.load('fon.jpg'), (800,500))
xfona = 0

fon4 = transform.scale(image.load('perekati.png'), (350,250))
fon5 = transform.scale(image.load('perekati.png'), (350,250))
fon6 = transform.scale(image.load('perekati.png'), (350,250))
xfona2 = 250



class gameobject(sprite.Sprite):
    def __init__(self, img, x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.image1 = transform.scale(image.load(img),(w,h))
        self.image2 = transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))

hero = gameobject('mariopng.ru-50.png', 460,300,100,100)
direct = 'right'
xhero = 0

abobus = gameobject('fade.jpg', 290,300,100,100)



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    okno.blit(fon1,  (xfona - 800, 0))
    okno.blit(fon2,  (xfona, 0))
    okno.blit(fon3, (xfona + 800, 0))
    hero.ris()
    abobus.ris()
    abobus.rect.x = xhero + 600
    kn = key.get_pressed()
    if kn[K_a]:
        xfona += 5
        xfona2 += 7
        xhero += 5
        direct = "left"
    if kn[K_d]:
        xfona -= 5
        xfona2 -= 7
        xhero -= 5
        direct = 'right'
    if direct == 'right':
        hero.image = hero.image1
    if direct == 'left':
        hero.image = hero.image2
    if xfona < -800:
        xfona = 0
    if xfona > 800:
        xfona = 0 
    if xfona2 < - 800:
        xfona2 = 0
    if xfona2 > + 800:
        xfona2 = 0





    okno.blit(fon4,  (xfona2 - 800, 300))
    okno.blit(fon5, (xfona2, 300))
    okno.blit(fon6, (xfona2 + 800, 300))

    fps.tick(60)
    display.update()