from nastran.post.f06 import read_f06
from nastran.post.flutter import get_critical_roots, join_flutter_pages, flutter_pages_to_df
from nastran.post.plots import plot_complex
import matplotlib.pyplot as plt
import os
print(os.getcwd())
res = read_f06('sol145_adddlm_f025_coupled_4_13_34_test_test.f06')
pages = join_flutter_pages(res.flutter)
df = flutter_pages_to_df(pages)
get_critical_roots(df)

p = plot_complex(df, modes=(1, 3, 4, 5, 7, 8, 10, 12))
plt.axvline(x=0, ymin=0, ymax=1, linestyle='dashed')
plt.title('FLUTTER_Root_Locus_Method : Ref2020_DLM')
plt.xlabel('Real Part (rad/sec)')
plt.ylabel('Imaginary part (Hz)')
plt.show()
