from nastran.post.f06 import read_f06
from nastran.post.flutter import get_critical_roots, join_flutter_pages, flutter_pages_to_df
from nastran.post.plots import plot_vf_vg
import matplotlib.pyplot as plt

res = read_f06('sol145_adddlm.f06')

pages = join_flutter_pages(res.flutter)
df = flutter_pages_to_df(pages)
get_critical_roots(df)

p = plot_vf_vg(df, modes=(3,7)) # how many modes want to print, if you want to all, del modes=()
plt.title('FLUTTER ANALYSIS : Ref2020_DLM', pad=160)
plt.xlabel('Equivalent Airspeed (mm/s)')
plt.ylabel('                                                      DAMPING                       FREQUENCY(Hz)')
plt.show()