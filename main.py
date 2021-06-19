# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
from joblib import load
import numpy as np
import warnings
warnings.simplefilter("ignore")

app = Flask(__name__) # initializing a flask app

@app.route("/",methods = ["GET"])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route("/predict",methods = ["POST","GET"]) # route to show the predictions in a web UI
@cross_origin()
def predict():
    if request.method == "POST":
        try:
            #  reading the inputs given by the user
            input1 = float(request.form["input1"])
            input2 = float(request.form["input2"])
            input3 = float(request.form["input3"])
            input4 = float(request.form["input4"])
            input5 = float(request.form["input5"])
            input6 = float(request.form["input6"])
            input7 = float(request.form["input7"])
            input8 = float(request.form["input8"])
            input9 = float(request.form["input9"])
            input10 = float(request.form["input10"])
            input11 = float(request.form["input11"])
            input12 = float(request.form["input12"])
            input13 = float(request.form["input13"])
            input14 = float(request.form["input14"])
            input15 = float(request.form["input15"])
            input16 = float(request.form["input16"])
            
            """ Example:- input_features = np.array([[-123.12,38.3,56.2,3797.42,
                                706.5,1521.12,714.135,3.6513,
                                5.34,0.1987,2.169,1.0,0.0,
                                0.0,0.0,0.0]])"""
            
            arr = np.array([[input1,input2,input3,input4,
                                         input5,input6,input7,input8,
                                         input9,input10,input11,input12,
                                         input13,input14,input15,input16]])
            model = load("RandomForestRegressor.joblib")
            prediction = model.predict(arr)
            
                   
            print("The median house value prediction is:"+str(round(prediction[0],3)) +"$")
            # showing the prediction results in a UI
            return render_template("index.html",data = round(prediction[0],3))
        except Exception as e:
            print("The Exception message is: "+str(e))
            return "Something went wrong"
    # return render_template('results.html')
    else:
        return render_template("index.html")



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug = True) # running the app