import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='default_status', data=df)
plt.title("Default vs Non-Default Borrowers")
plt.show()