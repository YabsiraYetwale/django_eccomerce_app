from django.shortcuts import render
from item.models import ItemModel

def dashboard(request,):
    items=ItemModel.objects.filter(creator=request.user)
    return render(request,'item/dashboard.html',{'items':items})