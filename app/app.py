from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from joblib import load
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='')
    else:
        mysalary = request.form['Your_age']
        mygender = request.form['Your_gender']
        mymarital = request.form['Your_marital']
        from sklearn.tree import DecisionTreeClassifier
        df = pd.read_csv("app/travel.csv")
        feature_cols = ['salary', 'gender', 'marital']
        x = df[feature_cols]
        y = df.destination
        model = DecisionTreeClassifier()
        model = model.fit(x.values, y)
        np_arr = np.array([mysalary, mygender, mymarital])
        y_pred = model.predict([np_arr])  
        y_pred_to_str = str(y_pred)
        #return predictions_to_str
        return render_template('index.html', href2='The recommended travel destination for you (salary:'+str(mysalary)+', gender:'+str(mygender)+', marital status:'+str(mymarital)+') is:'+y_pred_to_str)

