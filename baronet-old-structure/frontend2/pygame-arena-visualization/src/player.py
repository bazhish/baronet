class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.velocity = 5
        self.is_jumping = False
        self.jump_count = 10

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x - self.velocity > 0:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.x + self.velocity < 800 - self.width:
            self.x += self.velocity
        if not self.is_jumping:
            if keys[pygame.K_SPACE]:
                self.is_jumping = True
        else:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))