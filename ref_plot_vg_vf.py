from nastran.post.f06 import read_f06
from nastran.post.flutter import get_critical_roots, join_flutter_pages, flutter_pages_to_df
from nastran.post.plots import plot_vf_vg, plot_complex
import matplotlib.pyplot as plt


res = read_f06('MA_final/referenz/ref_025/cs_sol145_dlm_025_ma08_nch20_global.f06')
pages = join_flutter_pages(res.flutter)
df = flutter_pages_to_df(pages)
get_critical_roots(df)

p = plot_vf_vg(df,modes=(1, 3, 4, 6, 7, 9, 10))
# 1, 3, 4, 6, 7, 9, 11
# 1, 3, 4, 6, 7, 11how many modes want to print, if you want to all, del modes=()
plt.title('REF 25 : DLM_Ma 0.0', pad=160)
plt.xlabel('Velocity (EAS) [m/s]')
plt.ylabel('                                                      DAMPING [-]                      FREQUENCY [Hz]')
plt.savefig('MA_final/referenz/cs_sol145_dlm_025_ma08_nch20_global.f06_vgvf.png')
# plt.legend()
# plt.axhline(y=0, color='black', linestyle='-')
plt.grid(True)
plt.show()

# p = plot_complex(df, modes=(1, 3, 4, 6, 7))
# plt.axvline(x=0, ymin=0, ymax=1, linestyle='dashed')
# plt.title('CS_FLUTTER_Root_Locus_Method : Ref2020_dlm_m050_ma08_nch6_global')
# plt.xlabel('Real Part (rad/sec)')
# plt.ylabel('Imaginary part (Hz)')
# plt.savefig('MA_final/referenz/ref_100/CS_Ref2020_dlm_m050_ma08_nch6_global_root.png')
# plt.show() #When the order of savefig and show changes, empty photos are saved. Be sure to use savefig first.
















# res = read_f06('MA_final/referenz/cs_sol145_strip_500.f06')
# pages = join_flutter_pages(res.flutter)
# df = flutter_pages_to_df(pages)
# get_critical_roots(df)
#
# p = plot_vf_vg(df,modes=(1, 3, 4, 6, 7)) # 1, 3, 4, 6, 7, 11how many modes want to print, if you want to all, del modes=()
# plt.title('CS_FLUTTER ANALYSIS : Ref2020_strip_500_Ma08', pad=160)
# plt.xlabel('Equivalent Airspeed (m/s)')
# plt.ylabel('                                                      DAMPING                       FREQUENCY(Hz)')
# plt.savefig('MA_final/referenz/CS_Ref2020_strip_500_Ma08_vgvf.png')
# plt.show()
#
# p = plot_complex(df, modes=(1, 3, 4, 6, 7))
# plt.axvline(x=0, ymin=0, ymax=1, linestyle='dashed')
# plt.title('CS_FLUTTER_Root_Locus_Method : Ref2020_strip_500_Ma08')
# plt.xlabel('Real Part (rad/sec)')
# plt.ylabel('Imaginary part (Hz)')
# plt.savefig('MA_final/referenz/CS_Ref2020_dlm_100_strip_500_Ma08_root.png')
# plt.show() #When the order of savefig and show changes, empty photos are saved. Be sure to use savefig first.