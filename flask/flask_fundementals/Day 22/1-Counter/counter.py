from flask import Flask, render_template  ,redirect,session
app = Flask(__name__)                     
app.secret_key = 'counter'  
    
@app.route('/')                           
def counter():
    if 'counter' not in session:
        session['counter']=1
    else:
        session['counter']+=1
    
    return render_template("counter.html",x=session['counter'])

@app.route('/destroy_session')
def resetCountt():
    session.pop('counter')
    return redirect ('/')


  
if __name__=="__main__":
    app.run(debug=True)                   

