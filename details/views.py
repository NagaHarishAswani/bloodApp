from django.shortcuts import render
from django.http import HttpResponse
from details.models import DonorModel
from django.db.models import Max
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
#use aggregate for operations

def homepage(request):
    return render(request,'index.html')

from django.shortcuts import render

def newDonor(request):
    if request.method == 'POST':
        DonorModel(
              name = request.POST.get('dname'),
              age = request.POST.get('dage'),
              bg = request.POST.get('dbg'),
              gender = request.POST.get('dgender'),
              city = request.POST.get('dcity'),
              phno = request.POST.get('dno'),
        ).save()
        return render(request, 'EntryForm.html', {'message': 'Donor Successfully added'})
    return render(request, 'EntryForm.html')



def searchDonor(request):
    if request.method == 'POST':
        sdbg = request.POST.get('sdbg')
        sdcity = request.POST.get('sdcity')
        donor = DonorModel.objects.filter(Q(bg=sdbg) | Q(city=sdcity))
        if sdbg and sdcity:
            donor = donor.filter(bg=sdbg, city=sdcity)
        if len(donor) == 0:
            flag = True
        else:
            flag = False
        return render(request,'search.html',{"don":donor, "flag":flag})
    else:
        return render(request,"search.html")



def seeall(request):
    donor = DonorModel.objects.all().order_by('age')
    return render(request,"display.html",{"don":donor})

def update_delete(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        donor = DonorModel.objects.filter(phno=phone_number).first()
        if donor:
            return render(request, 'update_delete.html', {'donor': donor})
        else:
            return render(request, 'update_delete.html', {'error_message': 'Donor not found.'})
    return render(request, 'update_delete.html')

def update_donor(request, id):
    donor = DonorModel.objects.get(id=id)
    
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        age = request.POST.get('age')
        bg = request.POST.get('bg')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        phno = request.POST.get('phno')
        
        # Update donor details
        donor.name = name
        donor.age = age
        donor.bg = bg
        donor.gender = gender
        donor.city = city
        donor.phno = phno
        donor.save()
        
        return redirect('/')
    
    return render(request, 'update.html', {'donor': donor})

def delete_donor(request, id):
  
    donor = DonorModel.objects.get(id=id)
    
    if request.method == 'POST':

        donor.delete()
        messages.success(request, 'Donor deleted successfully')
        return render(request, 'delete.html', {'message': 'Donor deleted successfully', 'back_button': True})
    
    return render(request, 'delete.html', {'donor': donor, 'back_button': False})