from data_analysis import mongodb_connection
from konlpy.tag import Okt
import collections
collection = mongodb_connection.mongodb_set()

pipeline = [
    {'$match': {'keyword':'예술강사', 'reference':'naver', 'save_date':{'$regex':'^2020-04-13'}}},
    {'$group': {'_id':{'content_date':'$content_date', 'location':'$location', 'tag': '$tag','content':'$content', 'reference':'$reference'}}},
    {'$limit': 100}
]

data = list(collection.aggregate(pipeline, allowDiskUse=True))
dup = []

print('가져온 데이터 개수', len(data))

for data2 in data:
    dup += list(data2.get('_id').get('tag'))

result = []
for result_data in collections.Counter(dup).most_common(10):
    result.append(list(result_data))
print(result)