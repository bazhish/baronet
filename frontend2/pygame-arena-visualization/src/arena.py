class Arena:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.platforms = []
        self.obstacles = []

    def add_platform(self, platform):
        self.platforms.append(platform)

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def draw(self, screen):
        for platform in self.platforms:
            platform.draw(screen)
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def update(self):
        for obstacle in self.obstacles:
            obstacle.update()