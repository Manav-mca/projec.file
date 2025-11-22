import pygame
import random
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

class Snake:
    def __init__(self):
        self.body = [(WIDTH//2, HEIGHT//2)]
        self.direction = (20, 0)
        
    def move(self):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, head)
        self.body.pop()
        
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, 20, 20))

class WaterGun:
    def __init__(self):
        self.bullets = []
        
    def shoot(self, x, y, direction):
        self.bullets.append([x, y, direction[0]*2, direction[1]*2])
        
    def update(self):
        for bullet in self.bullets[:]:
            bullet[0] += bullet[2]
            bullet[1] += bullet[3]
            if bullet[0] < 0 or bullet[0] > WIDTH or bullet[1] < 0 or bullet[1] > HEIGHT:
                self.bullets.remove(bullet)
                
    def draw(self, screen):
        for bullet in self.bullets:
            pygame.draw.circle(screen, BLUE, (int(bullet[0]), int(bullet[1])), 3)

class Target:
    def __init__(self):
        self.x = random.randint(20, WIDTH-20)
        self.y = random.randint(20, HEIGHT-20)
        
    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), 10)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Water Gun Snake")
    clock = pygame.time.Clock()
    
    snake = Snake()
    water_gun = WaterGun()
    target = Target()
    score = 0
    font = pygame.font.Font(None, 36)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    water_gun.shoot(snake.body[0][0], snake.body[0][1], snake.direction)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake.direction != (0, 20):
            snake.direction = (0, -20)
        elif keys[pygame.K_DOWN] and snake.direction != (0, -20):
            snake.direction = (0, 20)
        elif keys[pygame.K_LEFT] and snake.direction != (20, 0):
            snake.direction = (-20, 0)
        elif keys[pygame.K_RIGHT] and snake.direction != (-20, 0):
            snake.direction = (20, 0)
        
        snake.move()
        water_gun.update()
        
        # Check bullet-target collision
        for bullet in water_gun.bullets[:]:
            if abs(bullet[0] - target.x) < 15 and abs(bullet[1] - target.y) < 15:
                water_gun.bullets.remove(bullet)
                target = Target()
                score += 1
        
        # Wrap snake around screen
        head = snake.body[0]
        if head[0] < 0:
            snake.body[0] = (WIDTH, head[1])
        elif head[0] > WIDTH:
            snake.body[0] = (0, head[1])
        elif head[1] < 0:
            snake.body[0] = (head[0], HEIGHT)
        elif head[1] > HEIGHT:
            snake.body[0] = (head[0], 0)
        
        screen.fill(BLACK)
        snake.draw(screen)
        water_gun.draw(screen)
        target.draw(screen)
        
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
