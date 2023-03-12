from flask import Flask, render_template 
# from markupsafe import escape
app = Flask(__name__)

@app.route('/') # home page will get 
@app.route('/<int:size>')
@app.route('/<int:width>/<int:height>')
@app.route('/<int:width>/<int:height>/<color1>/<color2>')
def homepage(size=8, width=8, height=8, color1='black' ,color2='#ff0000'):
  if width==8 and size==8:
    return render_template('index.html', size=size, width=width, height=height ,color1=color1, color2=color2)
  elif size==4:
    return render_template('index.html',size=8,width=8 ,height=4,color1=color1, color2=color2)
  elif not color1 and not color2:
    return render_template('index.html',size=8,width=8 ,height=4,color1=color1, color2=color2)
  else:
    return render_template('index.html', size=8, width=8, height=height,color1=color1, color2=color2)





