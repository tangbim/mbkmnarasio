# import numpy as np
from scipy.stats import ttest_ind, ttest_ind_from_stats, ttest_1samp
# from scipy.special import stdtr

# alpha = 0.05
# score1 = [56,76,62,57,55,61,62,43,57,61,58]
# score2 = [80,75,62,95,80,86,87,79,78,88,91]

# stat,p = ttest_ind(score1,score2)

# print('t = %.3f, p = %.3f'% (stat,p))

# if p < alpha:
#       print('tolak h0')
# else:
#       print('gagal tolak')

import numpy as np
from scipy import stats

alpha = 0.05

data = [108,112,117,130,111,131,113,113,105,128]
meanNull = 120

t_statistic, p_value = ttest_1samp(data, meanNull)
if p_value < alpha:
    print("Reject the null hypothesis. There is sufficient evidence to suggest that the population mean is less than", meanNull)
else:
    print("Fail to reject the null hypothesis. There is not sufficient evidence to suggest that the population mean is less than", meanNull)
