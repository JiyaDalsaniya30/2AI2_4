# 🏥 Medical Insurance Cost Prediction

## 👥 Team Members
| Name   | ID |
|--------|------|
| Jiya Dalsaniya    | 2503031240024 | [LEADER]
| Mehul Mehta       | 2503031240064 |
| Dhruv Mahajan     | 2503031240059 |
| Prem Mesavaniya   | 2503031240065 |
| Krish Solanki     | 2503031240055 |
| Harshvardhan Goud | 2503031240068 |

---

## 📌 Problem Statement
The objective of this project is to **predict medical insurance charges** based on individual attributes such as:

- Age  
- Gender  
- BMI (Body Mass Index)  
- Number of children  
- Smoking habits  
- Region  

The goal is to identify key factors affecting insurance costs and build an accurate machine learning model.

---

## 📊 Dataset Description

| Feature   | Description |
|----------|------------|
| age      | Age of the individual |
| sex      | Gender (male/female) |
| bmi      | Body Mass Index |
| children | Number of dependents |
| smoker   | Smoking status (yes/no) |
| region   | Residential region |
| charges  | Insurance cost (Target Variable) |

✔️ Dataset is clean and contains **no missing values**

---

## 🧹 Data Preprocessing
- Checked for missing values  
- Converted categorical variables:
  - `sex` → 0 / 1  
  - `smoker` → 0 / 1  
  - `region` → Label Encoding  
- Split dataset into:
  - Training Set (80%)  
  - Testing Set (20%)  
- Applied feature scaling (if needed)

---

## 🤖 Model Training
- **Algorithm Used:** Linear Regression  
- **Library:** Scikit-learn  

Steps:
1. Load dataset  
2. Split data  
3. Train model  
4. Predict on test data  

---

## 📈 Model Evaluation

Metrics used:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

### 🔍 Key Insights
- 🚬 Smoking significantly increases insurance cost  
- ⚖️ Higher BMI leads to higher charges  
- 👴 Age is directly proportional to insurance cost  

---

## 🔗 GitHub Collaboration
- Repository created on GitHub  
- Code & dataset uploaded  
- Version control using commits  
- Team collaboration using branches  
- Proper project structure maintained  

---

## 📌 Conclusion
This project demonstrates how **Machine Learning** can predict insurance charges effectively.

✔️ Linear Regression gives a strong baseline  
✔️ Model performance is good on test data  

### 🚀 Future Improvements
- Use advanced models (Random Forest, XGBoost)  
- Hyperparameter tuning  
- Feature engineering  

---

