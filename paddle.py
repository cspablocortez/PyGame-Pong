class Paddle:
    def __init__(self, team):
        self.team = team
        self.color = (255, 255, 255)
        self.width = 15
        self.height = 100
        self.y = int(0 + HEIGHT / 3)
        self.velocity = 5
        self.score = 0

        if team == "player1":
            self.x = self.x = 0 + self.width * 2
        else:
            self.x = WIDTH - self.width * 2

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        if self.y < 0:
            self.y = 0

        if self.y > HEIGHT - self.height:
            self.y = HEIGHT - self.height

        keys = pygame.key.get_pressed()
        if self.team == "player1":
            if keys[pygame.K_w]:
                self.y -= self.velocity
            if keys[pygame.K_s]:
                self.y += self.velocity

        if self.team == "player2":
            if keys[pygame.K_UP]:
                self.y -= self.velocity
            if keys[pygame.K_DOWN]:
                self.y += self.velocity

        self.rect = pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])