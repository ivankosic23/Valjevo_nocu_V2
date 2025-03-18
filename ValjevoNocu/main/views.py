from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
    days_serbian_padezi = [
        'ponedeljak',  # Monday
        'utorak',      # Tuesday
        'sredu',       # Wednesday
        'četvrtak',    # Thursday
        'petak',       # Friday
        'subotu',      # Saturday
        'nedelju' 
                 ]
    today = datetime.now()
    dani=[] 
    days =today.weekday()
    daysi=today.strftime("%Y-%m-%d")
    for i in range(7):
        
        dayi=days_serbian[(days + i) % 7]
        danpom=(today + timedelta(days=i))
        dayindex = danpom.strftime("%Y-%m-%d")
        dani.append((dayi,dayindex))
    
    day_index = int(request.GET.get('day_index',0))
    selected_day = request.GET.get('datum', daysi)

    if day_index < 0:
            day_index = len(dani) - 1  # Set to last index
    elif day_index >= len(dani):
        day_index = 0

    try:
        date_object = datetime.strptime(selected_day, "%Y-%m-%d").date()+timedelta(days=day_index)
        danilabel=date_object.weekday()
        danilab=days_serbian_padezi[danilabel]
    except ValueError:
         danilab = "Invalid date"

    
    current_label=dani[day_index][0]

    svirkes = Svirka.objects.select_related('kafic').filter(datum=daysi)
    if selected_day is not None:
             svirkes = Svirka.objects.select_related('kafic').filter(datum=date_object)
    #Kontejneri sa kaficima

    return render(request,"home.html",{'days':dani,
                                       'svirke':svirkes,
                                       'danlabel':danilab,
                                       'day_index':day_index,
                                       'current_label':current_label,
                                       'day_date':daysi})

@login_required
def dogadjaj(request):
    if request.method=='POST':
        ime =request.POST['Kafic']
        datum =request.POST['datum']
        opis= request.POST['opiskafic']
        dodati_dogadjaj=Svirka(ime=ime,datum=datum,opis=opis)
        dodati_dogadjaj.save()
        return render(request,"admin.html",{})
@login_required   
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

