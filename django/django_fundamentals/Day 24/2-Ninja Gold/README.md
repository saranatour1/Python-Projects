# Explanition of the whole proccess

So, this took me 4 hours to figure out.. I got frusrated with how much i've written in code to the point where I'm conviced I did something wrong, So I have to re-iterate.

- I have one last task that I decided It's too much to do it after 4 hours.

## steps

1. General steps:
   I followed the steps of creating a file up untill the 'deployment' to localhost:8000 , so I will not go through them here.
2. Topics and standarlization of requirements:
   I was asked to do the following:

- Make a wire frame (which I did in almost 30-40min)
- Have the four forms appear when the user goes to http://localhost:8000 (easy sleasy)
- Use a hidden input tag in each form to pass the relevant location to the server (followed from the material as well)
- Have /process_money determine how much gold the user should have For now, save the activity log in session (Done but after 4 hours).

2. Files Steps:
   in the Html, I have created 4 forms that have similar syntax

```html
<div class="form">
  <form method="post" action="/process_money">
    {% csrf_token %}
    <input type="hidden" name="which_form" value="farm" />
    <h1>Farm</h1>
    <p>Earns (10-20) Golds</p>
    <input type="submit" value="Find Gold!" />
  </form>
</div>
```

My eyes are not able to see the view file from how much text is present,but in that file , I am able to access the form value like this:

```python
def process_money(request):
  if request.method == 'POST':
    form_name = request.POST['which_form']
    if request.POST.get('which_form') == 'farm':
      #farm related code here
    elif request.POST.get('which_form') == 'cave':
      #cave related code here
    elif request.POST.get('which_form') == 'house':
      #house related code here
    elif request.POST.get('which_form') == 'quest':
      #quest related code here
    return redirect('/')
```

So here I have created a mistake, where I am refrencing te form_name from the request, instead of maybe saving it to the session? although the session size is fixed to 4KB when there is no database for dejango -I'm not 100% sure-,So I will leave it at that.
next step, is to check wether there is a post operation happening, and if so, return the 'case' to the front end side, so staring from the html:

```html
<div class="Gold-input-from-python">
  <label class="gold" for="gold">Your Gold</label>
  <div class="gold-container"><span>{{count}}</span></div>
</div>
```

to the python views.py file:

```python
def process_money(request):
  request.session['proccessed']=False
  x = 0
  random_operator = 0
  if request.method == 'POST':
    x = random.randint(10, 20)
    random_operator = random.randint(0, 1)
    request.session['random_oparator']=random_operator
    quest_random_int= random.randint(0, 50)
    current_count=request.session.get('count', 0)
    request.session['request_activity']=x
    if request.POST.get('which_form') == 'farm':
      request.session['count'] = current_count + x
    elif request.POST.get('which_form') == 'cave':
      request.session['count'] = current_count + x
    elif request.POST.get('which_form') == 'house':
      request.session['count'] = current_count + x
    elif request.POST.get('which_form') == 'quest':
      if random_operator == 0:
        request.session['count'] = current_count -quest_random_int
        request.session['request_activity']=quest_random_int
      else:
        request.session['count'] = current_count +quest_random_int
        request.session['request_activity']=quest_random_int

    return redirect('/')
```

Confused No more! here is the descreption:

- first, I check wether there is a post request happening through '`if request.method == 'POST':`'
- the count is refrenced by `current_count` which gets the count from the session by using the 'get' function, and if count is not there the value is passed as zero
- 'x' refrences the random integer from 10-20 that is added to the gold when one the three is refrenced
- 'quest_random_int' refrences the one time when Quest is accessed, the random int becomes ranged from 0-50
- 'random_operator' refrences the randomized time of when to add or decrement some of the gold based on the Quest as well
- and that's it for this one.
  untill now, the gold is the only thing that is being proccesed. there is a section called Activites, where the actions are being refrenced by form name, time, date , and amount of gold, let's iterate the proccess of this one again:

```python
    request.session['time']=strftime("%I:%M:%S %p", localtime())
    request.session['date']= strftime("%B %d %Y", localtime())
    print(request.session['time'],request.session['date'])
    activity_str = (f"You entered a {form_name} and got {x} golds on ({request.session.get('date')} {request.session.get('time')})")
    activities = request.session.get('activities', [])
    activities.append(activity_str)
    request.session['activities'] = activities

```

- the time is being taken from my computer's local time -I hope I understood this correctly-, and the date as well
- I went back and fourth with the message part of the code, beacause appearantly making a for loop is hard, So I went ahead, created a list, where each activity is being held into activites, and activites is being put in the session, I can see my problems now, but since it works I will not touch it.
- Huh. the HTML. this is where I made the decession to not ever have to do this again without planning.
  ```html
  <div class="activites">
    <h3>Activites:</h3>
    <div class="big-box">
      <div class="scroll-down">
        {% if activities%} {% for activity in activities %}
        <p>{{ activity }}</p>
        {% endfor %} {% else %}
        <p>No activities to show.</p>
        {% endif %}
      </div>
    </div>
  </div>
  ```
  I always thought that this line is very funny '`something= !something`'
- I am at 5 hours now, and I completlyforgot the rest, but in the root where everyhting is being redirected:

```python
def index(request):
  count = request.session.get('count', 0)
  request_activity=request.session.get('request_activity',0)
  time =request.session.get('time',0)
  date=request.session.get('date',0)
  proccessed=request.session.get('proccessed')
  activities = request.session.get('activities', [])
  random_oparator=request.session.get('random_oparator')
  context = {'count': count,'request_activity':request_activity, 'time':time, 'date':date,'proccessed':proccessed ,'activities':activities,'random_oparator':random_oparator }
  return render(request, 'index.html', context)

```
I have one last thing to do, which is when the amount is decreased I need to change the colors of the text from green to red, I'm one if statment away.

that is all, and You can Clone the directory, cd into dojo_gold to check everything. Just incase I may not add .png's to the readme.
I'm finished.
