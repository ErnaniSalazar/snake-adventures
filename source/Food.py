 class Food(GameObject):
	def __init__(self, score, hp=1, size, color, sprite):
		self.score=score
		self.hp=hp
    	super(). __init__(posInGrid, size, color, sprite) #call father constructor

class Enemy(Food):
	def __init__(self, size, score, color, sprite=None, hp=1):
		super().__init__(size, score, color, sprite, hp)

	def move(target):
		pass
 
