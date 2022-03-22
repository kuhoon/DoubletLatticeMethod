import os

from sol103 import *

nodesFileName = "nodes.dat"
lumpFileName = "mass_lump.dat"
concFileName = "mass_conc.dat"
elementsFileName = "elements.dat"
model = BDF()

create103(model, nodesFileName, lumpFileName, concFileName, elementsFileName ) #sol145 파일 만들기

bdf_filename_out = os.path.join('datFiles/sol103_OUT3.bdf')
model.write_bdf(bdf_filename_out, enddata=True)
print(bdf_filename_out)

print('----------------------------------------------------------------------------------------------------')
