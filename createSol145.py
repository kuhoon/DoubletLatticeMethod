import os

from sol145 import *

rfListFileName = "datFiles/rfList.dat"
sectionFileName = "datFiles/sections.dat"
model = BDF()
create145(model, rfListFileName, sectionFileName ) #sol145 파일 만들기

bdf_filename_out = os.path.join('sol145_OUT3.bdf')
model.write_bdf(bdf_filename_out, enddata=True)
print(bdf_filename_out)

print('----------------------------------------------------------------------------------------------------')
