plt.figure(figsize=(10, 5))
sns.lineplot(data=df[df["class"] == 0], x="year", y="marks")
plt.title(f"g")
plt.show()
