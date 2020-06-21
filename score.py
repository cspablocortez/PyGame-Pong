class Score:
    def __init__(self, player):
        self.score = 0

        if player == "player1":
            self.x = WIDTH / 4
            self.y = 20

        if player == "player2":
            self.x = WIDTH / 2 + WIDTH / 4
            self.y = 20

    def increase_score(self):
        self.score += 1

    def display_score(self):
        font = pygame.font.SysFont("Arial", 72)
        text = font.render(str(self.score), True, (255, 255, 255))
        screen.blit(text, [int(self.x), int(self.y)])

    def reset_score(self):
        self.score = 0