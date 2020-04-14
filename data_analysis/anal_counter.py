from collections import Counter
import pandas as pd
from pandas import Series, DataFrame

def tagCnt(x):
    tagList = []
    area = []
    result = []
    areaList = ["서울","인천","강원","경기","충북","충남","경남","경북","제주","전북","전남","울산","세종","부산","대전","광주","대구","이외"]

    for i in range(len(areaList)):
        cntResult = {areaList[i]:Counter(x[areaList[i]]).most_common(10)}
        if not x[areaList[i]]:
            cntResult.keys()
        else:
            result.append(cntResult.get(areaList[i]))
            area.append(areaList[i])
    for j in range(len(result)):
        trans = list(result[j])

    result = pd.DataFrame(trans, columns=['HASH', 'COUNT'])
    result.set_index(result['HASH'], inplace=True)
    result.drop('HASH', axis=1)
    return result