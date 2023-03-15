from django.shortcuts import render, HttpResponse, redirect
import random  # import the random module
from time import gmtime, strftime,localtime

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

def process_money(request):
  request.session['proccessed']=False
  x = 0
  random_operator = 0
  if request.method == 'POST':
    form_name = request.POST['which_form']
    request.session['proccessed']=True
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

    request.session['time']=strftime("%I:%M:%S %p", localtime())
    request.session['date']= strftime("%B %d %Y", localtime())
    print(request.session['time'],request.session['date'])
    activity_str = (f"You entered a {form_name} and got {x} golds on ({request.session.get('date')} {request.session.get('time')})")
    activities = request.session.get('activities', [])
    activities.append(activity_str)
    request.session['activities'] = activities
    
    return redirect('/')
