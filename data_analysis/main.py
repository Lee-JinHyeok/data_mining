from data_analysis import mongodb_connection
from konlpy.tag import Okt
import collections
collection = mongodb_connection.mongodb_set()

pipeline = [
    {'$match': {'keyword':'예술강사','reference':'naver', 'save_date':{'$regex':'^2020-04-13'}}},
    {'$group': {'_id':{'content_date':'$content_date', 'location':'$location', 'tag': '$tag','content':'$content', 'reference':'$reference'}}},
    {'$limit': 1000}
]

data = list(collection.aggregate(pipeline, allowDiskUse=True))
okt = Okt()
dup = []
dup2 = []
# 11 sec
for data2 in data:
    dup += (list(okt.nouns(data2.get('_id').get('content'))))

#0.02 sec
for data3 in dup:
    if len(data3) >= 2:
        dup2.append(data3)

print(len(data))
print(dup)
print(len(dup))
print(type(dup))

print(dup2)
print(len(dup2))
print(type(dup2))
print(collections.Counter(dup2).most_common(10))

result = []
for result_data in collections.Counter(dup2).most_common(10):
    result.append(list(result_data))

print(result)
print(result[0])
print(result[1])
print(result[2])
print(type(result[0]))