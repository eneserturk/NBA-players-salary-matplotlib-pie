import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("nba2k20-full.csv")
df = pd.DataFrame(data)

piece = int(input("How many NBA players' salaries would you like to see on the pie chart: "))

salary = []
for x in data["salary"]:
    y = x.split("$")
    salary.append(int(y[1]))

data["salary"] = salary

cash = data.sort_values("salary",ascending=False).head(piece)["salary"]
name = data.sort_values("salary",ascending=False).head(piece)["full_name"]

plt.pie(cash,labels=name,shadow=True,autopct="%1.1f%%")
plt.show()

