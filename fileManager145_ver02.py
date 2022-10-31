import os
from pyNastran.bdf.bdf import *
import numpy as np

nodesFileName = "Ref_220425/data_nodes.dat"
elementsFileName = "Ref_220425/data_elements.dat"
sectionFileName = "Ref_220425/data_planform.dat"
machFileName = "datFiles/6_machNum.dat"
rrfFileName = "datFiles/7_redRF.dat"
v3FileName = "datfiles/8_v3.dat"

model = BDF()

idList = []
xValueList = []
yValueList = []
zValueList = []
mLump = []
pbeamList = []
areaList = []
i1List = []
i2List = []
jList = []
idFromList = []
idToList = []

# ===== special for sol145
idSectList = []
xLeList = []
yLeList = []
zLeList = []
cList = []
machValueList = []
rrfValueList = []
v3ValueList = []
bSpanList = []
aelistList = []
eId = 201
ptList = []  # [ [], [], [] ]

E = 72397.0
G = 27000.0
nu = 0.32
rho = 0.0000000000000001
mat = model.add_mat1(1, E, G, nu, rho)

# ====================================================================
# =========================== OPEN FILES =============================
# ====================================================================

n = int(input("Bitte gebe eine Beladungszustände mit 25, 50 und 100% ein : "))
if n == 25 :
    with open("Ref_220425/masses_f025/data_masses.dat") as datFile:
        lumpValueList = [data.split() for data in datFile]
        del lumpValueList[0]
        for v in lumpValueList:
            conm1List.append(v[0])  # conm1list 1-100
            mass.append(v[2])
            iYy.append(v[3])
            firstMoment.append(v[4])
elif n == 50 :
    with open("Ref_220425/masses_f050/data_masses.dat") as datFile:
        lumpValueList = [data.split() for data in datFile]
        del lumpValueList[0]
        for v in lumpValueList:
            conm1List.append(v[0])  # conm1list 1-100
            mass.append(v[2])
            iYy.append(v[3])
            firstMoment.append(v[4])
elif n == 100 :
    with open("Ref_220425/masses_f100/data_masses.dat") as datFile:
        lumpValueList = [data.split() for data in datFile]
        del lumpValueList[0]
        for v in lumpValueList:
            conm1List.append(v[0])  # conm1list 1-100
            mass.append(v[2])
            iYy.append(v[3])
            firstMoment.append(v[4])

# open node.dat file_Wing
with open("Ref_220425/data_nodes.dat") as datFile:
    nodeValueList = [data.split() for data in datFile]
    del nodeValueList[0] # delete line 0
    for v in nodeValueList:
        idList.append(v[0]) # add list element
        xValueList.append(v[1])
        yValueList.append(v[2])
        zValueList.append(v[3])

# open mass_lump.dat file_Wing
with open("Ref_220425/data_lump_mass.dat") as datFile:
    lumpValueList1 = [data.split() for data in datFile]
    del lumpValueList1[0]
    for v in lumpValueList1:
        conm2List.append(v[0])
        mLump.append(v[2])

# open elements.dat file_pbeam
with open("Ref_220425/data_elements.dat") as datFile:
    elementValueList = [data.split() for data in datFile]
    del elementValueList[0]
    for v in elementValueList:
        pbeamList.append(v[0])
        idFromList.append(v[1])
        idToList.append(v[2])
        areaList.append(v[3])
        i1List.append(v[4])
        i2List.append(v[5])
        jList.append(v[7])

# <================ special for sol145 ===================>
# open 5_sections.dat file_Wing
with open(sectionFileName) as datFile:
    sectValueList = [data.split() for data in datFile]
    del sectValueList[0]  # 0번 행을 지워라
    for v in sectValueList:
        idSectList.append(v[0])
        xLeList.append(v[1])  # list 원소 추가
        yLeList.append(v[2])
        zLeList.append(v[3])
        cList.append(v[4])

# open 6_machNum.dat file
with open(machFileName) as datFile:
    tempList = [data.split() for data in datFile]
    for t in tempList:
        machValueList.append(float(t[0]))

# open 7_redRF.dat file
with open(rrfFileName) as datFile:
    tempList = [data.split() for data in datFile]
    for t in tempList:
        rrfValueList.append(float(t[0]))

# open 8_v3.dat file
with open(v3FileName) as datFile:
    tempList = [data.split() for data in datFile]
    for t in tempList:
        v3ValueList.append(float(t[0]) * -1)

# ====================================================================
# ========================= ADD ATTRIBUTES ===========================
# ====================================================================

# start model number
model.sol = 145  # start=103

