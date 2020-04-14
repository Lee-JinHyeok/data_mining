from django.shortcuts import render
from konlpy.tag import Okt
import collections

def home(request):
    collection = mongodb_set()

    pipeline = [
        {'$match': {'keyword': '예술강사', 'reference': 'naver', 'save_date': {'$regex': '^2020-04-13'}}},
        {'$group': {
            '_id': {'content_date': '$content_date', 'location': '$location', 'tag': '$tag', 'content': '$content',
                    'reference': '$reference'}}},
        {'$limit': 1000}
    ]

    data = list(collection.aggregate(pipeline, allowDiskUse=True))
    okt = Okt()
    dup = []
    dup2 = []
    # 11 sec
    for data2 in data:
        dup += (list(okt.nouns(data2.get('_id').get('content'))))

    # 0.02 sec
    for data3 in dup:
        if len(data3) >= 2:
            dup2.append(data3)

    # print(len(data))
    # print(dup)
    # print(len(dup))
    # print(type(dup))

    # print(dup2)
    # print(len(dup2))
    # print(type(dup2))
    # print(collections.Counter(dup2).most_common(10))

    result = []
    for result_data in collections.Counter(dup2).most_common(10):
        result.append(list(result_data))

    # print(result)

    return render(request, 'home.html',{'result':result})

# mongodb 설정
def mongodb_set():
    import pymongo
    # db 연동
    conn = pymongo.MongoClient('localhost', 27017)  # mongoDB에서 port를 변경하지 않았으면 기본값인 27017
    db = conn.get_database('crawling')  # 데이터베이스 선택 데이터베이스가 없어도 자동으로 만들어진다
    collection = db.get_collection('data')  # 테이블 선택 데이터베이스가 없어도 자동으로 만들어진다
    return collection