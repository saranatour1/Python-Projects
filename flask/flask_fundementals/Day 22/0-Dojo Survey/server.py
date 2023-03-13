from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/")
def form_start():
    return render_template('index.html')
  
@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form=request.form['language']
    comments_from_form=request.form['comments']
    likes_from_form=request.form['options']
    accept_terms=request.form['terms']
    return render_template("result.html", name_on_template=name_from_form, location_from_template=location_from_form,language_on_template=language_from_form,comments_on_template=comments_from_form ,likes_on_templates=likes_from_form,terms_on_template=accept_terms)
  
@app.route('/')
def go_back():
    return redirect('/')    