from nastran.post.f06 import read_f06
from nastran.post.flutter import get_critical_roots, join_flutter_pages, flutter_pages_to_df
from nastran.post.plots import plot_vf_vg, plot_complex
import matplotlib.pyplot as plt

res = read_f06('MA_final/referenz/sol145/dlm/sol145_dlm_100.f06')
pages = join_flutter_pages(res.flutter)
df = flutter_pages_to_df(pages)
get_critical_roots(df)

p = plot_vf_vg(df,modes=(1, 3, 4, 6, 7, 8, 11, 12)) # 4, 7, 12how many modes want to print, if you want to all, del modes=()
plt.title('FLUTTER ANALYSIS : Ref2020_DLM_100', pad=160)
plt.xlabel('Equivalent Airspeed (m/s)')
plt.ylabel('                                                      DAMPING                       FREQUENCY(Hz)')
plt.savefig('MA_final/referenz/sol145/dlm/Ref2020_DLM_100_vgvf.png')
plt.show()

p = plot_complex(df, modes=(1, 3, 4, 6, 7, 8, 11, 12))
plt.axvline(x=0, ymin=0, ymax=1, linestyle='dashed')
plt.title('FLUTTER_Root_Locus_Method : Ref2020_DLM_100')
plt.xlabel('Real Part (rad/sec)')
plt.ylabel('Imaginary part (Hz)')
plt.savefig('MA_final/referenz/sol145/dlm/Ref2020_DLM_100_root.png')
plt.show() #When the order of savefig and show changes, empty photos are saved. Be sure to use savefig first.