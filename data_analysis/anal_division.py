def analDivision(x):
    dicList = dict()
    area01 = []
    area02 = []
    area03 = []
    area04 = []
    area05 = []
    area06 = []
    area07 = []
    area08 = []
    area09 = []
    area10 = []
    area11 = []
    area12 = []
    area13 = []
    area14 = []
    area15 = []
    area16 = []
    area17 = []
    area18 = []
    for j in range(len(x)):
        if x[j][2] == '서울':
            for i in range(0,1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area01.append(tag_split[k])
        elif x[j][2] == '인천':
            for i in range(0, 1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area02.append(tag_split[k])
        elif x[j][2] == '강원':
            for i in range(0, 1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area03.append(tag_split[k])
        elif x[j][2] == '경기':
            for i in range(0, 1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area04.append(tag_split[k])
        elif x[j][2] == '충북':
            for i in range(0, 1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area05.append(tag_split[k])
        elif x[j][2] == '충남':
            for i in range(0, 1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area06.append(tag_split[k])
        elif x[j][2] == '경남':
            for i in range(0, 1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area07.append(tag_split[k])
        elif x[j][2] == '경북':
            for i in range(0, 1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area08.append(tag_split[k])
        elif x[j][2] == '제주':
            for i in range(0, 1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area09.append(tag_split[k])
        elif x[j][2] == '전북':
            for i in range(0, 1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area10.append(tag_split[k])
        elif x[j][2] == '전남':
            for i in range(0, 1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area11.append(tag_split[k])
        elif x[j][2] == '울산':
            for i in range(0, 1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area12.append(tag_split[k])
        elif x[j][2] == '세종':
            for i in range(0, 1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area13.append(tag_split[k])
        elif x[j][2] == '부산':
            for i in range(0, 1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area14.append(tag_split[k])
        elif x[j][2] == '대전':
            for i in range(0, 1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area15.append(tag_split[k])
        elif x[j][2] == '광주':
            for i in range(0, 1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area16.append(tag_split[k])
        elif x[j][2] == '대구':
            for i in range(0, 1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area17.append(tag_split[k])
        else:
            for i in range(0, 1):
                tag_split = x[j][1].split(',')
                for k in range(len(tag_split)):
                    area18.append(tag_split[k])



    # 모든 지역의 구분 배열 만들기

    dicList = {'서울':area01,"인천":area02,"강원":area03,"경기":area04,"충북":area05,"충남":area06,"경남":area07,"경북":area08,"제주":area09,"전북":area10,"전남":area11,"울산":area12,"세종":area13,"부산":area14,
               "대전":area15,"광주":area16,"대구":area17,"이외":area18}

    return dicList