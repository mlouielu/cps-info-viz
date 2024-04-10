from pycps import get_asec

asec = get_asec(2021, ["a_age", "marsupwt"])

print(asec)
#         a_age  marsupwt
# 0          56    687.71
# 1          57    687.71
# 2          78    646.86
# 3          65   1516.95
# 4          66   1516.95
# ...       ...       ...
# 163538     69    514.11
# 163539     70    516.25
# 163540     66    516.25
# 163541     55    386.37
# 163542     52    386.37
#
# [163543 rows x 2 columns]

print(asec.marsupwt.sum())
# 326195439.67
