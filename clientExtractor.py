import json
import cv2 as cv
import base64
from util import *
from elasticsearch import Elasticsearch

tmp_file = "/tmp/katie.img"
client = Elasticsearch()
res = client.search(index="katie", doc_type="raw_cloud", body={"query": {"match_all": {}}, "size": 1} )
hits = res['hits']['hits']
detector = cv.ORB_create()

for hit in hits:
	# source = hit['_source']
	# source['imageBase64'] = "Katie Dwyer"
	# client.update(index='katie', doc_type="raw_cloud", body={"doc": source}, id=hit['_id'])
	 image64 = hit['_source']['imageBase64']
	 imgData = base64.b64decode(image64)

	 with open(tmp_file, 'wb') as f:
	 	f.write(imgData)

	 img = cv.imread(tmp_file, 0)
	 (keys, descs) = detector.detectAndCompute(img, None)
	 print Pair(keys[0], descs[0])
	 print Pairs(keys, descs)
	 # print descs