# case control
spc_id = 50
cc = CaseControlDeck([
    'SUBCASE 1',
    'SUBTITLE = Default',
    'METHOD = 10', # MODIFIED GIVENS METHOD OF REAL EIGENVALUE EXTRACTION
    'SPC = %s' % spc_id, # WING ROOT DEFLECTIONS AND PLATE IN-PLANE ROTATIONS FIXED
    'VECTOR(SORT1,REAL)=ALL',
    'SPCFORCES(SORT1, REAL) = ALL',
    'BEGIN BULK',
    'ANALYSIS = FLUTTER',
    'AESYMXY = Asymmetric',
    'AESYMXZ = Symmetric',
    'FMETHOD = 1'
])
model.case_control_deck = cc
model.validate()


# model.add_mat1(1, E, G, nu, rho)

model.add_param('POST', [0])
model.add_param('PRTMAXIM', ['YES'])
model.add_param('SNORM', [20.0])
model.add_param('WTMASS', [1.0])  # default = 1.0
model.add_param('Aunit', [1.0])

# # insert model.add_grid(id_no, x, y, z)
for i, x, y, z in zip(idList, xValueList, yValueList, zValueList):
    model.add_grid(int(i), [float(x), float(y), float(z)])

# insert model.add_pbeam(id_pbeam, mid, x/xb, so, area, i1, i2, i12, j)
for p, a, i1, i2, j in zip(pbeamList, areaList, i1List, i2List, jList):
    model.add_pbeam(int(p), 1, [0.0], ['YES'], [float(a)], [float(i1)], [float(i2)], [0], [float(j)])

# insert model.add_cbeam
for p, idFrom, idTo in zip(pbeamList, idFromList, idToList):
    model.add_cbeam(int(p), int(p), [int(idFrom), int(idTo)], [], 100)

# insert model.add_spc1, spcadd
model.add_spc1(spc_id, '123456', [1])
model.add_spcadd(1, spc_id)

# insert model.add_rbe2
model.add_rbe2(51, 8, '123456', [100])
model.add_rbe2(52, 8, '123456', [101])

# insert model.add_eigrl
eigrl = model.add_eigrl(10, nd=10, msglvl=0) # how many want to mode
# model.add_eigrl(int(1), '', '', 10, 0)  # how many want to mode

# <=========== sol 145 ===============>
# insert model.add_point(id_no, x, y, z)
for x, y, z, c in zip(xLeList, yLeList, zLeList, cList):
    model.add_point(eId, [float(x), float(y), float(z)])
    ptList.append([float(x), float(y), float(z)])
    eId = eId + 1
    model.add_point(eId, [float(x) + float(c), float(y), float(z)])
    eId = eId + 1

# insert model.add_paero1, caero1
eId2 = 103001
nCh = 5  # 나스트란 기본설정. chord 박스 5개
b1Span = float(yLeList[1]) - float(yLeList[0])  # span 길이를 균일하게 하기위한.
for i in range(len(idSectList) - 1):  # leg, list = 길이, 원소의 갯수
    bSpan = round((float(yLeList[i + 1]) - float(yLeList[i])) * nCh / b1Span)  # round 반올림
    model.add_paero1(eId2)
    model.add_caero1(eId2, eId2, 1, np.array(ptList[i], float), float(cList[i]), np.array(ptList[i + 1], float), float(cList[i + 1]), 0, bSpan, 0, nCh, 0)
    eId2 += 1000
    bSpanList.append(bSpan)

# insert model.add_set1, aero, aeros
model.add_set1(1, idList)

model.add_aero(float(1.0), float(1984.0), float(1.228E-12), 0)  # velocity, aerodynamic chord, density scal, coord
model.add_aeros(float(1984.0), float(17174.0), float(3.227E7 / 2), 0, 0)  # half span model => half area

# insert model.add_mkaero2
# for m in machValueList:
#     tempMachMesh = [float(m)]
#     for i in range(len(rrfValueList)-1):
#         tempMachMesh.append(None)
#     model.add_mkaero2(tempMachMesh, rrfValueList)
for m in machValueList:
    for rf in rrfValueList:
        model.add_mkaero2([m], [rf])

# insert model.add_spline4
model.add_spline4(int(1), int(105001), int(1), int(1), float(), 'FPS', 'BOTH', int(10), int(10))

# manage aelist
eId2 = eId2 - (1000 * len(bSpanList))
for i in range(len(bSpanList)):
    for b in range(bSpanList[i] * 5):
        aelistList.append(eId2 + b)
    eId2 += 1000


model.add_aelist(1, aelistList)  # 그물망 수(우리가 설정한. 예를 들어 33x5면 165개
# manage flfact
seaAD = 1.225E-12
cruiseAD = 8.170E-13
model.add_flfact(1, [float(cruiseAD/seaAD)])
model.add_flfact(2, [float(0.0)])
model.add_flfact(3, v3ValueList)



# insert model.add_flutter
model.add_flutter(1, 'PK', 1, 2, 3, 'L', None, None, float(1E-3))

# write bdf file
model.validate()
bdf145_filename_out = os.path.join('sol145_caero1.bdf')
model.write_bdf(bdf145_filename_out, enddata=True)
print(bdf145_filename_out)
print("====> write bdf file success!")
