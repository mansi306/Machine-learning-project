# Loan Approval Prediction Project

This project is a **Loan Approval Prediction System** developed using **Machine Learning** with a web interface powered by **Flask**. It helps banks or financial institutions predict whether a loan application should be approved based on applicant information such as income, education, employment status, etc.

---

## 📁 Project Structure
```
loan_prediction-main/
├── app.py                  # Main Flask application
├── model.pkl               # Trained Machine Learning model (Pickle file)
├── requirements.txt        # Project dependencies
├── Procfile                # For deployment (Heroku)
├── train.csv               # Training dataset
├── test.csv                # Test dataset
├── Loan Prediction.ipynb   # Jupyter Notebook - EDA, model building, training
├── templates/
│   ├── index.html         # Input form for prediction
│   └── prediction.html    # Output page showing prediction result
└── README.md               # Project documentation (you are here)
```

---

## 💡 Problem Statement
The objective is to predict whether a loan application will be approved based on information like:
- Gender
- Marital Status
- Education
- Employment Status
- Income
- Loan Amount

---

## 📊 Dataset Description
The dataset is sourced from a loan approval system. It contains both training and testing data.

### Key Columns:
- `Loan_ID`
- `Gender`
- `Married`
- `Dependents`
- `Education`
- `Self_Employed`
- `ApplicantIncome`
- `CoapplicantIncome`
- `LoanAmount`
- `Loan_Amount_Term`
- `Credit_History`
- `Property_Area`
- `Loan_Status` *(Target column in training data)*

There are:
- 📂 **614 records in `train.csv`**
- 📂 **368 records in `test.csv`**

---

## 🔍 Model Building Workflow
1. **Data Cleaning & Preprocessing**
2. **Exploratory Data Analysis (EDA)**
3. **Feature Engineering**
4. **Model Selection** (Logistic Regression)
5. **Model Training**
6. **Model Evaluation**
7. **Saving Model (model.pkl)**
8. **Web Integration using Flask**

---

## 🚀 How It Works (Flask Web App)
- User enters loan application details on `index.html`
- Form data is sent to the backend (`app.py`)
- Model predicts if loan will be approved or not
- Result is shown on `prediction.html`

---

## 🛠 Technologies Used
- Python
- Pandas, NumPy, Seaborn, Matplotlib
- Scikit-learn
- Flask
- HTML/CSS (Bootstrap for styling)

---

## 📦 Installation & Run Instructions
1. Clone the repository:
```bash
git clone https://github.com/mansi306/loan_prediction-main.git
cd loan_prediction-main
```
2. Create virtual environment & activate it:
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run Flask App:
```bash
python app.py
```
5. Visit in browser: `http://127.0.0.1:5000/`

---

## 📷 Sample Prediction Interface
## Home Page 
![Home Page Screenshot](https://github.com/mansi306/Machine-learning-project/raw/main/loan_prediction-main/static/Images/Home_page.png)

---

## 📁 test.csv Preview (few rows)
| Loan_ID | Gender | Married | Dependents | Education | Self_Employed | ApplicantIncome | CoapplicantIncome | LoanAmount | Loan_Amount_Term |
|---------|--------|---------|------------|-----------|----------------|------------------|--------------------|------------|------------------|
| LP001015 | Male | Yes | 0 | Graduate | No | 5720 | 0 | 110 | 360 |
| LP001022 | Male | Yes | 1 | Graduate | No | 3076 | 1500 | 126 | 360 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

---

## 📌 Interview Questions & Answers

### 1. What is the objective of this project?
The main objective is to predict whether a loan application should be approved or rejected based on the applicant’s details using a Machine Learning model.

### 2. What type of ML model is used here?
We used **Logistic Regression**, which is a supervised learning algorithm used for classification problems.

### 3. What are the important features in this dataset?
- Gender
- Married status
- Dependents
- Education
- Self Employed
- Applicant & Coapplicant Income
- Loan Amount
- Credit History
- Property Area

### 4. Why did you choose Logistic Regression?
It is simple, efficient, and suitable for binary classification problems like predicting loan approval (Yes/No).

### 5. How did you handle missing values?
We used techniques like filling missing values using **mean**, **median**, or **mode** depending on the feature type.

### 6. What performance metric did you use?
We used **accuracy score**, **confusion matrix**, and **classification report (precision, recall, f1-score)**.

### 7. How did you integrate ML with the web interface?
We used **Flask** framework. Input form collects user data and passes it to the ML model via the Flask backend. The prediction result is displayed on the output page.

### 8. What is `model.pkl`?
It’s a **Pickle file** that contains the trained ML model, saved using Python’s `pickle` library so we can reuse it without retraining.

### 9. What is the use of `Procfile`?
It is used for **deployment on Heroku**. It tells Heroku how to run the app.

### 10. Can this model be improved further?
Yes, by:
- Trying advanced models like Random Forest, XGBoost
- Hyperparameter tuning
- Cross-validation
- Improving preprocessing and feature engineering

### 11. What challenges did you face?
- Handling missing values
- Encoding categorical variables
- Ensuring model performance is consistent
- Integrating frontend and backend smoothly

### 12. Why did you choose Flask over Django?
Flask is lightweight, easier for small ML projects, and gives more flexibility without much overhead.

### 13. How would you deploy this project?
- Use **Heroku** with `Procfile`, `requirements.txt`, and GitHub integration.
- Alternatively, use **Render**, **PythonAnywhere**, or **Docker + AWS**.

### 14. What libraries did you use?
- **Pandas, NumPy**: Data preprocessing
- **Matplotlib, Seaborn**: Visualization
- **Scikit-learn**: ML Model building
- **Flask**: Web framework

### 15. What is Credit History and why is it important?
Credit history shows whether the applicant has repaid past loans. It is a key factor in deciding loan approval probability.

### 16. What is the role of `train.csv` and `test.csv`?
- `train.csv` is used to train the model
- `test.csv` is used to evaluate model performance or simulate real-time prediction

### 17. What does the prediction output look like?
It will show either **"Loan Approved"** or **"Loan Rejected"** based on the model’s prediction.

### 18. How will you explain this project to a non-technical person?
We built a system where banks can enter applicant details and instantly get a prediction on whether the loan should be approved or not, helping them take faster decisions.

---
## 📃 License
This project is open-source and free to use under the [MIT License](LICENSE).

---

## 📧 Contact
Created by **Mansi306** · Feel free to reach out for queries!

