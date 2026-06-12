# 🏠 House Price Prediction Using Machine Learning

A Machine Learning project that predicts house prices using property features and Linear Regression. This project demonstrates data preprocessing, exploratory data analysis, model training, evaluation, and house price prediction.

---

## 📌 Overview

The goal of this project is to predict house prices based on property-related features such as area, property size, and price per square foot.

The project uses:

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn

---

## 🚀 Features

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Correlation Analysis
- Linear Regression Model
- House Price Prediction
- Actual vs Predicted Comparison
- Interactive User Input
- Data Visualization

---

## 📂 Project Structure

```text
House_Price_Prediction/
│
├── Housing.csv
├── house.py
│
├── Images/
│   ├── Acutal_vs_predicted price.png
│   ├── Correlation_matrix1.png
│   ├── Matchingcity with price.png
│   ├── Mode_evaluation &Model comparison.png
│   ├── Predicted_price.png
│   ├── correlation_heatmap.png
│   └── price_vs_totalarea.png
│
└── README.md
```

---

## 🧠 Machine Learning Workflow

### 1. Data Collection

The dataset contains housing-related information including:

- Area
- Bedrooms
- Bathrooms
- Stories
- Parking
- Furnishing Status
- Price

### 2. Data Preprocessing

- Handle missing values
- Encode categorical features
- Feature selection
- Data transformation

### 3. Model Training

The dataset is split into:

- Training Data (80%)
- Testing Data (20%)

The model is trained using:

```python
from sklearn.linear_model import LinearRegression
```

### 4. Model Evaluation

The model performance is evaluated using:

- R² Score
- Actual vs Predicted Analysis
- Model Comparison

---

## 📊 Visualizations

### Correlation Heatmap

![Correlation Heatmap](Images/correlation_heatmap.png)

### Correlation Matrix

![Correlation Matrix](Images/Correlation_matrix1.png)

### Price vs Total Area

![Price vs Total Area](Images/price_vs_totalarea.png)

### City-wise Price Analysis

![City Price Analysis](Images/Matchingcity%20with%20price.png)

### Predicted House Price

![Predicted House Price](Images/Predicted_price.png)

### Actual vs Predicted Price

![Actual vs Predicted](Images/Acutal_vs_predicted%20price.png)

### Model Evaluation & Comparison

![Model Evaluation](Images/Mode_evaluation%20%26Model%20comparison.png)

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/House_Price_Prediction.git
```

Move to project folder:

```bash
cd House_Price_Prediction
```

Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

Run the project:

```bash
python house.py
```

---

## 📈 Sample Prediction

### Input

```text
Enter Total Area: 1200
Enter Price Per SQFT: 5000
```

### Output

```text
Predicted House Price:
₹ 6,000,000
```

---

## 📋 Results

- Successfully trained a Linear Regression model.
- Generated house price predictions based on property features.
- Visualized relationships between house attributes and prices.
- Compared actual prices with predicted values.

---

## 🔮 Future Improvements

- Random Forest Regressor
- XGBoost Regressor
- Hyperparameter Tuning
- Web Application Deployment
- Real-time House Price Prediction
- Advanced Feature Engineering

---

## 👨‍💻 Author

**Nandhakumar D**

Machine Learning Project – House Price Prediction

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
