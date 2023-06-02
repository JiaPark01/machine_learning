import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(type(tips))
print(tips.shape)
print(tips)

sns.relplot(data=tips, x = "total_bill", y = "tip", col = "time", hue = "smoker", style = "smoker", size = "size")
print(tips.head(7))
print(tips.tail())
plt.show()