from flask import Flask, request, jsonify, render_template

import pickle

app = Flask(__name__)

model_RF=pickle.load(open('RF_winner2.pkl', 'rb')) 
model_KNN=pickle.load(open('KNN_winner2.pkl', 'rb')) 
model_K_SVM=pickle.load(open('K_SVM_winner2.pkl', 'rb')) 
model_DT=pickle.load(open('DT_winner2.pkl', 'rb')) 

@app.route('/')
def home():
  return render_template("index.html")

   
#------------------------------About us-------------------------------------------
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/internshipm')
def internshipm():
    return render_template('internshipm.html')

@app.route('/internship')
def internship():
    return render_template('internship.html')

@app.route('/Blog')
def Blog():
    return render_template('Blog.html')
  

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/Decision')
def Decision():
    return render_template('Decision.html')

@app.route('/Random')
def Random():
    return render_template('Random.html')

@app.route('/SVM')
def SVM():
    return render_template('SVM.html')

@app.route('/KNN')
def KNN():
    return render_template('KNN.html')

@app.route('/knn_predict' , methods=['GET'])
def knn_predict():
    T1= int(request.args.get('T1'))
    T2= int(request.args.get('T2'))
    C = float(request.args.get('C'))
    rl=int(request.args.get('rl'))
    bl=int(request.args.get('bl'))
    Tr=int(request.args.get('Tr'))
    CR=int(request.args.get('CR'))
    RR=int(request.args.get('RR'))
    Wl=int(request.args.get('Wl'))
    prediction = model_KNN.predict([[T1,T2,C,rl,bl,Tr,CR,RR,Wl]])
    if prediction == [1]:
    	return render_template('KNN.html', prediction_text='Batting team Win the match')
    
    else:
    	return render_template('KNN.html', prediction_text='Bowling team Win the match')

@app.route('/svm_predict' , methods=['GET'])
def svm_predict():
    T1= int(request.args.get('T1'))
    T2= int(request.args.get('T2'))
    C = float(request.args.get('C'))
    rl=int(request.args.get('rl'))
    bl=int(request.args.get('bl'))
    Tr=int(request.args.get('Tr'))
    CR=int(request.args.get('CR'))
    RR=int(request.args.get('RR'))
    Wl=int(request.args.get('Wl'))
    prediction = model_K_SVM.predict([[T1,T2,C,rl,bl,Tr,CR,RR,Wl]])
    if prediction == [1]:
    	return render_template('SVM.html', prediction_text='Batting team Win the match')
    
    else:
    	return render_template('SVM.html', prediction_text='Bowling team Win the match')

@app.route('/decision_predict' , methods=['GET'])
def decision_predict():
    T1= int(request.args.get('T1'))
    T2= int(request.args.get('T2'))
    C = float(request.args.get('C'))
    rl=int(request.args.get('rl'))
    bl=int(request.args.get('bl'))
    Tr=int(request.args.get('Tr'))
    CR=int(request.args.get('CR'))
    RR=int(request.args.get('RR'))
    Wl=int(request.args.get('Wl'))
    prediction = model_DT.predict([[T1,T2,C,rl,bl,Tr,CR,RR,Wl]])
    if prediction == [1]:
    	return render_template('Decision.html', prediction_text='Batting team Win the match')
    
    else:
    	return render_template('Decision.html', prediction_text='Bowling team Win the match')

@app.route('/random_predict' , methods=['GET'])
def random_predict():
    T1= int(request.args.get('T1'))
    T2= int(request.args.get('T2'))
    C = float(request.args.get('C'))
    rl=int(request.args.get('rl'))
    bl=int(request.args.get('bl'))
    Tr=int(request.args.get('Tr'))
    CR=int(request.args.get('CR'))
    RR=int(request.args.get('RR'))
    Wl=int(request.args.get('Wl'))
    prediction = model_RF.predict([[T1,T2,C,rl,bl,Tr,CR,RR,Wl]])
    if prediction == [1]:
    	return render_template('Random.html', prediction_text='Batting team Win the match')
    
    else:
    	return render_template('Random.html', prediction_text='Bowling team Win the match')



if __name__=="__main__":
  app.run(debug=True)
  
