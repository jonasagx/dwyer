import re
import os
import json
import time
import json
import datetime
import numpy as np

class RawImage:
	"""docstring for image"""

	datePattern = "%Y%m%d%H%M"
	datePartternExtract = '\d{11}[0-9]'

	def __init__(self, imagePath):
		self.imagePath = imagePath
		self._loadImage()
		self.base64 = self.toBase64()

	def _loadImage(self):
		fileInfo = os.stat(self.imagePath)
		self.image = open(self.imagePath, "rb")

	def toBase64(self):
		with self.image as i:
		    data = i.read()
		    return data.encode("base64")
	
	def getBase64(self):
		return self.base64

	def getTimestamp(self):
		dataString = re.search(self.datePartternExtract, self.imagePath).group(0)
		date = datetime.datetime.strptime(dataString, self.datePattern).timetuple()
		return int(time.mktime(date))

	def _getDict(self):
		return { 
			"date": str(self.getTimestamp()),
			"imageBase64": self.getBase64()
		}

	def __str__(self):
		return json.dumps(self._getDict())
		# return self.getBase64()

	def export(self):
		return self._getDict()

class Pair:
	def __init__(self, keyPoint, descriptor):
		self.keyPoint = keyPoint
		self.descriptor = descriptor

	def getDict(self):
		return {
			'pt': list(self.keyPoint.pt), 
			'angle': self.keyPoint.angle, 
			'octave': self.keyPoint.octave, 
			'class_id': self.keyPoint.class_id, 
			'response': self.keyPoint.response, 
			'size': self.keyPoint.size,	
			'descriptor': self.descriptor.tolist()
		}

	def jsonify(self):
		return self.getDict()

	def __str__(self):
		return json.dumps(self.getDict())

class Pairs:
	def __init__(self, keys, descs):
		self.pairs = []
		for k, d in zip(keys, descs):
			self.pairs.append(Pair(k, d))

	def add(self, pair):
		self.pairs.append(pair)

	def get(self):
		return self.pairs

	def jsonify(self):
		return {
			'list': self.pairs
		}

	def __str__(self):
		return json.dumps(self.jsonify())
	# 	# str = ''
	# 	# for pair in self.pairs:
	# 	# 	str += pair.__str__()
	# 	# return str