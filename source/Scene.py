class Scene(object):
	def __init__(self, objects={}, start={}, update={}): 
		self.objects = objects
		self.start = start
		self.update = update