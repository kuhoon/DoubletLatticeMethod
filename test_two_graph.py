from nastran.post.f06 import read_f06
from nastran.post.flutter import join_flutter_pages, flutter_pages_to_df
import matplotlib.pyplot as plt

res = read_f06('MA_final/referenz/sol145/strip/sol145_strip_050.f06')
pages = join_flutter_pages(res.flutter)
df = flutter_pages_to_df(pages)

res1 = read_f06('MA_final/referenz/sol145/strip/test/sol145_strip_050.f06')
pages1 = join_flutter_pages(res1.flutter)
df1 = flutter_pages_to_df(pages1)

res2 = read_f06('MA_final/referenz/sol145/strip/test2/sol145_strip_050.f06')
pages2 = join_flutter_pages(res2.flutter)
df2 = flutter_pages_to_df(pages2)

x1 = df.loc[(1, 0.45, 1), 'VELOCITY']
y1 = df.loc[(1, 0.45, 1), 'DAMPING'] #subcase 1, mach 0.45, point 1

x2 = df1.loc[(1, 0.45, 1), 'VELOCITY']
y2 = df1.loc[(1, 0.45, 1), 'DAMPING']

x3 = df1.loc[(1, 0.45, 1), 'VELOCITY']
y3 = df1.loc[(1, 0.45, 1), 'DAMPING']

plt.plot(x1/1000, y1, label='Strip_model')
plt.plot(x2/1000, y2, label='Strip_mode1 x3')
plt.plot(x3/1000, y3, label='Strip_mode1 x10')
plt.title('FLUTTER_REFERENZ : Strip vs STRIP_050_more')
plt.xlabel('Velocity(m/s)')
plt.ylabel('Damping')
plt.legend()
plt.grid(True)
plt.savefig('MA_final/referenz/sol145/Strip_vs_STRIP_ref_050_mode1_.png')
plt.show()