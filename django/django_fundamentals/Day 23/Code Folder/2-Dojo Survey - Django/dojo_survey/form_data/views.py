from django.shortcuts import render
def index(request):
    return render(request,"index.html")
def result(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    language_on_form=request.POST['language']
    # like_on_form=request.POST['options']
    options_from_form = request.POST.get('options')
    comments_on_form=request.POST['comments']
    # terms_on_form=request.POST['terms']
    terms_on_form = request.POST.get('terms')

    context = {
        "name_on_template" : name_from_form,
        "location_on_template" : location_from_form,
        "language_on_template":language_on_form,
        "likes_on_template": options_from_form,
        "comments_on_template":comments_on_form,
        "terms_on_template":terms_on_form,
    }
    return render(request,"show.html",context)