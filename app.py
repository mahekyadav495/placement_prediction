from flask import Flask, request, jsonify
import pickle
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return "Placement prediction api is working"
@app.route('/predict',methods=['POST'])
def predict():
    data=request.json
    features = [[
        data['cgpa'],
        data['aptitude'],
        data['communictaion'],
        data['project']
    ]]
    prediction = model.predict(features)[0]
    return jsonify({
        "prediction":int(prediction)
    })
import os
if __name__=='__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0',port=port)    