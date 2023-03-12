from flask import Flask,render_template 

app = Flask(__name__)

@app.route("/")
@app.route("/<int:small>")
@app.route("/<int:row>/<int:col>")
@app.route("/<color1>/<color2>")
def hello_world(row=8 , col=8,small=8,color1="#000" , color2="#ff0000"):
  row=small
  return render_template("index.html", row=row, col=col, small=small,color1=color1,color2=color2)