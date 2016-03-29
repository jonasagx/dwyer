import sys
import glob
from util import RawImage
from elasticsearch import Elasticsearch

client = Elasticsearch()

folder = sys.argv[1]

if(folder[-1] != '/'):
	folder += '/'

print "Processing pictures in " + folder

for key, photoPath in enumerate(glob.glob(folder + '*.jpg')):
	img = RawImage(photoPath)
	res = client.index(index="katie", doc_type='raw_cloud', body=img.export(), id=key)
	print photoPath