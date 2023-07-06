from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.http import HttpResponse

def djangoforms(request):
    SUFO=SignUpForm()
    d={'SUFO':SUFO}
    if request.method=='POST':
        SUFDT=SignUpForm(request.POST)
        if SUFDT.is_valid():
            name=SUFDT.cleaned_data['name']
            return HttpResponse(str(SUFDT.cleaned_data))
    return render(request,'djangoforms.html',d)