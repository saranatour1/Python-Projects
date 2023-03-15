import random
from django.shortcuts import render

def index(request):

  if request.method == 'POST':
    number = int(request.POST.get('number'))
    x = int(request.session.get('x'))
    win=False
    if number < x:
      message = 'Too low!'
    elif number > x:
      message = 'Too high!'
    else:
      message = (f'You guessed it! the number is {x}')
      win=True
      request.session.flush()
    context = {'message': message ,'win':win}
  else:
    x = random.randint(1, 100)
    request.session['x'] = x
    context = {'x': x}
  return render(request, 'index.html', context)
