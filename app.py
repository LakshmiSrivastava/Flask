from flask import Flask, request
import pickle

app = Flask(__name__)

with open('classifier.pkl', 'rb') as f:
    clf = pickle.load(f)

@app.route('/ping', methods=['GET'])
def ping():
    return 'Pinging Model Application!!'

@app.route('/predict', methods=['POST'])
def predict():
    loan_req = request.get_json()

    gender = 0 if loan_req['gender'] == 'Male' else 1
    marital_status = 0 if loan_req['married'] == 'unmarried' else 1
    credit_history = 0 if loan_req['credit_history'] == 'Unclear Debts' else 1

    applicant_income = int(loan_req['applicant_income'])
    loan_amount = int(loan_req['loan_amount'])

    result = clf.predict([[
        gender,
        marital_status,
        credit_history,
        applicant_income,
        loan_amount
    ]])

    pred = 'Rejected' if result == 0 else 'Approved'

    return {'loan_approval_status': pred}
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


