from django.shortcuts import render
from time import gmtime, strftime,localtime
def display_time(request):
    context = {
        "time": strftime("%H:%M:%S %p", localtime()),
        "date":strftime("%Y-%m-%d",localtime())    }
    print(context)
    return render(request,'index.html', context)

