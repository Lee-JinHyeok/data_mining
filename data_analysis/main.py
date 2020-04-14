from data_analysis import mongodb_connection
from konlpy.tag import Okt
collection = mongodb_connection.mongodb_set()

pipeline = [
    {'$match': {'keyword':'예술강사','reference':'naver', 'save_date':{'$regex':'^2020-04-14'}}},
    {'$group': {'_id':{'content_date':'$content_date', 'location':'$location', 'tag': '$tag','content':'$content', 'reference':'$reference','save_date':'$save_date'}}},
    {'$limit': 1000}
]

data = list(collection.aggregate(pipeline, allowDiskUse=True))
okt = Okt()
dup = []
dup2 = []
# 11 sec
for data2 in data:
    dup += (list(okt.nouns(data2.get('_id').get('content'))))
    print(data2.get('_id').get('save_date'))
    print(data2.get('_id').get('reference'))

#0.02 sec
for data3 in dup:
    if len(data3) >= 2:
        dup2.append(data3)

print(len(data))
print(dup)
print(len(dup))
print(dup2)
print(len(dup2))
# 여긴 테스트 zjalt