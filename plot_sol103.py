import os
import numpy as np
import matplotlib.pyplot as plt
from pyNastran.op2.op2 import read_op2
import matplotlib.patches as mpatches
import pandas as pd

cw_path = os.path.abspath(os.getcwd())
model_path = os.path.join(cw_path, 'MA_final/referenz/sol103/ungekoppelt/sol103_100_uncoupled.op2')

sol103 = read_op2(model_path, debug=False, build_dataframe = True, mode = 'msc')
print(sol103.get_op2_stats(short=True))
# sol103.eigenvectors[1]
# sol103.eigenvectors[1].modes
# sol103.eigenvectors[1].mode_cycles
x_data = np.delete(sol103.eigenvectors[1].modes,[1, 4, 8, 9])
y_data = np.delete(sol103.eigenvectors[1].mode_cycles, [1, 4, 8, 9])
colors = ['r'] * len(x_data)  # 기본 색상은 파란색으로 설정
colors[0] = 'b'  # 1번 요소 막대는 빨간색으로 변경
colors[1] = 'b'  # 1번 요소 막대는 빨간색으로 변경
colors[2] = 'g'  # 1번 요소 막대는 빨간색으로 변경
colors[3] = 'b'  # 6번 요소 막대는 빨간색으로 변경
colors[4] = 'g'  # 6번 요소 막대는 빨간색으로 변경
colors[5] = 'g'  # 6번 요소 막대는 빨간색으로 변경
colors[6] = 'b'  # 6번 요소 막대는 빨간색으로 변경
# colors[7] = 'g'  # 6번 요소 막대는 빨간색으로 변경
# plt.bar(np.arange(len(x_data)), y_data, width=0.3, color='g') %모든색을 g로 통일할때
plt.bar(np.arange(len(x_data)), y_data, width=0.3, color=colors)
plt.xticks(np.arange(len(x_data)), x_data)
plt.xlabel('Mode')
plt.ylabel('Mode Frequency [Hz]')
plt.title('SOL103_100 Mode Frequency')
plt.grid()

for i in range(len(x_data)):
    plt.text(i, y_data[i], round(y_data[i], 2), ha='center', va='bottom')

blue_patch = mpatches.Patch(color='b', label='Biegung')
red_patch = mpatches.Patch(color='r', label='Torsion')
green_patch = mpatches.Patch(color='g', label='T+B')
plt.legend(handles=[blue_patch, red_patch, green_patch])

plt.savefig('MA_final/referenz/sol103/ungekoppelt/sol103_100_uncoupled.png')
plt.show()