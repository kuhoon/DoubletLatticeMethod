from pyNastran.op2.op2 import OP2
import pandas as pd
pd.set_option('display.precision',1)
op2=OP2()
op2.read_op2('sol103_adddlm_f025_coupled.op2')

# print(op2.get_op2_stats())

print(op2.eigenvectors[1].data_frame)