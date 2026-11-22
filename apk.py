import pygame

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((600,300))
pygame.display.set_caption("SPACE ISOLATION")

nametag = "> gnaa <"
win = 'VICROTY !'
font = pygame.font.Font(
    "PAITON/fonts/Pixelate-Regular.ttf", 20)

clock = pygame.time.Clock()

halo = pygame.image.load(
    "PAITON/asset/standart.png"
).convert_alpha()

monsterX = pygame.image.load(
    "PAITON/asset/MonsterX.png"
)



monsterX = pygame.transform.scale(monsterX, (100, 100))
bg = pygame.image.load(
    "PAITON/asset/deck.png"
).convert_alpha()

halo = pygame.transform.scale(halo, (50, 50))
halo_fire = pygame.image.load (
    "PAITON/asset/fire.png"
)

halo_fire = pygame.transform.scale(halo_fire, (50, 50))
halo_rect = halo.get_rect()
bg = pygame.transform.scale(bg, (600, 300))
player = halo

fire = pygame.image.load(
    "PAITON/asset/Ammo.png"
).convert_alpha()
fire = pygame.transform.scale(fire, (96,94))
YELLOW = (255, 230, 70)
white = (255, 255, 255)


maxH = 100
cur = 100

hp_bg = pygame.draw.rect(
    screen,
    white,
    (20, 20, 200, 10)
)

hp = hp_bg = pygame.draw.rect(
    screen,
    YELLOW,
    (20, 20, 200, 10)
)
X_bg = pygame.draw.rect(
    screen,
    white,
    (380, 20, 200, 10)
)

X_hp = X_bg = pygame.draw.rect(
    screen,
    YELLOW,
    (380, 20, 200, 10)
)
speed = 3

halo_x = 50
halo_y = 195

M_x = 490
M_y = 150

Fire = []
fire_speed = 8
fire_delay = 300

monsterX_rect = monsterX.get_rect(
    topleft=(M_x, M_y)
)

damage = -80
makX = 200
curX = 200
last_fire = -fire_delay

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        halo_x += speed

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        halo_x -= speed

    halo_rect.topleft = (round(halo_x), halo_y)

    current_time = pygame.time.get_ticks()
    if keys[pygame.K_SPACE]:

        player = halo_fire


        if current_time - last_fire >= fire_delay:

                bullet_rect = fire.get_rect(
                    midleft=(
                        halo_rect.right,
                        halo_rect.centery
                    )
                )

                Fire.append(bullet_rect)

                last_fire = current_time

    else:
        player = halo


    for bullet in Fire:
                bullet.x += fire_speed

    Fire = [
            bullet for bullet in Fire
                if bullet.left < 600
        ]

    for bullet in Fire[:]:

        if curX > 0 and bullet.colliderect(monsterX_rect):

            makX -= damage

            curX = max(0, curX)

            Fire.remove(bullet)


    screen.fill((30, 30, 40))
    screen.blit(bg, (0, 0))

    screen.blit(player, (halo_x, halo_y))
    screen.blit(monsterX, (M_x, M_y))
    pygame.draw.rect(screen, white, hp_bg)
    pygame.draw.rect(screen, white, X_bg)

    for bullet in Fire:
        screen.blit(fire, bullet)

    hp_w = int(
        200 * (cur/maxH)
    )

    hp_bar = pygame.Rect(
        20, 20, hp_w, 10
    )

    pygame.draw.rect(screen, YELLOW, hp_bar)

    X_w = int(
       200 * curX/makX
    )

    X_bar = pygame.Rect(
        380, 20, X_w, 10
    )

    pygame.draw.rect(screen, YELLOW, X_bar)

    name_text = font.render(
        nametag,
        True,
        YELLOW
    )

    win_text = font.render(
            win,
            True,
            YELLOW
        )

    if makX > 600:
        screen.blit(win_text, (250, 150))

    name_rect = name_text.get_rect (
        midbottom=(halo_rect.centerx, halo_rect.top -5)
    )

    box_rect = name_rect.inflate(12, 8)
    screen.blit(name_text, name_rect)
    halo_rect.topleft = (round(halo_x), halo_y)

    pygame.display.update()

    clock.tick(60)

pygame.quit()