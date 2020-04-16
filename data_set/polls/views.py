from django.shortcuts import render
from konlpy.tag import Okt
import collections

def home(request):
    # 딕셔너리(map) 선언
    result = {}
    # result['tag']태그 데이터
    result['tag'] = tag_data()
    # result['content']콘텐츠 데이터
    result['content'] = content_data()
    print(result)
    return render(request, 'home.html',{'result':result})


def tag_data():
    collection = mongodb_set()

    pipeline = [
        {'$match': {'keyword': '예술강사', 'reference': 'naver', 'save_date': {'$regex': '^2020-04-13'}}},
        {'$group': {
            '_id': {'content_date': '$content_date', 'location': '$location', 'tag': '$tag', 'content': '$content',
                    'reference': '$reference'}}},
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
    return  result

def content_data():
    # 데이터베이스 연결
    collection = mongodb_set()
    # 데이터베이스에서 가져올 데이터
    pipeline = [
        {'$match': {'keyword': '예술강사', 'reference': 'naver', 'save_date': {'$regex': '^2020-04-13'}}},  # 조건부
        {'$group': {
            '_id': {'content_date': '$content_date', 'location': '$location', 'tag': '$tag', 'content': '$content',
                    'reference': '$reference'}}},  # 중복 검사
        {'$limit': 100}  # 제한 개수 설정
    ]
    # 가져올 데이터 data에 저장
    data = list(collection.aggregate(pipeline, allowDiskUse=True))

    # 11 sec
    dup_content = []
    # db에서 가져온 데이터 중 content만 단어 빈도수 정렬
    # 단어 빈도수 찾아주는 API
    okt = Okt()
    for sample_data in data:
        dup_content += (list(okt.nouns(sample_data.get('_id').get('content'))))

    # 0.02 sec
    dup2_content = []
    # 정렬한 단어중 1글자면 빼고 저장
    for sample_data in dup_content:
        if len(sample_data) >= 2:
            dup2_content.append(sample_data)

    # 데이터 결과 확인
    # print('가져온 데이터 개수', len(data))
    # print('dup_content의 길이', len(dup_content),'타입', type(dup_content),'값',dup_content)
    # print('dup2_content 길이', len(dup2_content),'타입', type(dup2_content),'값',dup2_content)
    # print(collections.Counter(dup2_content).most_common(10))

    # 단어 빈도수 많은 순으로 10개 가져와 result에 리스트 타입으로 저장
    result = []
    for result_data in collections.Counter(dup2_content).most_common(10):
        result.append(list(result_data))
    return  result

# mongodb 설정
def mongodb_set():
    import pymongo
    # db 연동
    conn = pymongo.MongoClient('localhost', 27017)  # mongoDB에서 port를 변경하지 않았으면 기본값인 27017
    db = conn.get_database('crawling')  # 데이터베이스 선택 데이터베이스가 없어도 자동으로 만들어진다
    collection = db.get_collection('data')  # 테이블 선택 데이터베이스가 없어도 자동으로 만들어진다
    return collection