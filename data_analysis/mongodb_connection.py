# mongodb 설정
def mongodb_set():
    import pymongo
    # db 연동
    conn = pymongo.MongoClient('localhost', 27017)  # mongoDB에서 port를 변경하지 않았으면 기본값인 27017
    db = conn.get_database('crawling')  # 데이터베이스 선택 데이터베이스가 없어도 자동으로 만들어진다
    collection = db.get_collection('data')  # 테이블 선택 데이터베이스가 없어도 자동으로 만들어진다
    return collection