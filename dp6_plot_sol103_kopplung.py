import os
import numpy as np
import matplotlib.pyplot as plt
from pyNastran.op2.op2 import read_op2
import matplotlib.patches as mpatches
import pandas as pd

cw_path = os.path.abspath(os.getcwd())
model_path = os.path.join(cw_path, 'MA_final/DP6/sol103/kopplung/sol103_dp6_m1_coupled.op2')

sol103 = read_op2(model_path, debug=False, build_dataframe = True, mode = 'msc')
print(sol103.get_op2_stats(short=True))
# sol103.eigenvectors[1]
# sol103.eigenvectors[1].modes
# sol103.eigenvectors[1].mode_cycles
x_data = np.delete(sol103.eigenvectors[1].modes,[1, 4, 9, 10])
y_data = np.delete(sol103.eigenvectors[1].mode_cycles, [1, 4, 9, 10])
colors = ['r'] * len(x_data)  # 기본 색상은 파란색으로 설정

plt.bar(np.arange(len(x_data)), y_data, width=0.3, color=colors)
plt.xticks(np.arange(len(x_data)), x_data)
plt.xlabel('Mode')
plt.ylabel('Mode Frequency [Hz]')
plt.title('SOL103_dp6_M1 Mode Frequency')
plt.grid()

for i in range(len(x_data)):
    plt.text(i, y_data[i], round(y_data[i], 2), ha='center', va='bottom')

plt.savefig('MA_final/DP6/sol103/kopplung/sol103_dp6_m1_coupled.png')
plt.show()