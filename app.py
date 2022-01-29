from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
filename="diabetes.pkl"
classifier=pickle.load(open(filename,'rb'))
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        glucose=float(request.form['glucose'])
        bp=float(request.form['bloodpressure'])
        insulin=float(request.form['insulin'])
        bmi=float(request.form['bmi'])
        dpf=float(request.form['dpf'])
        age=float(request.form['age'])
        glucose1=(glucose-44)/(199-44)
        bp1=(bp-40)/(122-40)
        insulin1=(insulin-25)/(846-25)
        bmi1=(bmi-18.2)/(67.1-18.2)
        dpf1=(dpf-0.078)/(2.42-0.078)
        age1=(age-21)/(81-21)
        data=np.array([[glucose1,bp1,insulin1,bmi1,dpf1,age1]])
        predicted=classifier.predict(data)
        return render_template('result.html',prediction=predicted)

if __name__=="__main__":
    app.run(debug=True)