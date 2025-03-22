from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained ML model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction')  # This route loads the form
def prediction():
    return render_template("prediction.html")

@app.route('/predict', methods=['POST'])  # This route processes form data
def predict():
    try:
        # Fetch form values
        gender = request.form['gender']
        married = request.form['married']
        dependents = request.form['dependents']
        education = request.form['education']
        employed = request.form['employed']
        credit = float(request.form['credit'])
        area = request.form['area']
        applicant_income = float(request.form['ApplicantIncome'])
        coapplicant_income = float(request.form['CoapplicantIncome'])
        loan_amount = float(request.form['LoanAmount'])
        loan_term = float(request.form['Loan_Amount_Term'])

        # Encode categorical features
        male = 1 if gender == "Male" else 0
        married_yes = 1 if married == "Yes" else 0
        not_graduate = 1 if education == "Not Graduate" else 0
        employed_yes = 1 if employed == "Yes" else 0
        semiurban = 1 if area == "Semiurban" else 0
        urban = 1 if area == "Urban" else 0

        # Encode dependents
        dep_1 = dep_2 = dep_3 = 0
        if dependents == '1':
            dep_1 = 1
        elif dependents == '2':
            dep_2 = 1
        elif dependents == '3+':
            dep_3 = 1

        # Apply log transformations
        applicant_income_log = np.log(applicant_income)
        total_income_log = np.log(applicant_income + coapplicant_income)
        loan_amount_log = np.log(loan_amount)
        loan_term_log = np.log(loan_term)

        # Final feature vector for prediction
        features = [[credit, applicant_income_log, loan_amount_log, loan_term_log, total_income_log,
                     male, married_yes, dep_1, dep_2, dep_3,
                     not_graduate, employed_yes, semiurban, urban]]

        prediction = model.predict(features)

        result = "Loan Approved ✅" if prediction[0] == 1 else "Loan Rejected ❌"
        return render_template("prediction.html", prediction_text=result)

    except Exception as e:
        return render_template("prediction.html", prediction_text=f"Error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
