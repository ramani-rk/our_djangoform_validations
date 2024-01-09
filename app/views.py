from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse

def create_school(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['Sname']   
            sp=SFDO.cleaned_data['Sprincipal']
            sl=SFDO.cleaned_data['Slocation']
            e=SFDO.cleaned_data['email']
            c=SFDO.cleaned_data['confirmemail']
            SO=School.objects.get_or_create(Sname=sn,Sprincipal=sp,Slocation=sl,email=e,confirmemail=c)[0]
            SO.save()
            return HttpResponse('School is created')
        else:
            return HttpResponse('invalid data')
    return render (request,'create_school.html',d)


def create_web(request):
    EWFO=WebForm()
    d={'EWFO':EWFO}

    if request.method=='POST':
        WFDO=WebForm(request.POST)
        if WFDO.is_valid():
            sn=WFDO.cleaned_data['Sname']   
            sc=WFDO.cleaned_data['Scont']
            sa=WFDO.cleaned_data['Sadd']
            SN=School.objects.get(Sname=sn)
            WO=Webpage.objects.get_or_create(Sname=SN,Scont=sc,Sadd=sa)[0]
            WO.save()

            return HttpResponse('Webpage is created')
        else:
            return HttpResponse('invalid data')
    return render (request,'create_web.html',d)