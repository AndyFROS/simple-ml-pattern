import seaborn as sns
import matplotlib.pyplot as plt
#Перед визуализацией используйте кодировщик меток (Он находится по пути universe/Cycle_Label_Encoder.py)
plt.figure(figsize=(23, 15))
sns.heatmap(df.corr(), annot = True, vmin=-1, vmax=1,cmap= 'coolwarm')
