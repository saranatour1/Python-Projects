from flask import Flask, render_template 

app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return 'Hello World!'

@app.route('/play')
def layout_1():
    return render_template('index.html',layout='layout_1')

@app.route('/play/<int:num_box>')
def multiple_layouts(num_box):
  return render_template('index.html', layout='layout_2', num_box=num_box)

@app.route('/play/<int:num_box>/<color>')
def layout_3(num_box, color):
    return render_template('index.html', layout='layout_3', num_box=num_box, color=color)


if __name__ == "__main__":
    app.run(debug=True)






