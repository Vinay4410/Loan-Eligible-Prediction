import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

with open('Model', 'rb') as model_file:
    model = pickle.load(model_file)

def preprocess_form_data(data):
    gender = int(data['gender'] == 'Male')  # 1 for Male, 0 for Female
    marital_status = int(data['maritalStatus'] == 'Yes')
    self_employed = int(data['selfEmployed'] == 'Yes')
    dependents = int(data['dependents'])
    education = int(data['education'] == 'Graduate')
    applicant_income = int(data['applicantIncome'])
    coapplicant_income = int(data['coapplicantIncome'])
    loan_amount = int(data['loanAmount'])
    loan_amount_term = int(data['loanAmountTerm'])
    credit_history = int(data['creditHistory'])
    property_area = int(data['propertyArea'] == 'Urban')

    x = [gender, marital_status, self_employed, dependents, education,
         applicant_income, coapplicant_income, loan_amount, loan_amount_term,
         credit_history, property_area]
    return [x]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = preprocess_form_data(request.form)

    prediction = model.predict(features)[0]
    
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
