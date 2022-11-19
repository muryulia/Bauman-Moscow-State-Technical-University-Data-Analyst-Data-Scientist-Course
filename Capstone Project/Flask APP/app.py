import flask 
from flask import render_template 
import pickle 
import sklearn 
import numpy as np
from sklearn import model_selection
from sklearn.ensemble import GradientBoostingRegressor 
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.multioutput import MultiOutputRegressor

app = flask.Flask(__name__, template_folder='templates') 

@app.route('/', methods=['POST', 'GET']) 
@app.route('/index', methods=['POST', 'GET']) 

def main():
    if flask.request.method == 'GET':
        return render_template('main.html') 

    if flask.request.method == 'POST':
        with open('gb_model.pkl', 'rb') as f:
            loaded_model = pickle.load(f)

        test_data = []
        IW = float(flask.request.form['IW']) 
        IF = float(flask.request.form['IF']) 
        VW = float(flask.request.form['VW']) 
        FP = float(flask.request.form['FP']) 
        test_data.append(IW)
        test_data.append(IF)
        test_data.append(VW)
        test_data.append(FP)
        test_data = np. array([test_data])

        y_pred = loaded_model.predict(test_data) 
        depth = round(y_pred[0,0], 2)
        width = round(y_pred[0,1], 2)

        return render_template('main.html', 
            result=str(depth) + ', ' + str(width)
        ) 

if __name__ == '__main__':
    app.run()