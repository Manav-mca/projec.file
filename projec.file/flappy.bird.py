import pygame
import random

pygame.init()
W, H = 400, 600

class Bird:
    def __init__(self):
        self.y = H//2
        self.vel = 0
    
    def jump(self):
        self.vel = -10
    
    def update(self):
        self.vel += 0.8
        self.y += self.vel
    
    def draw(self, s):
        pygame.draw.circle(s, (255,255,0), (50, int(self.y)), 20)

class Pipe:
    def __init__(self, x):
        self.x = x
        self.gap = random.randint(150, 400)
    
    def update(self):
        self.x -= 3
    
    def draw(self, s):
        pygame.draw.rect(s, (0,255,0), (self.x, 0, 50, self.gap))
        pygame.draw.rect(s, (0,255,0), (self.x, self.gap+120, 50, H))
    
    def collides(self, bird):
        if 30 <= self.x <= 70:
            return not (self.gap < bird.y < self.gap+120)
        return False

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

bird = Bird()
pipes = [Pipe(W + i*200) for i in range(3)]
score = 0

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: break
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            bird.jump()
    
    bird.update()
    
    for pipe in pipes:
        pipe.update()
        if pipe.collides(bird):
            print(f"Game Over! Score: {score}")
            pygame.quit()
            exit()
        if pipe.x == 20:
            score += 1
    
    # Reset pipes
    if pipes[0].x < -50:
        pipes.pop(0)
        pipes.append(Pipe(W))
    
    # Boundaries
    if bird.y < 0 or bird.y > H:
        print(f"Game Over! Score: {score}")
        pygame.quit()
        exit()
    
    screen.fill((135,206,235))
    bird.draw(screen)
    for pipe in pipes:
        pipe.draw(screen)
    
    font = pygame.font.Font(None, 36)
    screen.blit(font.render(str(score), True, (255,255,255)), (10, 10))
    
    pygame.display.flip()
    clock.tick(60)
else:
    pygame.quit()

  