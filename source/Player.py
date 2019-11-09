class Player(object):
	def __init__(self, snake, score, color, sprite=None, hp=3):
		self.snake=snake
		self.score=score
		self.color=color
		self.sprite=sprite
		self.hp=hp



   
        

    def handle_keys(self):
         key = pygame.key.get_pressed()
         dist = 1
         if key[pygame.K_LEFT]:
             self.rect.move(-1, 0)  
         if key[pygame.K_RIGHT]:
             self.rect.move(1, 0)          
         if key[pygame.K_UP]:
             self.rect.move(0, 1)
         if key[pygame.K_DOWN]:
             self.rect.move(0, -1)
           
    def draw(self, surface):
         snake.draw
