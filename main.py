import pygame, os
import random, math
import Player, Asteroid, Bullet
pygame.font.init()

WIDTH, HEIGHT = 600,600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ASTEROIDS")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60
PLAYER_WIDTH, PLAYER_HEIGHT = 50,40

PLAYER_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Player.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
ASTEROID_IMAGE = pygame.image.load(os.path.join('Assets', 'asteroid1.png'))

SCORE_FONT = pygame.font.SysFont('Arial',30)

def blitRotate2(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)

def draw_window(player,asteroids,bullets,score):
    WIN.fill(BLACK)
    blitRotate2(WIN, PLAYER_IMAGE, player.get_position(), player.get_orientation())
    for asteroid in asteroids:
        blitRotate2(WIN, pygame.transform.scale(ASTEROID_IMAGE, (asteroid.get_rect().width, asteroid.get_rect().height)), asteroid.get_position(), asteroid.get_orientation())
    for bullet in bullets:
        pygame.draw.circle(WIN, WHITE, bullet.get_position(), 2)

    score_text = SCORE_FONT.render(
        "SCORE: " + str(score), 1, WHITE)
    WIN.blit(score_text, (10, 10))

    pygame.display.update()



def update_location(player,asteroids,bullets):
    newX = player.get_position()[0]+math.cos(player.get_orientation()*math.pi/180)*player.get_velocity()
    newY = player.get_position()[1]-math.sin(player.get_orientation()*math.pi/180)*player.get_velocity()
    if newX > WIDTH:
        newX = 0 - PLAYER_HEIGHT
    elif newX < 0 - PLAYER_WIDTH:
        newX = WIDTH
    if newY > HEIGHT:
        newY = 0 - PLAYER_HEIGHT
    elif newY < 0 - PLAYER_HEIGHT:
        newY = HEIGHT
    player.set_position((newX, newY))

    for asteroid in asteroids:
        newX = asteroid.get_position()[0]+math.cos(asteroid.get_orientation()*math.pi/180)*asteroid.get_velocity()
        newY = asteroid.get_position()[1]-math.sin(asteroid.get_orientation()*math.pi/180)*asteroid.get_velocity()
        if newX > WIDTH:
            newX = 0 - asteroid.get_rect().width
        elif newX < 0 - asteroid.get_rect().width:
            newX = WIDTH
        if newY > HEIGHT:
            newY = 0 - asteroid.get_rect().height
        elif newY < 0 - asteroid.get_rect().height:
            newY = HEIGHT
        asteroid.set_position((newX, newY))

    for bullet in bullets:
        newX = bullet.get_position()[0]+math.cos(bullet.get_orientation()*math.pi/180)*10
        newY = bullet.get_position()[1]-math.sin(bullet.get_orientation()*math.pi/180)*10
        if newX > WIDTH or newX < 0 or newY > HEIGHT or newY < 0:
            bullets.remove(bullet)
        bullet.set_position((newX, newY))
    

def handle_keys(keys_pressed,player):

    if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
        if player.get_velocity() < 8:
            player.add_velocity(1)
    elif player.get_velocity() > 0: 
        player.add_velocity(-1)
    if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
        if player.get_velocity() > -5:
            player.add_velocity(-1)
    elif player.get_velocity() < 0: 
        player.add_velocity(1)
    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
        player.add_orientation(5)
    if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
        player.add_orientation(-5)

def show_score(score):
    font = pygame.font.SysFont('Arial',100)
    gameover_text = font.render(
        "GAME OVER", 1, WHITE)
    score_text = font.render(
        "SCORE: " + str(score), 1, WHITE)
    WIN.blit(gameover_text, (10, HEIGHT//2-200))
    WIN.blit(score_text, (10, HEIGHT//2-100))

    pygame.display.update()

def main():
    while True:
        player = Player.Player((WIDTH//2-PLAYER_WIDTH//2,HEIGHT//2-PLAYER_HEIGHT//2),90,(PLAYER_WIDTH,PLAYER_HEIGHT))
        score = 0
        asteroids = []
        bullets = []
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()     
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and len(bullets) < 3:
                        bullets.append(Bullet.Bullet((player.get_position()[0]+PLAYER_WIDTH//2, player.get_position()[1]+PLAYER_HEIGHT//2),player.get_orientation()))

            keys_pressed = pygame.key.get_pressed()
            handle_keys(keys_pressed,player)
            if random.randint(1,200) == 1 and len(asteroids) < 7:
                asteroids.append(Asteroid.Asteroid(random.randint(2,3),(random.randint(1,WIDTH),HEIGHT)))
            for asteroid in asteroids:
                for bullet in bullets:
                    if bullet.get_rect().colliderect(asteroid.get_rect()):
                        asteroids += asteroid.break_asteroid()
                        asteroids.remove(asteroid)
                        bullets.remove(bullet)
                        score += 50
                if asteroid.get_rect().colliderect(player.get_rect()):
                    run = False

            update_location(player,asteroids,bullets)
            draw_window(player,asteroids,bullets,score)
        show_score(score)
        cont = False
        while cont == False:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()     
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        cont = True


if __name__ == "__main__":
    main()
