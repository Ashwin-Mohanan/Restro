from tokenize import Name
from django.http import HttpResponse
from django.shortcuts import render
from testapp.models import Restro
from django.db.models import Q
from django.views.generic import View,ListView,DetailView
# Create your views here.
def main(request):
    return render(request,'testapp.main.html')
class Home(View):
    def get(self,request):
        return render(request,'testapp/home.html')

def RestroDetails(request):
        Dish=Restro.objects.all()
        return render(request,'testapp/restro_details.html',{'Dish':Dish})

# def Restrofilter(request):
#     if request.method == 'POST':
#         name=request.POST['name']
#         # price=request.POST['Price']
#         # taste=request.POST['Taste']
#         Dish=Restro.objects.all()
#         if name:
#             Dish=Restro.objects.filter(Name__icontains=name)
#         # if price:
#         #     Dish=Restro.filter(Price__name=price)
#         # if taste:
#         #     Dish=Restro.filter(Taste__name=taste)
#         return render(request,'testapp/restro_details.html',{'dish':Dish})
#     elif request.method =='GET':
#         return render(request,'testapp/filter.html') 

def Restrofilter(request):
    if request.method=="POST":
        name=request.POST.get('Name')
        searched=Restro.objects.all()
        if name:
            searched=Restro.objects.filter(Name__icontains=name)
        
        return render(request,'testapp/filter.html',{'searched':searched})

    elif request.method =='GET':
        return render(request,'testapp/home.html')

    else:
        return HttpResponse("ERRORR")
