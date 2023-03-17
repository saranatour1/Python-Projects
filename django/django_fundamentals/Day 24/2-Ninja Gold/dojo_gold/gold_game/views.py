#import the needed libraries, like render redirect , random and time
from django.shortcuts import render, HttpResponse, redirect
import random  
from time import gmtime, strftime,localtime

# the main method 

def index(request):
  context = {'count': request.session.get('count', 0),
            'activities':request.session.get('activities', []),
            }  
  return render(request, 'index.html', context)

def process_money(request):
  x = 0
  if request.method == 'POST':
      form_name = request.POST['which_form']
      x = random.randint(10, 20)
      quest_random_int = random.randint(-50, 50)
      current_count = request.session.get('count', 0)
      request.session['request_activity'] = x
      
      if form_name in ['farm', 'cave', 'house']:
          request.session['count'] = current_count + x
      elif form_name == 'quest':
          request.session['count'] = current_count + quest_random_int
          request.session['request_activity'] = quest_random_int
          
      request.session['time'] = strftime("%I:%M:%S %p", localtime())
      request.session['date'] = strftime("%B %d %Y", localtime())
      
      if form_name == 'quest':
          if quest_random_int < 0:
              activity_str = (f'<p class="red">'
                              f'You entered a {form_name} and lost {-quest_random_int} golds on '
                              f'{request.session.get("date")} {request.session.get("time")}</p>')
          else:
              activity_str = (f'<p class="green">'
                              f'You entered a {form_name} and got {quest_random_int} golds on '
                              f'{request.session.get("date")} {request.session.get("time")}</p>')
      else:
          activity_str = (f'<p class="green">'
                          f'You entered a {form_name} and got {x} golds on '
                          f'{request.session.get("date")} {request.session.get("time")}</p>')
          
      activities = request.session.get('activities', [])
      activities.append(activity_str)
      request.session['activities'] = activities
      
      return redirect('/')


