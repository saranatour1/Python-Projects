#Flask and templete rendering overview 
This is a New topic for me so Here is a snippet of What I did for my future self: 
## Steps 
1. I first accessed the html file like normal, I created 3 divs for the first layout, and Made sure that there class is 'Layout_1, Layout_2 , Layout_3'
2. I took the first part of the question before jumping to  the next, when I access the '/play' route I am supposed to recieve a welcome message and 3 boxes, So thats exactly what I did:
```python3
# accessing the Flask app like normal :
from flask import Flask, render_template 

app = Flask(__name__) 
# then, I access 1 or more of these routes: 
@app.route('/')          
def hello_world():
    return 'Hello World!'

@app.route('/play')
def layout_1():
    return render_template('index.html')
    
```
3. Next , in the index.html file I build the boxes like normal: 
```html
 <div class="layout_1">
      <h1>Welcome!</h1>
      <div class="boxes">
        <div class="blue-box"></div>
        <div class="blue-box"></div>
        <div class="blue-box"></div>
      </div>
    </div>
```
And here is the regular output of this: 






























