from flask import Flask
import pickle

app = Flask(__name__)  # Renamed 'pancakes' to 'app'

print(__name__)

with open('classifier.pkl', 'rb') as f:
    clf = pickle.load(f)  # classifier is a random forest model

@app.route('/ping', methods=['GET'])
def ping():
    return 'Pinging Model Application!!'


#flask app app.py run