class KeyPoint:
	def __init__(self, keyPoint):
		self.keyPoint = keyPoint

	def get(self):
		return {
			'pt': list(self.keyPoint.pt), 
			'angle': self.keyPoint.angle, 
			'octave': self.keyPoint.octave, 
			'class_id': self.keyPoint.class_id, 
			'response': self.keyPoint.response, 
			'size': self.keyPoint.size
		}

	def __str__(self):
		return self.get().__str__()