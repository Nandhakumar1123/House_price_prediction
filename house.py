import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv('cleaned_dataset.csv')
#pd.set_option('display.max_columns', None)
pd.set_option('display.max_columns', None)
print(df.head())  # Or df to print the full DataFrame

print(df.info())
c=['Balcony']
df[c] = df[c].replace({'Yes': 1, 'No': 0}).astype(int)

print(df.info())
X = df[['Total_Area', 'Price_per_SQFT']]  

y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=542)
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

y_pred = lr_model.predict(X_test)
lr_y_pred = lr_model.predict(X_test)
r_accuracy = r2_score(y_test, lr_y_pred)*10000
print(r_accuracy)
total_area = int(input("Enter Total Area (in sq ft): "))
price_per_sqft = int(input("Enter Price per SQFT: "))

predicted_price = lr_model.predict(np.array([[total_area, price_per_sqft]]))  # ✅ Fixed input
print(f"Predicted Price: ₹{predicted_price[0]:,.2f}")
# Find the closest match in the dataset
matching_row = df.loc[(df['Total_Area'] == total_area) & (df['Price_per_SQFT'] == price_per_sqft)]

# Print entire row if found, otherwise show a message
if not matching_row.empty:
    print("\nMatching Property Details:\n", matching_row)
else:
    print("\nNo exact match found in the dataset.")
    print("\nNo exact match found in the dataset.")




#clean
c=['Balcony']
df[c] = df[c].replace({'Yes': 1, 'No': 0}).astype(int)
df.head(20) 


#declare X and y
X = df[['Property Size', 'Price_per_SQFT']]  
y = df['Price']

#train and testing  random values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#fitting into LR
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

#predicting values
y_pred = lr_model.predict(X_test)
lr_y_pred = lr_model.predict(X_test)

#accuracy
r_accuracy = r2_score(y_test, lr_y_pred)*10000
print('Accuracy : ',r_accuracy)

#getting input 
total_area = int(input("Enter Total Area (in sq ft): "))
price_per_sqft = int(input("Enter Price per SQFT: "))

#output
predicted_price = lr_model.predict(np.array([[total_area, price_per_sqft]])) 
print(f"Predicted Price: ₹{predicted_price[0]:,.2f}")

# Finding closest match in the dataset
matching_row = df.loc[(df['Total_Area'] == total_area) & (df['Price_per_SQFT'] == price_per_sqft)]


#parking 

import pandas as pd
df = pd.read_csv('Chennai houseing sale.csv')
df = df[['PARK_FACIL']]
print(df.head())

df.to_csv('park_only.csv', index=False)