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

![image](https://user-images.githubusercontent.com/77834808/224062759-8dd0cdbc-c277-4228-aade-3b2535195c3c.png)

and that's exactly it for this one! 
4. going on to the next part, which is if I want another layout in the same html page, I found this to be a pretty good resource <a href="https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application">Digital Ocean</a> its a good  start!
```python3
@app.route("/example")
def example():
    return render_template("example.html", layout_class="child-layout")
```
5.Going back to the html, we neeed to impply what is happening to the layout each time a request is happening, If you are thinking about an if statment You are not wrong 
```html
 {% if layout == 'layout_1' %}
    <div class="layout_1">
      <h1>Welcome!</h1>
      <div class="boxes">
        <div class="blue-box"></div>
        <div class="blue-box"></div>
        <div class="blue-box"></div>
      </div>
    </div>
<!--this is a jinja's thing  -->
```
then in the python file, some changes will be made to bothe functions:
```python3
@app.route('/play/<int:num_box>')
def multiple_layouts(num_box):
  return render_template('index.html', layout='layout_2', num_box=num_box)


```
based on the number taken from the url, it should apear like this: 
![image](https://user-images.githubusercontent.com/77834808/224075748-45c1a3bf-dab4-4390-b1e2-d9ea04faac7b.png)

**using a grid instead of flex is a better choice here** 

I think knowing that little trick made such a difference to the next part of the requirments,with a forloop in the html, it should endup looking like this:
```python3

@app.route('/play/<int:num_box>/<color>')
def layout_3(num_box, color):
    return render_template('index.html', layout='layout_3', num_box=num_box, color=color)
```

![image](https://user-images.githubusercontent.com/77834808/224076677-85dd1eb8-a5d8-49ee-936b-1a0931fca265.png)




One Quick piece of advice, don't be limited to 1 single resource, that is really not good,so don't be a box. 















