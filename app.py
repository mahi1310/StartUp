from flask import Flask,render_template,request
from sklearn.ensemble import RandomForestClassifier
import pickle

app=Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        relationships=int(request.form['relationships'])
        funding_rounds=int(request.form['funding_rounds'])
        funding_total_usd=int(request.form['funding_total_usd'])
        milestones=int(request.form['milestones'])
        avg_participants=int(request.form['avg_participants'])

    data=[[int(relationships),int(funding_rounds),int(funding_total_usd),int(milestones),int(avg_participants)]]
    pk=pickle.load(open('C:/Users/Mahitha/OneDrive/Documents/flask/.venv/Include/predict.pkl','rb'))
    prediction=pk.predict(data)[0]

    if relationships<=0 and funding_rounds<=0 and funding_total_usd<=0 and milestones<=0 and avg_participants<=0:
       prediction='PLEASE ENTER VALID DATA'
    elif milestones< 4:
       prediction='OUR PREDICTION SAYS THAT YOUR STARTUP MIGHT FAIL AS milestones ARE LESS'\
        '. PLEASE TRY TO INCREASE milestones THEN YOU WILL DEFINITELY SUCCEED.'
    elif relationships< 4:
        prediction='OUR PREDICTION SAYS THAT YOUR STARTUP MIGHT FAIL AS relationships ARE LESS'\
         '. PLEASE TRY TO INCREASE relationships THEN YOU WILL DEFINITELY SUCCEED.'
    elif funding_rounds< 4:
        prediction='OUR PREDICTION SAYS THAT YOUR STARTUP MIGHT FAIL AS funding_rounds ARE LESS'\
        '. PLEASE TRY TO INCREASE funding_rounds THEN YOU WILL DEFINITELY SUCCEED.'
    elif funding_total_usd< 50000:
       prediction='OUR PREDICTION SAYS THAT YOUR STARTUP MIGHT FAIL AS TOTAL AMOUNT IS NOT SUFFICIENT, PLEASE TRY TO INCREASE funding_rounds'\
        ' THEN AUTOMATICALLY THE TOTAL AMOUNT WILL INCREASE AND YOU WILL DEFINITELY SUCCEED.'
    else:
       prediction='OUR PREDICTION SAYS THAT YOUR STARTUP WILL HOPEFULLY A SUCCESS.'
    return render_template('index.html',prediction=prediction,relationships=relationships,funding_rounds=funding_rounds,funding_total_usd=funding_total_usd,
                           milestones=milestones,avg_participants=avg_participants)

if __name__=="__main__":
    app.run(debug=True)