from nastran.post.f06 import read_f06
from nastran.post.flutter import join_flutter_pages, flutter_pages_to_df
import matplotlib.pyplot as plt


res = read_f06('MA_final/referenz/ref_050/cs_sol145_dlm_050_ma08_nch6_narrow.f06')
pages = join_flutter_pages(res.flutter)
df = flutter_pages_to_df(pages)

res1 = read_f06('MA_final/referenz/ref_050/cs_sol145_dlm_050_ma08_nch10_narrow.f06')
pages1 = join_flutter_pages(res1.flutter)
df1 = flutter_pages_to_df(pages1)

res2 = read_f06('MA_final/referenz/ref_050/cs_sol145_dlm_050_ma08_nch15_narrow.f06')
pages2 = join_flutter_pages(res2.flutter)
df2 = flutter_pages_to_df(pages2)
res2 = read_f06('MA_final/referenz/ref_050/cs_sol145_dlm_050_ma08_nch20_narrow.f06')
pages2 = join_flutter_pages(res2.flutter)
df2 = flutter_pages_to_df(pages2)

x1 = df.loc[(1, 0.45, 1), 'VELOCITY']
y1 = df.loc[(1, 0.45, 1), 'DAMPING'] #subcase 1, mach 0.45, point 1

x2 = df.loc[(1, 0.45, 1), 'VELOCITY']
y2 = df.loc[(1, 0.45, 1), 'DAMPING']

# x3 = df1.loc[(1, 0.45, 1), 'VELOCITY']
# y3 = df1.loc[(1, 0.45, 1), 'DAMPING']
#
# x4 = df1.loc[(1, 0.45, 1), 'VELOCITY']
# y4 = df1.loc[(1, 0.45, 1), 'DAMPING']

plt.plot(x1/1000, y1, label='DLM 1', marker='o')
plt.plot(x2/1000, y2, label='Strip 1', marker='v')
# plt.plot(x3/1000, y3, label='Strip_mode1 x10', marker='x')
# plt.plot(x3/1000, y3, label='Strip_mode1 x0.5', marker='d')
plt.title('FLUTTER_DP4_M1_mode 1 : DLM vs Strip DP')
plt.xlabel('Velocity(m/s)')
plt.ylabel('Damping')
plt.legend()
plt.grid(True)
# plt.savefig('MA_final/DP4/DLM_vs_strip_dp4_m1_mode1_.png')
plt.show()