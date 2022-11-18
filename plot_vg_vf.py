from nastran.post.f06 import read_f06
from nastran.post.flutter import get_critical_roots, join_flutter_pages, flutter_pages_to_df
from nastran.post.plots import plot_vf_vg
import matplotlib.pyplot as plt
# how many modes want to print
# Nastran always adds 6 more modes automatically.
# There is no need to consider the 6 modes other than the mode that requested output.
# can change mm/s to m/s or others
# C:\Users\kuhoo\AppData\Local\Programs\Python\Python310\Lib\site-packages\nastran\post\plots.py

res = read_f06('sol145_adddlm_f025_coupled.f06')

pages = join_flutter_pages(res.flutter)
df = flutter_pages_to_df(pages)
get_critical_roots(df)

p = plot_vf_vg(df, modes=(1, 3, 4, 6, 7, 9, 10, 12))
plt.title('FLUTTER ANALYSIS : Ref2020_DLM', pad=160)
plt.xlabel('Equivalent Airspeed (m/s)')
plt.ylabel('                                                      DAMPING                       FREQUENCY(Hz)')
plt.show()