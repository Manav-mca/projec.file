import pygame
import random

pygame.init()
W, H = 600, 400

class Snake:
    def __init__(self):
        self.pos = [W//2, H//2]
        self.dir = [20, 0]
    
    def move(self):
        self.pos[0] += self.dir[0]
        self.pos[1] += self.dir[1]
        self.pos[0] %= W
        self.pos[1] %= H
    
    def draw(self, s):
        pygame.draw.rect(s, (0,255,0), (*self.pos, 20, 20))

class Bullet:
    def __init__(self, x, y, dx, dy):
        self.x, self.y, self.dx, self.dy = x, y, dx*3, dy*3
    
    def update(self):
        self.x += self.dx
        self.y += self.dy
        return 0 <= self.x <= W and 0 <= self.y <= H
    
    def draw(self, s):
        pygame.draw.circle(s, (0,0,255), (int(self.x), int(self.y)), 3)

class Target:
    def __init__(self):
        self.x = random.randint(20, W-20)
        self.y = random.randint(20, H-20)
    
    def draw(self, s):
        pygame.draw.circle(s, (255,0,0), (self.x, self.y), 10)

# Game objects
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
snake = Snake()
bullets = []
target = Target()
score = 0

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: break
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                bullets.append(Bullet(*snake.pos, *snake.dir))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: snake.dir = [0, -20]
    if keys[pygame.K_DOWN]: snake.dir = [0, 20]
    if keys[pygame.K_LEFT]: snake.dir = [-20, 0]
    if keys[pygame.K_RIGHT]: snake.dir = [20, 0]
    
    snake.move()
    bullets = [b for b in bullets if b.update()]
    
    # Collision
    for b in bullets[:]:
        if abs(b.x - target.x) < 15 and abs(b.y - target.y) < 15:
            bullets.remove(b)
            target = Target()
            score += 1
    
    screen.fill((0,0,0))
    snake.draw(screen)
    target.draw(screen)
    for b in bullets: b.draw(screen)
    
    font = pygame.font.Font(None, 36)
    screen.blit(font.render(f"Score: {score}", True, (255,255,255)), (10, 10))
    
    pygame.display.flip()
    clock.tick(15)
else:
    pygame.quit()
