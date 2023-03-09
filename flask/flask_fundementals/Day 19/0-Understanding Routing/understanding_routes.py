from flask import Flask, make_response
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/dojo')
def greeting():
    return 'Dojo!'


@app.route('/say/<name>')
def sayhello(name):
    print(name)
    return 'Hello  ' + name


@app.route('/repeat/<num>/<text>')
def hellowworld(num, text):
    if num == 0 or text == '':
        return make_response(("Not found", 404))
    else:
        return ((text+"<br>")*int(num))


if __name__ == "__main__":
    app.run(debug=True)
