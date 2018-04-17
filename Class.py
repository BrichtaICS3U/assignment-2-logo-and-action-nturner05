class Logo(pygame.sprite.Sprite):

    def __init__(self, width, height, speed):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.width=width
        self.height=height
        self.speed = speed

    pygame.draw.ellipse(screen, BLACK, [80, 80, 250, 250], 2)
    pygame.draw.ellipse(screen, BLACK, [90, 90, 230, 230], 0)
    pygame.draw.ellipse(screen, WHITE, [130, 130, 150, 150], 0)

    self.rect = self.image.get_rect()

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20
    
    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
