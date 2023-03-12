This is the steps that I took to solve this assignemnt: 
I first created the 8*8 checker board, To see how it would look like, I alternated between using a table element or a regular div and stuck wth a tabe: 
```html
 <table>
      <tr>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
      </tr>
      <tr>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
      </tr>
      <tr>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
      </tr>
      <tr>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
      </tr>
      <tr>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
      </tr>
      <tr>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
      </tr>
      <tr>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
      </tr>
      <tr>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
        <td class="black" ></td>
        <td class="white" ></td>
      </tr>
    </table>

```

for  this, the output looked something like this: 

![image](https://user-images.githubusercontent.com/77834808/224545338-02c42c71-5936-4971-9a4e-f4c0cc4a452a.png)

then I started manipulating the look of the output in a for loop, where each row contains a black element when the row and table are 'even' numbers, 
```html
<table>
  <!-- Remember to take the i and j :) -->
  {% for i in range(row) %}
  <tr>
    {% for j in range(col) %}
      {% if (i+j) % 2 == 0 %}
        <td class="black"></td>
      {% else %}"
        <td class="white"></td>
      {% endif %}
    {% endfor %}
  </tr>
{% endfor %}
</table>

```
note that, I reffered the col and row variables in the flask app, to reduce one step, and to make sure that the two are connected. 
in the flask app: 

```python3
@app.route("/")
def hello_world(row=8 , col=8):
  return render_template("index.html", row=row, col=col)
```
and the output stays the same no matter what!
then I was wondering if I could refer to the routes as one route, as if I could edit one of the routes and it wouldn;t effect the other, an that appearantly was the best idea I had, In the second part I tried that: 
```python3
@app.route("/")
@app.route("/<int:small>")
def hello_world(row=8 , col=8,small=8):
  row=small
  return render_template("index.html", row=row, col=col, small=small)
```
So this makes sure that row stays at 8 when requested, and it wouldn't effect the row anywhere else, it would keep the column at default. 
here is a screenshot:  **I know I messed up the colors**
```python3

@app.route("/")
@app.route("/<int:small>")
def hello_world(row=8 , col=8,small=8):
  row=small
  return render_template("index.html", row=row, col=col, small=small)
```


![image](https://user-images.githubusercontent.com/77834808/224545875-7d7d1a3f-d0ae-4503-965b-b2a088262cc0.png)

next is super easy to achieve, since I deducted a step above, everything will be normal:
```python3

@app.route("/")
@app.route("/<int:small>")
@app.route("/<int:row>/<int:col>")
def hello_world(row=8 , col=8,small=8,color1="#000" , color2="#ff0000"):
  row=small
  return render_template("index.html", row=row, col=col, small=small)

```
![image](https://user-images.githubusercontent.com/77834808/224545975-c775534b-754a-437d-9ecc-8c18fc3f959e.png)
and last but least, the colors! 
this is what I did in the html to fixate the colors: 
```html
<table>
  <!-- Remember to take the i and j :) -->
  {% for i in range(row) %}
  <tr>
    {% for j in range(col) %}
      {% if (i+j) % 2 == 0 %}
        <td style="background-color:{{color2}};"></td>
      {% else %}
        <td style="background-color:{{color1}};"></td>
      {% endif %}
    {% endfor %}
  </tr>
{% endfor %}
</table>

```
and here is the edited python code : 
```python3
@app.route("/")
@app.route("/<int:small>")
@app.route("/<int:row>/<int:col>")
@app.route("/<color1>/<color2>")
def hello_world(row=8 , col=8,small=8,color1="#000" , color2="#ff0000"):
  row=small
  return render_template("index.html", row=row, col=col, small=small,color1=color1,color2=color2)
```
I would make another modification to the pyhton code: 
```python3
@app.route("/")
@app.route("/<color1>/<color2>")
@app.route("/<int:small>")
@app.route("/<int:row>/<int:col>/<color1>/<color2>")
def hello_world(row=8 , col=8,small=8,color1="#000" , color2="#ff0000"):
  row=small
  return render_template("index.html", row=row, col=col, small=small,color1=color1,color2=color2)

```
![image](https://user-images.githubusercontent.com/77834808/224546116-43e9be00-5bce-4abc-bd95-f3acd8c61a58.png)


and I would make one last modification to the html,using ternary operator: 
```html
<table>
  <!-- Remember to take the i and j :) -->
  {% for i in range(row) %}
  <tr>
    {% for j in range(col) %}
        <td style="background-color: {{ color2 if (i+j) % 2 else color1 }};"></td>
    {% endfor %}
  </tr>
{% endfor %}
</table>
```

and I made sure everything still works as intended! 














































