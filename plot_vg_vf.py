from nastran.post.f06 import read_f06
from nastran.post.flutter import get_critical_roots, join_flutter_pages, flutter_pages_to_df
from nastran.post.plots import plot_vf_vg, plot_complex
import matplotlib.pyplot as plt
# how many modes want to print
# In sol 145, Nastran always adds more 6 modes automatically.
# There is no need to consider the 6 modes other than the mode that requested output.
# can change mm/s to m/s or others
# C:\Users\kuhoo\AppData\Local\Programs\Python\Python310\Lib\site-packages\nastran\post\plots.py

# new1 = 'C:\Users\kuhoo\PycharmProjects\DoubletLatticeMethod\Change_sPan\new'

n = int(input("Bitte gebe eine Beladungszustände mit 00, 25, 50 und 100% ein : "))
if n == 00 :
    res = read_f06('test/sol145_adddlm_f000_636.f06')
    pages = join_flutter_pages(res.flutter)
    df = flutter_pages_to_df(pages)
    get_critical_roots(df)
    # print(df.VELOCITY*0.001) #show VELOCITY in Dataframe, change mm/s to m/s with *0.001
    p = plot_vf_vg(df, modes=(1, 3, 4, 7, 8, 10, 12))
    plt.title('FLUTTER ANALYSIS : Ref2020_DLM_TEST_00', pad=160)
    plt.xlabel('Equivalent Airspeed (m/s)')
    plt.ylabel('                                                      DAMPING                       FREQUENCY(Hz)')
    plt.show()

    p = plot_complex(df, modes=(1, 3, 4, 5, 7, 8, 10, 12))
    plt.axvline(x=0, ymin=0, ymax=1, linestyle='dashed')
    plt.title('FLUTTER_Root_Locus_Method : Ref2020_DLM_TEST_00')
    plt.xlabel('Real Part (rad/sec)')
    plt.ylabel('Imaginary part (Hz)')
    plt.show()

if n == 25 :
    res = read_f06('test/sol145_adddlm_f025_636.f06')
    pages = join_flutter_pages(res.flutter)
    df = flutter_pages_to_df(pages)
    get_critical_roots(df)
    # print(df.VELOCITY*0.001) #show VELOCITY in Dataframe, change mm/s to m/s with *0.001
    p = plot_vf_vg(df, modes=(1, 3, 4, 5, 7, 8, 10, 12))
    plt.title('FLUTTER ANALYSIS : Ref2020_DLM_TEST_25', pad=160)
    plt.xlabel('Equivalent Airspeed (m/s)')
    plt.ylabel('                                                      DAMPING                       FREQUENCY(Hz)')
    plt.show()

    p = plot_complex(df, modes=(1, 3, 4, 5, 7, 8, 10, 12))
    plt.axvline(x=0, ymin=0, ymax=1, linestyle='dashed')
    plt.title('FLUTTER_Root_Locus_Method : Ref2020_DLM_TEST_25')
    plt.xlabel('Real Part (rad/sec)')
    plt.ylabel('Imaginary part (Hz)')
    plt.show()

elif n == 50 :
    res = read_f06('test/sol145_adddlm_f050_636.f06')
    pages = join_flutter_pages(res.flutter)
    df = flutter_pages_to_df(pages)
    get_critical_roots(df)
    # print(df.VELOCITY*0.001) #show VELOCITY in Dataframe, change mm/s to m/s with *0.001
    p = plot_vf_vg(df, modes=(1, 3, 4, 6, 7, 8, 11, 12))
    plt.title('FLUTTER ANALYSIS : Ref2020_DLM_TEST_50', pad=160)
    plt.xlabel('Equivalent Airspeed (m/s)')
    plt.ylabel('                                                      DAMPING                       FREQUENCY(Hz)')
    plt.show()

    p = plot_complex(df, modes=(1, 3, 4, 6, 7, 8, 11, 12))
    plt.axvline(x=0, ymin=0, ymax=1, linestyle='dashed')
    plt.title('FLUTTER_Root_Locus_Method : Ref2020_DLM_TEST_50')
    plt.xlabel('Real Part (rad/sec)')
    plt.ylabel('Imaginary part (Hz)')
    plt.show()

elif n == 100 :
    res = read_f06('test/sol145_adddlm_f100_636.f06')
    pages = join_flutter_pages(res.flutter)
    df = flutter_pages_to_df(pages)
    get_critical_roots(df)
    # print(df.VELOCITY*0.001) #show VELOCITY in Dataframe, change mm/s to m/s with *0.001
    p = plot_vf_vg(df, modes=(1, 3, 4, 5, 7, 8, 10, 12))
    plt.title('FLUTTER ANALYSIS : Ref2020_DLM_TEST_100', pad=160)
    plt.xlabel('Equivalent Airspeed (m/s)')
    plt.ylabel('                                                      DAMPING                       FREQUENCY(Hz)')
    plt.show()

    p = plot_complex(df, modes=(1, 3, 4, 6, 7, 8, 10, 12))
    plt.axvline(x=0, ymin=0, ymax=1, linestyle='dashed')
    plt.title('FLUTTER_Root_Locus_Method : Ref2020_DLM_TEST_100')
    plt.xlabel('Real Part (rad/sec)')
    plt.ylabel('Imaginary part (Hz)')
    plt.show()


# print(get_critical_roots(df))
#
# from nastran.post.f06 import read_f06
# from nastran.post.flutter import get_critical_roots, join_flutter_pages, flutter_pages_to_df
# from nastran.post.plots import plot_complex
# import matplotlib.pyplot as plt
#
# res = read_f06('ref_flugel/sol145/sol145_adddlm_f025_coupled_4_13_34_test.f06')
# pages = join_flutter_pages(res.flutter)
# df = flutter_pages_to_df(pages)
# get_critical_roots(df)
#
# p = plot_complex(df, modes=(1, 3, 4, 5, 7, 8, 10, 12))
# plt.axvline(x=0, ymin=0, ymax=1, linestyle='dashed')
# plt.title('FLUTTER_Root_Locus_Method : Ref2020_DLM_TEST')
# plt.xlabel('Real Part (rad/sec)')
# plt.ylabel('Imaginary part (Hz)')
# plt.show()
