
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__)
model = load_model('churnmodelANN.h5')


@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
  '''
  For rendering results on HTML GUI
  '''
  creditscore = int(request.args.get('creditscore'))
  geo = int(request.args.get('geo'))
  age = int(request.args.get('age'))
  tenure = int(request.args.get('tenure'))  
  balance = int(request.args.get('balance'))
  numofproducts = int(request.args.get('numofproducts')) 
  creditcards=int(request.args.get('creditcards'))
  activemember = int(request.args.get('activemember'))
  
  salary = int(request.args.get('salary')) 
  
  
  y_pred= model.predict(sc_X.transform(np.array([[0,1, creditscore,geo,age,tenure,balance,
                                                  numofproducts,creditcards,activemember,salary]])))
  y_pred = (y_pred > 0.5)
  if y_pred>0.5:
    result="Customer will not exit Bank"
  else:
    result="Customer will exit bank"
        
  return render_template('index.html', prediction_text='Model  has predicted  : {}'.format(result))


if __name__ == "__main__":
    app.run()