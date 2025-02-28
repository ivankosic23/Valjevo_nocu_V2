from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Kafic,Svirka
from datetime import datetime, timedelta


# Create your views here.

def home(request):
    days_serbian = [
        'Ponedeljak',  # Monday
        'Utorak',      # Tuesday
        'Sreda',       # Wednesday
        'Četvrtak',    # Thursday
        'Petak',       # Friday
        'Subota',      # Saturday
        'Nedelja' 
                 ]
    today = datetime.now()
    dani=[]
    days =today.weekday()
    for i in range(7):
        
        dayi=days_serbian[(days + i) % 7]
        dayindex=(days+i)%7
        dani.append((dayi,dayindex))
    #Kontejneri sa kaficima
    svirke = Svirka.objects.all()
    return render(request,"home.html",{'days':dani,
                                       'svirke':svirke})


def relja(request):
    kafici=Kafic.objects.all()
    return render(request,'admin.html',{'kafici':kafici})

def dogadjaj(request):
    if request.method=='POST':
        ime =request.POST['Kafic']
        datum =request.POST['datum']
        opis= request.POST['opiskafic']
        dodati_dogadjaj=Svirka(ime=ime,datum=datum,opis=opis)
        dodati_dogadjaj.save()
        return render(request,"admin.html",{})
    
def create_svirka(request):
    if request.method == 'POST':
        # Get data from the request
        date_str = request.POST.get('datum')
        opis = request.POST.get('opis')
        kafic_id = request.POST.get('kafic')  # Get the selected Kafic ID

        if date_str:
            datum = datetime.strptime(date_str, '%Y-%m-%d').date()
        # Create a new Svirka instance
            if kafic_id:
                kafic = Kafic.objects.get(ID=kafic_id)  # Fetch the Kafic instance
                Svirka.objects.create(
                    ime=kafic.Ime,
                    datum=datum,
                    opis=opis,
                    kafic=kafic
                )
                return redirect('create_svirka')

    kafici=Kafic.objects.all()
    return render(request, 'admin.html', {'kafici': kafici})
