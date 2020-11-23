from flask import Flask,request, url_for, redirect, render_template
import numpy as np
from keras.models import load_model

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("forest_fire.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    print(int_features)
    model = load_model("my_model")
    prediction=model.predict([int_features])
    output='{0:.{1}f}'.format(prediction[0][0], 2)

    if output>str(0.5):
        return render_template('forest_fire.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output),bhai="kuch karna hain iska ab?")
    else:
        return render_template('forest_fire.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now")


 
if __name__ == '__main__':
    app.run()
