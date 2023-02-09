from django.shortcuts import render
from .models import Customer,Transfer
from django.http import HttpResponse
# Create your views here.
def home(request):
    obj = Customer.objects.all()
    return render(request,'userapp/index.html',{'customers':obj})

def customerDetails(request,id):
    obj = Customer.objects.get(id=int(id))
    return render(request,'userapp/details.html',{'detail':obj})

def transfer(request,id):
    obj = Customer.objects.get(id=int(id))
    return render(request,'userapp/list.html',{'customers':Customer.objects.all(),'user':obj})

def execute(request,id1=None,id2=None):
    if request.method == 'POST':
        amount = int(request.POST.get('amount'))
        obj1 = Customer.objects.get(id=int(id1))
        obj2 = Customer.objects.get(id=int(id2))
        obj1.curr_balance-=amount
        obj2.curr_balance+=amount
        obj1.save()
        obj2.save()
        obj3 = Transfer.objects.create(fromuser=obj1,touser=obj2,amount=amount)
        obj3.save()
        return HttpResponse('<h1>Transaction successfull</h1>')
    obj1 = Customer.objects.get(id=int(id1))
    obj2 = Customer.objects.get(id=int(id2))
    return render(request,'userapp/execute.html',{'fromuser':obj1,'touser':obj2})
