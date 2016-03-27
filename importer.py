import sys
import glob
import base64
from util import RawImage
from elasticsearch import Elasticsearch

client = Elasticsearch()

folder = sys.argv[1]

if(folder[-1] != '/'):
	folder += '/'

print "Processing pictures in " + folder

for photoPath in glob.glob(folder + '*.jpg'):
	i = RawImage(photoPath)
	res = client.index(index="katie", doc_type='cloud', id=i.getTimestamp(), body=i.export())
	print photoPath