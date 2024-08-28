import math
import pygame
import random

from pygame import mixer

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

num_of_enemies = 6
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("./assests/enemy.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

backgroundImage = pygame.image.load("./assests/background.jpg")

# Background sound
mixer.music.load("./assests/background.wav")
mixer.music.play(-1)

bulletImage = pygame.image.load("./assests/bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.4
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX, textY = 10, 10

game_over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render(f"Score: {score_value}", True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage, (x + 16, y + 10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    return False

def game_over_text():
    over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (300, 250))

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
                    bullet_sound = mixer.Sound("./assests/laser.wav")
                    bullet_sound.play()
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

    # Bullet Movement
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    # Enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]


        if enemyY[i] > 510:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
    
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.2
            enemyY[i] += enemyY_change[i]

        if enemyX[i] >= 736:
            enemyX_change[i] = -0.2
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound("./assests/explosion.wav")
            explosion_sound.play()

            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        
        enemy(enemyX[i], enemyY[i], i)

    show_score(textX, textY)
    player(playerX, playerY)

    pygame.display.update()