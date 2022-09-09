import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:f}'.format})

pd.set_option('display.float_format', lambda x: '%.3f' % x)

pd.options.display.max_columns=50

import warnings
warnings.filterwarnings("ignore")


mod = sm.tsa.statespace.SARIMAX(y,
order=(1, 1, 1),
seasonal_order=(1, 2, 1, 9),
enforce_stationarity=False,
enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])
