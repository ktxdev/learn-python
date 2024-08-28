import math
import pygame
import random

# Initisialize the pygame
pygame.init()

# Create the screen/windows
screen = pygame.display.set_mode((800, 600))
running = True

# Change title and icon
pygame.display.set_caption("Space Invadors")
icon = pygame.image.load("./assests/ufo.png")
pygame.display.set_icon(icon)

playerImage = pygame.image.load("./assests/player.png")
playerX = 370
playerY = 480
playerX_change = 0

enemyImage = pygame.image.load("./assests/enemy.png")
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40

backgroundImage = pygame.image.load("./assests/background.jpg")

bulletImage = pygame.image.load("./assests/bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.4
bullet_state = "ready"

score = 0

def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y):
    screen.blit(enemyImage, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage, (x + 16, y + 10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    return False

# Gaming loop
while running:
    screen.fill((0, 0, 0))
    screen.blit(backgroundImage, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if left or right arrow is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0

    if playerX >= 736:
        playerX = 736

    # Enemy movement
    enemyX += enemyX_change
    
    if enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change

    if enemyX >= 736:
        enemyX_change = -0.2
        enemyY += enemyY_change

    # Bullet Movement
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    # Collision
    collision = is_collision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)


    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()