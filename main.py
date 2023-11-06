import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = pandas.read_csv('iphone_price.csv')
plt.scatter(data['version'], data['price'])
plt.show()
model = LinearRegression()
model.fit(data[['version']], data[['price']])
n = int(input("Enter the version of iPhone price you want to see : "))
print(model.predict([[n]]))