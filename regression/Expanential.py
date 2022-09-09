mod = sm.tsa.statespace.ExponentialSmoothing(y,
initialization_method="heuristic",
concentrate_scale = True,
seasonal = 3

)
results = mod.fit()
print(results.summary().tables[1])
