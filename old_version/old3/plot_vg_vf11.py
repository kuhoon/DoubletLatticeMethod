from pyNastran.op2.op2 import OP2

# create an instance of the OP2 class with the path to the F06 file
op2 = OP2()

# read the F06 file
op2.read_f06('MA/sol145_adddlm_f000_636.f06')

# get a list of all the subcases in the F06 file
subcase_ids = op2.get_op2_info().subcase_ids

# get the result for a specific subcase (in this case, subcase 1)
result = op2.get_displacement_index


f06_filename = data['MA/sol145_adddlm_f000_636.f06']
# res = test_plot_flutter2(plot_vg, 'MA/sol145_adddlm_f000_636.f06')
#
# plot_root_locus(res, modes=[1, 3, 4, 5, 7, 8, 10, 12])
# plt.title('FLUTTER ANALYSIS : Ref2020_DLM_TEST_100', pad=160)
# plt.xlabel('Equivalent Airspeed (m/s)')
# plt.ylabel('                                                      DAMPING                       FREQUENCY(Hz)')
# plt.show()

plot_flutter_f06('MA/sol145_adddlm_f000_636.f06', show=False, log=log)