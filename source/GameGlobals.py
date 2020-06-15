import pygame
import random
from WallE import WallE
from Snake import Snake
from Snake import SnakePart
from Player import Player
from Food import Food
from Vector2 import Vector2
from Text import Text
from Enemy import Enemy
from Bullet import Bullet
from Scene import Scene
class SceneManager(object):
	def __init__(self, screenRef):
		self.screenRef = screenRef
		self.mainScene = Scene()
		self.homeScene = Scene()
		self.gameOverScene = Scene()
		self.bossScene = Scene()
		self.winScene = Scene()
		self.currScene = Scene()
	def initScenes(self):
		self.initHomeScene()
		self.initMainScene()
		self.initOverScene()
		self.initBossScene()
		self.initWinScene()
	def sceneLoad(self, scene):
		self.currScene = scene
		# breakpoint()
		self.currScene.start()
	def initHomeScene(self):	
		objects={}
		def start():
			# breakpoint()
			self.homeScene.objects["titleDisplay"] = Text(self.homeScene, Vector2(6, 70), Vector2(67, 200), pygame.Color(255, 255, 255), "Assets/Recreativos.otf","Snake Adventures")
			self.homeScene.objects["pressStartDisplay"] = Text(self.homeScene, Vector2(170, 300), Vector2(42, 200), pygame.Color(255, 255, 255), "Assets/Recreativos.otf", "PRESS SPACE BAR")

		def update():
			# breakpoint()
			self.homeScene.objects["titleDisplay"].draw(self.screenRef)
			self.homeScene.objects["pressStartDisplay"].draw(self.screenRef)
			# pygame.time.wait(500)
			# self.screenRef.fill((0, 0, 0))
			# titleDisplay.draw(self.screenRef)
			# pygame.time.wait(500)
			key = pygame.key.get_pressed()
			if key[pygame.K_SPACE]:
				self.sceneLoad(self.mainScene)
		self.homeScene = Scene(objects, start, update)
	def initMainScene(self):
		objects={}
		def start():
			worldGameObjects = []
			self.mainScene.objects["snake"] = Snake(self.mainScene, Vector2(449, 449), Vector2(30, 30), pygame.Color(200, 0, 0))
			self.mainScene.objects["player"] = Player(self.mainScene.objects["snake"], 0, Vector2(0, 0), atk=1, hp=10)
			food = Food(self.mainScene, Vector2(30*random.randint(2, 22) - 1, 30*random.randint(2, 22) - 1), 1, Vector2(30, 30), pygame.Color(0, 247, 0), None, hp=1)
			enemy1 = Enemy(self.mainScene, Vector2(30*random.randint(2, 22) - 1, 30*random.randint(2, 22) - 1), 0, Vector2(30, 30), pygame.Color(100, 0, 100), self.mainScene.objects["snake"].getHead(), atk=1, hp=2, speed=30)
			enemy2 = Enemy(self.mainScene, Vector2(30*random.randint(2, 22) - 1, 30*random.randint(2, 22) - 1), 0, Vector2(30, 30), pygame.Color(100, 0, 100), self.mainScene.objects["snake"].getHead(), atk=1, hp=2, speed=30)
			self.mainScene.objects["scoreDisplay"] = Text(self.mainScene, Vector2(70, 1), Vector2(28, 30), pygame.Color(0, 0, 0), "Assets/Recreativos.otf", "")
			worldGameObjects = [food]
			enemys = [enemy1, enemy2]
			worldGameObjects.extend(enemys)

			for i in range (0, 24):
			  topWallBlock = WallE(self.mainScene, Vector2((30*i)-1, -1), Vector2(30, 30), pygame.Color(0, 255, 255))
			  bottomWallBlock = WallE(self.mainScene, Vector2((30*i)+29, 689), Vector2(30, 30), pygame.Color(0, 255, 255))
			  leftWallBlock = WallE(self.mainScene, Vector2(-1, (30*i)-1), Vector2(30, 30), pygame.Color(0, 255, 255))
			  rightWallBlock = WallE(self.mainScene, Vector2(689 ,(30*i)+29), Vector2(30, 30), pygame.Color(0, 255, 255))
			  wall = [rightWallBlock, leftWallBlock, topWallBlock, bottomWallBlock]
			  worldGameObjects.extend(wall)

			objects["worldGameObjects"]=worldGameObjects
			self.mainScene.objects = objects
		def update():
			self.mainScene.objects["scoreDisplay"].setText('score: '+ str(self.mainScene.objects["player"].score)+'                  health: '+str(self.mainScene.objects["player"].hp))
			self.mainScene.objects["player"].handleKeys()
			self.mainScene.objects["player"].act()
			for gameObject in objects["worldGameObjects"]:
				gameObject.act()
				#check all colisions
				# breakpoint()
				if self.mainScene.objects["snake"].getHead().pos.equal(gameObject.pos):
					if gameObject.getType() == "Enemy" or gameObject.getType() == "Food" or gameObject.getType() == "Bullet":
						self.mainScene.objects["player"].getHit(gameObject.atk)
						gameObject.getHit(self.mainScene.objects["player"].atk)
						if gameObject.getType() == "Food":
							self.mainScene.objects["snake"].eat()
						if gameObject.hp==0:
							self.mainScene.objects["player"].score= self.mainScene.objects["player"].score+gameObject.score
					elif gameObject.getType() == "WallE":
						self.mainScene.objects["player"].hp = 0
				for otherGameObject in objects["worldGameObjects"]:
					if gameObject == otherGameObject:
						continue
					if gameObject.pos.equal(otherGameObject.pos):
						if gameObject.getType() == "WallE":
							if otherGameObject.getType() == "Enemy":
								otherGameObject.retreat()
							if otherGameObject.getType() == "Bullet":
								otherGameObject.hp = 0
						elif gameObject.getType() == "Bullet":
							if otherGameObject.getType() != "Food":
								gameObject.getHit(otherGameObject.atk)
								otherGameObject.getHit(gameObject.atk)
		    	#NPC respawn
				if gameObject.hp <= 0:	
					if gameObject.getType() == "Enemy" or gameObject.getType() == "Food":
						gameObject.pos = Vector2(30*random.randint(2, 22) - 1, 30*random.randint(2, 22) - 1)
						gameObject.hp = gameObject.initialHP
					elif gameObject.getType() == "Bullet":
						objects["worldGameObjects"].remove(gameObject)
				#Game Over
				if self.mainScene.objects["player"].hp <= 0:
					self.sceneLoad(self.gameOverScene)
				if self.mainScene.objects["player"].score >= 10:
					self.sceneLoad(self.bossScene)				
				gameObject.draw(self.screenRef)
			self.mainScene.objects["snake"].draw(self.screenRef)
			self.mainScene.objects["scoreDisplay"].draw(self.screenRef)
			pygame.time.wait(500)
		self.mainScene = Scene(objects, start, update)	
	def initBossScene(self):
		objects={}
		def start():
			worldGameObjects = []
			self.bossScene.objects["snake"] = Snake(self.bossScene, Vector2(449, 449), Vector2(30, 30), pygame.Color(200, 0, 0))
			self.bossScene.objects["player"] = Player(self.bossScene.objects["snake"], 0, Vector2(0, 0), atk=1, hp = self.mainScene.objects["player"].hp)
			food = Food(self.bossScene, Vector2(30*random.randint(2, 22) - 1, 30*random.randint(2, 22) - 1), 1, Vector2(30, 30), pygame.Color(0, 247, 0), None, hp=1)
			boss = Enemy(self.bossScene, Vector2(30*random.randint(2, 22) - 1, 30*random.randint(2, 22) - 1), 0, Vector2(30, 30), pygame.Color(10, 0, 10), self.bossScene.objects["snake"].getHead(), atk=1, hp=10, speed=30)
			self.bossScene.objects["boss"] = boss
			self.bossScene.objects["scoreDisplay"] = Text(self.bossScene, Vector2(70, 1), Vector2(28, 30), pygame.Color(0, 0, 0), "Assets/Recreativos.otf", "")
			worldGameObjects = [food, boss]
			
			for i in range (0, 24):
			  topWallBlock = WallE(self.bossScene, Vector2((30*i)-1, -1), Vector2(30, 30), pygame.Color(255, 0, 0))
			  bottomWallBlock = WallE(self.bossScene, Vector2((30*i)+29, 689), Vector2(30, 30), pygame.Color(255, 0, 0))
			  leftWallBlock = WallE(self.bossScene, Vector2(-1, (30*i)-1), Vector2(30, 30), pygame.Color(255, 0, 0))
			  rightWallBlock = WallE(self.bossScene, Vector2(689 ,(30*i)+29), Vector2(30, 30), pygame.Color(255, 0, 0))
			  wall = [rightWallBlock, leftWallBlock, topWallBlock, bottomWallBlock]
			  worldGameObjects.extend(wall)

			objects["worldGameObjects"]=worldGameObjects
			self.bossScene.objects = objects
		def update():
			self.bossScene.objects["scoreDisplay"].setText('score: '+ str(self.bossScene.objects["player"].score)+'                  health: '+str(self.bossScene.objects["player"].hp))
			self.bossScene.objects["player"].handleKeys()
			self.bossScene.objects["player"].act()
			for gameObject in objects["worldGameObjects"]:
				gameObject.act()
				#check all colisions
				# breakpoint()
				if self.bossScene.objects["snake"].getHead().pos.equal(gameObject.pos):
					if gameObject.getType() == "Enemy" or gameObject.getType() == "Food" or gameObject.getType() == "Bullet":
						self.bossScene.objects["player"].getHit(gameObject.atk)
						gameObject.getHit(self.bossScene.objects["player"].atk)
						if gameObject.getType() == "Food":
							self.bossScene.objects["snake"].eat()
						if gameObject.hp==0:
							self.bossScene.objects["player"].score= self.bossScene.objects["player"].score+gameObject.score
					elif gameObject.getType() == "WallE":
						self.bossScene.objects["player"].hp = 0
				for otherGameObject in objects["worldGameObjects"]:
					if gameObject == otherGameObject:
						continue
					if gameObject.pos.equal(otherGameObject.pos):
						if gameObject.getType() == "WallE":
							if otherGameObject.getType() == "Enemy":
								otherGameObject.retreat()
							if otherGameObject.getType() == "Bullet":
								otherGameObject.hp = 0
						elif gameObject.getType() == "Bullet":
							if otherGameObject.getType() != "Food":
								gameObject.getHit(otherGameObject.atk)
								otherGameObject.getHit(gameObject.atk)
		    	#NPC respawn
				if gameObject.hp <= 0:
					if gameObject.getType() == "Food":
						gameObject.pos = Vector2(30*random.randint(2, 22) - 1, 30*random.randint(2, 22) - 1)
						gameObject.hp = gameObject.initialHP
					elif gameObject.getType() == "Bullet":
						objects["worldGameObjects"].remove(gameObject)
				#Game Over
				if self.bossScene.objects["player"].hp <= 0:
					self.sceneLoad(self.gameOverScene)	
				if self.bossScene.objects["boss"].hp <= 0:
					self.sceneLoad(self.winScene)			
				gameObject.draw(self.screenRef)
			self.bossScene.objects["snake"].draw(self.screenRef)
			self.bossScene.objects["scoreDisplay"].draw(self.screenRef)
			pygame.time.wait(500)
		self.bossScene = Scene(objects, start, update)	
	def initOverScene(self):
		objects={}	
		def start():
			self.gameOverScene.objects["titleDisplay"] = Text(self.homeScene, Vector2(180, 70), Vector2(67, 200), pygame.Color(255, 0, 0), "Assets/Recreativos.otf","Game Over")
			# self.gameOverScene.objects["killDisplay"] = Text(self.homeScene, Vector2(180, 500), Vector2(67, 200), pygame.Color(255, 0, 0), "Assets/Recreativos.otf","Player waskilled by" + self.mainScene.objects.gameObject.getType())
			self.gameOverScene.objects["pressStartDisplay"] = Text(self.homeScene, Vector2(170, 300), Vector2(42, 200), pygame.Color(255, 255, 255), "Assets/Recreativos.otf", "PRESS SPACE BAR")
		def update():
			self.gameOverScene.objects["titleDisplay"].draw(self.screenRef)
			self.gameOverScene.objects["pressStartDisplay"].draw(self.screenRef)
			# pygame.time.wait(500)
			# self.screenRef.fill((0, 0, 0))
			# titleDisplay.draw(self.screenRef)
			# pygame.time.wait(500)
			key = pygame.key.get_pressed()
			if key[pygame.K_SPACE]:
				self.sceneLoad(self.homeScene)
		self.gameOverScene = Scene(objects, start, update)

	def initWinScene(self):
		objects={}	
		def start():
			self.winScene.objects["titleDisplay"] = Text(self.winScene, Vector2(180, 70), Vector2(67, 200), pygame.Color(255, 255, 0), "Assets/Recreativos.otf","You Won")
			self.winScene.objects["pressStartDisplay"] = Text(self.winScene, Vector2(170, 300), Vector2(42, 200), pygame.Color(255, 255, 255), "Assets/Recreativos.otf", "PRESS SPACE BAR")
		def update():
			self.winScene.objects["titleDisplay"].draw(self.screenRef)
			self.winScene.objects["pressStartDisplay"].draw(self.screenRef)
			# pygame.time.wait(500)
			# self.screenRef.fill((0, 0, 0))
			# titleDisplay.draw(self.screenRef)
			# pygame.time.wait(500)
			key = pygame.key.get_pressed()
			if key[pygame.K_SPACE]:
				self.sceneLoad(self.homeScene)
		self.winScene = Scene(objects, start, update)