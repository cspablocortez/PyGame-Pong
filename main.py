import pygame
from random import randint
from time import sleep
from settings import *
from puck import Puck
from paddle import Paddle
from score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.running = True

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("User asked to quit.")
                    self.playing = False
            self.draw()

    def draw(self):
        self.screen.fill(BLACK)


        # === board ===

        for i in range(1, 380, 10):
            pygame.draw.rect(self.screen, puck.color, [int(WIDTH / 2), i + 10, 5, 5], 0)

        pygame.draw.rect(self.screen, puck.color, [0, 2, WIDTH, 5], 0)
        pygame.draw.rect(self.screen, puck.color, [0, HEIGHT - 10, WIDTH, 5], 0)

        # == end board ---

        p1_score.display_score()
        p2_score.display_score()

        p1.move()
        p2.move()
        puck.move()

        for paddle in [p1, p2]:
            puck.check_collision(paddle)

        if puck.x < 0:
            p2_score.increase_score()
        if puck.x > (WIDTH - puck.size):
            p1_score.increase_score()

        pygame.display.update()


# class Puck:
#     def __init__(self):
#         self.color = (255, 255, 255)
#         self.size = 15
#         self.x = int(WIDTH / 2)
#         self.y = int(HEIGHT / 2)
#         self.x_vel = randint(3, 5)
#         self.y_vel = randint(3, 5)
#         self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
#
#     def move(self):
#
#         if self.x < 0 or self.x > (WIDTH - self.size):
#             sleep(0.5)
#             self.color = (0, 0, 255)
#             self.x = WIDTH / 2
#             self.y = HEIGHT / 2
#             self.x_vel = randint(-4, 4)
#             self.y_vel = randint(-4, 4)
#             self.color = (255, 255, 255)
#
#         if self.y < 0 or self.y > (HEIGHT - self.size):
#             self.y_vel *= -1
#
#         self.x += self.x_vel
#         self.y += self.y_vel
#         self.rect = pygame.draw.rect(screen, self.color, [int(self.x), int(self.y), self.size, self.size], 0)
#
#     def check_collision(self, sprite):
#         if self.rect.colliderect(sprite):
#             self.x_vel *= -1.1
#             self.y_vel *= -1.1


# class Paddle:
#     def __init__(self, team):
#         self.team = team
#         self.color = (255, 255, 255)
#         self.width = 15
#         self.height = 100
#         self.y = int(0 + HEIGHT / 3)
#         self.velocity = 5
#         self.score = 0
#
#         if team == "player1":
#             self.x = self.x = 0 + self.width * 2
#         else:
#             self.x = WIDTH - self.width * 2
#
#         self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
#
#     def move(self):
#         if self.y < 0:
#             self.y = 0
#
#         if self.y > HEIGHT - self.height:
#             self.y = HEIGHT - self.height
#
#         keys = pygame.key.get_pressed()
#         if self.team == "player1":
#             if keys[pygame.K_w]:
#                 self.y -= self.velocity
#             if keys[pygame.K_s]:
#                 self.y += self.velocity
#
#         if self.team == "player2":
#             if keys[pygame.K_UP]:
#                 self.y -= self.velocity
#             if keys[pygame.K_DOWN]:
#                 self.y += self.velocity
#
#         self.rect = pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])


# class Score:
#     def __init__(self, player):
#         self.score = 0
#
#         if player == "player1":
#             self.x = WIDTH / 4
#             self.y = 20
#
#         if player == "player2":
#             self.x = WIDTH / 2 + WIDTH / 4
#             self.y = 20
#
#     def increase_score(self):
#         self.score += 1
#
#     def display_score(self):
#         font = pygame.font.SysFont("Arial", 72)
#         text = font.render(str(self.score), True, (255, 255, 255))
#         screen.blit(text, [int(self.x), int(self.y)])
#
#     def reset_score(self):
#         self.score = 0


puck = Puck()
p1 = Paddle("player1")
p2 = Paddle("player2")

p1_score = Score("player1")
p2_score = Score("player2")

# =============== LOOP ===============


pygame.quit()
