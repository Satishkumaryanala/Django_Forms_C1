from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.


def insert_student(request):
    SFEO = StudentForm()
    d={'SFEO':SFEO}
    if request.method == 'POST':
        SFDO = StudentForm(request.POST)
        if SFDO.is_valid():
            sname = SFDO.cleaned_data['Sname']
            sid = SFDO.cleaned_data['Sid']
            semail = SFDO.cleaned_data['Semail']

            return HttpResponse('<h1 style="color:green;"><center><i>Data submitted successfully</i></center></h1>')

    return render(request,'DJforms.html',d)