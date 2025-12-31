Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd

... 
>>> 
>>> from sklearn.linear_model import LinearRegression

... 
>>> from sklearn.model_selection import train_test_split
>>> from sklearn.metrics import r2_score
>>> data = {
...     "Hours": [2,3,4,5,6,7,8,9],
...     "Attendance": [60,65,70,75,80,85,90,95],
...     "Sleep": [5,6,6,7,7,8,8,9],
...     "Marks": [45,50,60,65,75,80,88,92]
...     }
>>> df = pd.DataFrame(data)
>>> X = df[["Hours", "Attendance", "Sleep"]]
>>> X = df[["Hours", "Attendance", "Sleep"]]
>>> y = df["Marks"]
>>> X = df[["Hours", "Attendance", "Sleep"]]
>>> X_train, X_test, y_train, y_test = train_test_split(
...     X, y, test_size=0.25, random_state=42
...     )
>>> model = LinearRegression()
>>> model.fit(X_train, y_train)
LinearRegression()
>>> y_pred = model.predict(X_test)
>>> print("R2 Score:", r2_score(y_test, y_pred))
R2 Score: 0.9948979591836735
>>> print("Coefficients:", model.coef_)
Coefficients: [ 0.37362637  1.86813187 -5.28571429]
