# ctrl+d = 해당 줄 복사, ctrl+/ = 주석처리, shift + d / = 여러줄, ctrl shift alt j = 전체변환
from pyNastran.bdf.bdf import BDF, CaseControlDeck


def create145(model, rfListFileName, sectionFileName, concFileName, nodesFileName):
    idSectList = []
    xLeList = []
    yLeList = []
    zLeList = []
    cList = []
    machValueList = []
    rrfValueList = []
    idList = []
    v3ValueList = []

    ARfloat = 9.16

    # open sections.dat file_Wing
    with open(sectionFileName) as datFile:
        sectValueList = [data.split() for data in datFile]
        del sectValueList[0]  # 0번 행을 지워라
        for v in sectValueList:
            idSectList.append(v[0])
            xLeList.append(v[1])  # list 원소 추가
            yLeList.append(v[2])
            zLeList.append(v[3])
            cList.append(v[4])

    eId = 101
    ptList = []  # [ [], [], [] ]
    # insert model.add_point(id_no, x, y, z)
    for x, y, z, c in zip(xLeList, yLeList, zLeList, cList):
        model.add_point(eId, [float(x), float(y), float(z)])
        ptList.append([float(x), float(y), float(z)])
        eId = eId + 1
        model.add_point(eId, [float(x) + float(c), float(y), float(z)])
        eId = eId + 1

    eId2 = 100001
    nCh = 5  # 나스트란 기본설정. chord 박스 5개
    b1Span = float(yLeList[1]) - float(yLeList[0])  # span 길이를 균일하게 하기위한.
    for i in range(len(idSectList) - 1):  # leg, list = 길이, 원소의 갯수
        bSpan = round((float(yLeList[i + 1]) - float(yLeList[i])) * nCh / b1Span)  # round 반올림
        model.add_paero1(eId2)
        model.add_caero1(eId2, eId2, 1, ptList[i], float(cList[i]), ptList[i + 1], float(cList[i + 1]), 0, bSpan, 0,
                         nCh, 0)
        eId2 += 1000
    # 여기서 하고싶은것. 섹션 아이디는 n개이고, 여기서 생성되는 면은 n-1개이므로 섹션아이디-1 = n-1개로 표현
    # ptList는 [ [], [], [] ]형태이므로, float 불가. cList는 리스트-플롯 바로적용

    with open(nodesFileName) as datFile:
        nodeValueList = [data.split() for data in datFile]
        del nodeValueList[0]  # 0번 행을 지워라
        for v in nodeValueList:
            idList.append(int(v[0]))  # list 원소 추가

    with open(concFileName) as datFile:
        massValueList = [data.split() for data in datFile]
        del massValueList[0]
        for v in massValueList:
            idList.append(int(v[0]))

    model.add_set1(1, idList)

    model.add_aero(1, 1984, 1.228E-12, 0)  # velocity, aerodynamic chord, density scal, coord
    model.add_aeros(1984, 17174, 3.227E7 / 2, 0, 0)  # half span model => half area

    with open(rfListFileName) as datFile:
        rfValueList = [data.split() for data in datFile]
        del rfValueList[0]  # 0번 행을 지워라
        print(rfValueList))
        for v in rfValueList:
            machValueList.append(v[0])  # list 원소 추가
            rrfValueList.append(v[1])
            v3ValueList.append(v[4])

    for m, rf, v3 in zip(machValueList, rrfValueList, v3ValueList):
        model.add_mkaero2([float(m)], [float(rf)])

    model.add_spline4(1, 102001, 1, 1, '', 'FPS', 'BOTH', 10, 10)

    # model.add_aelist(1, 10000 ) # 그물망 수(우리가 설정한. 예를 들어 33x5면 165개

    seaAD = 1.225E-12
    cruiseAD = 8.170E-13
    model.add_flfact(1, [float(cruiseAD/seaAD)])
    model.add_flfact(2, [float(0.0)])
    model.add_flfact(3, [float(v3)])

    model.add_flutter(1, 'PK', 1, 2, 3, 'L', None, None, float(1E-3))
    model.sol = 145
