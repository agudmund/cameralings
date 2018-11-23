from django.shortcuts import render

context = {'first_name':'first','last_name':'last'}

def home(request):

    return render(request, 'tick/index.html',{'data': context})