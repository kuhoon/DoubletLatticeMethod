import os

from sol103 import *
from sol145 import *

nodesFileName = "datFiles/nodes.dat"
lumpFileName = "datFiles/mass_lump.dat"
concFileName = "datFiles/mass_conc.dat"
elementsFileName = "datFiles/elements.dat"

model103 = BDF()
create103(model103, nodesFileName, lumpFileName, concFileName, elementsFileName) #sol103 파일 만들기

bdf103_filename_out = os.path.join('sol103_OUT3.bdf')
model103.write_bdf(bdf103_filename_out, enddata=True)
print(bdf103_filename_out)

print('----------------------------------------------------------------------------------------------------')

model145 = BDF()
create145(model145, rfListFileName="datFiles/rfList.dat", sectionFileName="datFiles/sections.dat", concFileName="datFiles/mass_conc.dat", nodesFileName ="datFiles/nodes.dat")
bdf145_filename_out = os.path.join('sol145_OUT3.bdf')
model145.write_bdf(bdf145_filename_out, enddata=True)
print(bdf145_filename_out)

print('----------------------------------------------------------------------------------------------------')


