
from django.shortcuts import render,redirect

def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    
    context = {
        'counter': request.session['counter']
    }
    
    return render(request, 'index.html', context)

def destroy_session(request):
  del request.session['counter']	# clears a specific key
  return redirect('/')

def increment(request):
  request.session['counter'] += 1
  return redirect('/')