import json
import cv2 as cv
from elasticsearch import Elasticsearch

client = Elasticsearch()

# result = client.search(index='katie', q='date:"1412937000"')
# result = client.search(index='katie', q='match_all')

res = client.search(index="katie", doc_type="raw_cloud", body={"query": {"match_all": {}}, "size": 2} )

hits = res['hits']['hits']

for hit in hits:
	# source = hit['_source']
	# source['imageBase64'] = "Katie Dwyer"
	# client.update(index='katie', doc_type="raw_cloud", body={"doc": source}, id=hit['_id'])
	print hit